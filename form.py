# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1412, 1029)
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 1398, 1010))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.finalContour = QGraphicsView(self.horizontalLayoutWidget)
        self.finalContour.setObjectName(u"finalContour")
        self.finalContour.setMinimumSize(QSize(400, 400))
        self.finalContour.setSizeIncrement(QSize(10, 10))
        self.finalContour.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout.addWidget(self.finalContour, 1, 1, 1, 1)

        self.contour1 = QGraphicsView(self.horizontalLayoutWidget)
        self.contour1.setObjectName(u"contour1")
        self.contour1.setMinimumSize(QSize(400, 400))

        self.gridLayout.addWidget(self.contour1, 1, 0, 1, 1)

        self.edges = QGraphicsView(self.horizontalLayoutWidget)
        self.edges.setObjectName(u"edges")
        self.edges.setMinimumSize(QSize(400, 400))

        self.gridLayout.addWidget(self.edges, 0, 1, 1, 1)

        self.inputimage = QGraphicsView(self.horizontalLayoutWidget)
        self.inputimage.setObjectName(u"inputimage")
        self.inputimage.setMinimumSize(QSize(400, 400))

        self.gridLayout.addWidget(self.inputimage, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.filePath = QLineEdit(self.horizontalLayoutWidget)
        self.filePath.setObjectName(u"filePath")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePath.sizePolicy().hasHeightForWidth())
        self.filePath.setSizePolicy(sizePolicy)
        self.filePath.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_5.addWidget(self.filePath)

        self.browseImage = QPushButton(self.horizontalLayoutWidget)
        self.browseImage.setObjectName(u"browseImage")

        self.horizontalLayout_5.addWidget(self.browseImage)

        self.loadImage = QPushButton(self.horizontalLayoutWidget)
        self.loadImage.setObjectName(u"loadImage")

        self.horizontalLayout_5.addWidget(self.loadImage)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.blurKernelSize = QLineEdit(self.horizontalLayoutWidget)
        self.blurKernelSize.setObjectName(u"blurKernelSize")

        self.horizontalLayout_2.addWidget(self.blurKernelSize)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.blurSigma = QLineEdit(self.horizontalLayoutWidget)
        self.blurSigma.setObjectName(u"blurSigma")

        self.horizontalLayout_2.addWidget(self.blurSigma)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.cannyThreshold1 = QLineEdit(self.horizontalLayoutWidget)
        self.cannyThreshold1.setObjectName(u"cannyThreshold1")

        self.horizontalLayout_4.addWidget(self.cannyThreshold1)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.cannyThreshold2 = QLineEdit(self.horizontalLayoutWidget)
        self.cannyThreshold2.setObjectName(u"cannyThreshold2")

        self.horizontalLayout_4.addWidget(self.cannyThreshold2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.closing1Kernel = QLineEdit(self.horizontalLayoutWidget)
        self.closing1Kernel.setObjectName(u"closing1Kernel")

        self.horizontalLayout_3.addWidget(self.closing1Kernel)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.closing2Kernel = QLineEdit(self.horizontalLayoutWidget)
        self.closing2Kernel.setObjectName(u"closing2Kernel")

        self.horizontalLayout_3.addWidget(self.closing2Kernel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.smoothWindowSize = QLineEdit(self.horizontalLayoutWidget)
        self.smoothWindowSize.setObjectName(u"smoothWindowSize")

        self.horizontalLayout_7.addWidget(self.smoothWindowSize)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.preview = QPushButton(self.horizontalLayoutWidget)
        self.preview.setObjectName(u"preview")

        self.horizontalLayout_6.addWidget(self.preview)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.save = QPushButton(self.horizontalLayoutWidget)
        self.save.setObjectName(u"save")

        self.horizontalLayout_6.addWidget(self.save)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.browseImage.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.loadImage.setText(QCoreApplication.translate("Widget", u"Load Image", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Kernel Size:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Sigma:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Threshold 1:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Threshold 2:", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Kernel Size 1:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Kernel Size 2:", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Smoothing window:", None))
        self.preview.setText(QCoreApplication.translate("Widget", u"Preview", None))
        self.save.setText(QCoreApplication.translate("Widget", u"Save", None))
    # retranslateUi

