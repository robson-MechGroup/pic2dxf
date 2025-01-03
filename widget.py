import cv2
import numpy as np
import os
import sys
import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from form import Ui_Widget

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.scale_factor = 1.1  # Zoom in/out factor

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(self.scale_factor, self.scale_factor)  # Zoom in
        else:
            self.scale(1 / self.scale_factor, 1 / self.scale_factor)  # Zoom out

class ContourApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setup_connections()
        self.image_path = None

        # Replace GraphicsViews with zoomable views
        self.ui.inputimage = ZoomableGraphicsView(self.ui.inputimage.parent())
        self.ui.edges = ZoomableGraphicsView(self.ui.edges.parent())
        self.ui.contour1 = ZoomableGraphicsView(self.ui.contour1.parent())
        self.ui.finalContour = ZoomableGraphicsView(self.ui.finalContour.parent())

        # Add widgets to layouts dynamically
        self.ui.gridLayout.addWidget(self.ui.inputimage, 0, 0)
        self.ui.gridLayout.addWidget(self.ui.edges, 0, 1)
        self.ui.gridLayout.addWidget(self.ui.contour1, 1, 0)
        self.ui.gridLayout.addWidget(self.ui.finalContour, 1, 1)

    def setup_connections(self):
        self.ui.browseImage.clicked.connect(self.browse_image)
        self.ui.loadImage.clicked.connect(self.load_image)
        self.ui.preview.clicked.connect(self.preview_image)
        self.ui.save.clicked.connect(self.save_output)

    def browse_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        if file_dialog.exec():
            self.image_path = file_dialog.selectedFiles()[0]
            self.ui.filePath.setText(self.image_path)

    def load_image(self):
        if self.image_path:
            image = cv2.imread(self.image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            q_image = QImage(
                image.data, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888
            )
            pixmap = QPixmap.fromImage(q_image)
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            self.ui.inputimage.setScene(scene)
        else:
            print("No image selected")

    def preview_image(self):
        if not self.image_path:
            print("No image loaded")
            return

        try:
            blur_kernel = int(self.ui.blurKernelSize.text())
            blur_sigma = float(self.ui.blurSigma.text())
            canny_thresh1 = int(self.ui.cannyThreshold1.text())
            canny_thresh2 = int(self.ui.cannyThreshold2.text())
            closing1_kernel = int(self.ui.closing1Kernel.text())
            closing2_kernel = int(self.ui.closing2Kernel.text())
            smooth_window_size = int(self.ui.smoothWindowSize.text())

            image = cv2.imread(self.image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), blur_sigma)
            edges = cv2.Canny(blurred, canny_thresh1, canny_thresh2)

            kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (closing1_kernel, closing1_kernel))
            kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (closing2_kernel, closing2_kernel))
            closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel1)
            closed_edges = cv2.morphologyEx(closed_edges, cv2.MORPH_CLOSE, kernel2)

            contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            largest_contour = max(contours, key=cv2.contourArea)

            contour_image = np.zeros_like(image)
            cv2.drawContours(contour_image, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)

            smoothed_contour = self.smooth_contour(largest_contour, smooth_window_size)
            final_image = contour_image.copy()
            cv2.drawContours(final_image, [smoothed_contour], -1, (0, 255, 0), thickness=2)

            self.display_image(edges, self.ui.edges)
            self.display_image(contour_image, self.ui.contour1)
            self.display_image(final_image, self.ui.finalContour)

            self.final_contour = smoothed_contour
            self.contour_image = final_image

        except Exception as e:
            print(f"Error: {e}")

    def display_image(self, image, widget):
        scene = QGraphicsScene()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        q_image = QImage(
            image.data, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888
        )
        pixmap = QPixmap.fromImage(q_image)
        scene.addPixmap(pixmap)
        widget.setScene(scene)

    def smooth_contour(self, contour, window_size=5):
        smoothed_contour = []
        for i in range(len(contour)):
            x_sum = 0
            y_sum = 0
            count = 0
            for j in range(-window_size // 2, window_size // 2 + 1):
                index = (i + j) % len(contour)
                x_sum += contour[index][0][0]
                y_sum += contour[index][0][1]
                count += 1
            smoothed_contour.append([[x_sum // count, y_sum // count]])
        return np.array(smoothed_contour, dtype=np.int32)

    def save_output(self):
        if hasattr(self, 'final_contour'):
            save_path, _ = QFileDialog.getSaveFileName(self, "Save DXF", "", "DXF Files (*.dxf)")
            if save_path:
                with open(save_path, 'w') as f:
                    f.write('0\nSECTION\n2\nENTITIES\n0\nLWPOLYLINE\n8\n0\n70\n1\n')
                    for point in self.final_contour:
                        x, y = point[0]
                        f.write(f'10\n{x}\n20\n{-y}\n')  # Flip Y-axis
                    f.write('0\nENDSEC\n0\nEOF\n')
                print(f"DXF saved to {save_path}")
        else:
            print("No contour to save")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContourApp()
    window.show()
    sys.exit(app.exec())
