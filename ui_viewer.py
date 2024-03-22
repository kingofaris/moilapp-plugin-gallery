# Form implementation generated from reading ui file '.\plugins\moilapp-plugin-presentation\ui_viewer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Viewer(object):
    def setupUi(self, Viewer):
        Viewer.setObjectName("Viewer")
        Viewer.resize(1102, 844)
        self.verticalLayout = QtWidgets.QVBoxLayout(Viewer)
        self.verticalLayout.setContentsMargins(0, 11, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=Viewer)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.backButton.setMinimumSize(QtCore.QSize(0, 0))
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.moildevButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.moildevButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.moildevButton.setObjectName("moildevButton")
        self.horizontalLayout.addWidget(self.moildevButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.viewerZoomSlider = QtWidgets.QSlider(parent=self.frame_3)
        self.viewerZoomSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.viewerZoomSlider.setObjectName("viewerZoomSlider")
        self.horizontalLayout.addWidget(self.viewerZoomSlider)
        spacerItem1 = QtWidgets.QSpacerItem(60, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.compareViewButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.compareViewButton.setMinimumSize(QtCore.QSize(200, 0))
        self.compareViewButton.setObjectName("compareViewButton")
        self.horizontalLayout.addWidget(self.compareViewButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.navButtonsFrame = QtWidgets.QFrame(parent=Viewer)
        self.navButtonsFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.navButtonsFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.navButtonsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.navButtonsFrame.setObjectName("navButtonsFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.navButtonsFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.prevButton = QtWidgets.QPushButton(parent=self.navButtonsFrame)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout_3.addWidget(self.prevButton)
        self.nextButton = QtWidgets.QPushButton(parent=self.navButtonsFrame)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_3.addWidget(self.nextButton)
        self.verticalLayout.addWidget(self.navButtonsFrame)
        self.moildevFrame = QtWidgets.QFrame(parent=Viewer)
        self.moildevFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.moildevFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.moildevFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.moildevFrame.setObjectName("moildevFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.moildevFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.moildevButtonsFrame = QtWidgets.QFrame(parent=self.moildevFrame)
        self.moildevButtonsFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.moildevButtonsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.moildevButtonsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.moildevButtonsFrame.setObjectName("moildevButtonsFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.moildevButtonsFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.recenterButton = QtWidgets.QPushButton(parent=self.moildevButtonsFrame)
        self.recenterButton.setObjectName("recenterButton")
        self.horizontalLayout_2.addWidget(self.recenterButton)
        self.panoramaButton = QtWidgets.QPushButton(parent=self.moildevButtonsFrame)
        self.panoramaButton.setObjectName("panoramaButton")
        self.horizontalLayout_2.addWidget(self.panoramaButton)
        self.anypointButton = QtWidgets.QPushButton(parent=self.moildevButtonsFrame)
        self.anypointButton.setObjectName("anypointButton")
        self.horizontalLayout_2.addWidget(self.anypointButton)
        self.verticalLayout_2.addWidget(self.moildevButtonsFrame)
        self.radioButtonsFrame = QtWidgets.QFrame(parent=self.moildevFrame)
        self.radioButtonsFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.radioButtonsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.radioButtonsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.radioButtonsFrame.setObjectName("radioButtonsFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.radioButtonsFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.recenterMode1 = QtWidgets.QRadioButton(parent=self.radioButtonsFrame)
        self.recenterMode1.setObjectName("recenterMode1")
        self.recenterGroup = QtWidgets.QButtonGroup(Viewer)
        self.recenterGroup.setObjectName("recenterGroup")
        self.recenterGroup.addButton(self.recenterMode1)
        self.horizontalLayout_4.addWidget(self.recenterMode1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.recenterMode2 = QtWidgets.QRadioButton(parent=self.radioButtonsFrame)
        self.recenterMode2.setObjectName("recenterMode2")
        self.recenterGroup.addButton(self.recenterMode2)
        self.horizontalLayout_4.addWidget(self.recenterMode2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.panoramaCar = QtWidgets.QRadioButton(parent=self.radioButtonsFrame)
        self.panoramaCar.setChecked(True)
        self.panoramaCar.setObjectName("panoramaCar")
        self.panoramaGroup = QtWidgets.QButtonGroup(Viewer)
        self.panoramaGroup.setObjectName("panoramaGroup")
        self.panoramaGroup.addButton(self.panoramaCar)
        self.horizontalLayout_4.addWidget(self.panoramaCar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.panoramaTube = QtWidgets.QRadioButton(parent=self.radioButtonsFrame)
        self.panoramaTube.setObjectName("panoramaTube")
        self.panoramaGroup.addButton(self.panoramaTube)
        self.horizontalLayout_4.addWidget(self.panoramaTube, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.anypointMode1 = QtWidgets.QRadioButton(parent=self.radioButtonsFrame)
        self.anypointMode1.setChecked(True)
        self.anypointMode1.setObjectName("anypointMode1")
        self.anypointGroup = QtWidgets.QButtonGroup(Viewer)
        self.anypointGroup.setObjectName("anypointGroup")
        self.anypointGroup.addButton(self.anypointMode1)
        self.horizontalLayout_4.addWidget(self.anypointMode1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.anypointMode2 = QtWidgets.QRadioButton(parent=self.radioButtonsFrame)
        self.anypointMode2.setObjectName("anypointMode2")
        self.anypointGroup.addButton(self.anypointMode2)
        self.horizontalLayout_4.addWidget(self.anypointMode2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.radioButtonsFrame)
        self.parameterMoildevFrame = QtWidgets.QFrame(parent=self.moildevFrame)
        self.parameterMoildevFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.parameterMoildevFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.parameterMoildevFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.parameterMoildevFrame.setObjectName("parameterMoildevFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.parameterMoildevFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.parameterMoildevFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(parent=self.parameterMoildevFrame)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.label_3 = QtWidgets.QLabel(parent=self.parameterMoildevFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.parameterMoildevFrame)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_5.addWidget(self.spinBox_2)
        self.label_4 = QtWidgets.QLabel(parent=self.parameterMoildevFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.parameterMoildevFrame)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_5.addWidget(self.spinBox_3)
        self.label_5 = QtWidgets.QLabel(parent=self.parameterMoildevFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.parameterMoildevFrame)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_5.addWidget(self.spinBox_4)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.parameterMoildevFrame)
        self.verticalLayout.addWidget(self.moildevFrame)
        self.frame_2 = QtWidgets.QFrame(parent=Viewer)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.imageLabel = QtWidgets.QLabel(parent=self.frame_2)
        self.imageLabel.setText("")
        self.imageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout.addWidget(self.imageLabel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Viewer)
        QtCore.QMetaObject.connectSlotsByName(Viewer)

    def retranslateUi(self, Viewer):
        _translate = QtCore.QCoreApplication.translate
        Viewer.setWindowTitle(_translate("Viewer", "Viewer"))
        self.backButton.setText(_translate("Viewer", "Back"))
        self.moildevButton.setText(_translate("Viewer", "Moildev Config"))
        self.label.setText(_translate("Viewer", "Zoom:"))
        self.compareViewButton.setText(_translate("Viewer", "Compare View"))
        self.prevButton.setText(_translate("Viewer", "Previous"))
        self.nextButton.setText(_translate("Viewer", "Next"))
        self.recenterButton.setText(_translate("Viewer", "Recenter"))
        self.panoramaButton.setText(_translate("Viewer", "Panorama"))
        self.anypointButton.setText(_translate("Viewer", "Anypoint"))
        self.recenterMode1.setText(_translate("Viewer", "Mode 1"))
        self.recenterMode2.setText(_translate("Viewer", "Mode 2"))
        self.panoramaCar.setText(_translate("Viewer", "Car"))
        self.panoramaTube.setText(_translate("Viewer", "Tube"))
        self.anypointMode1.setText(_translate("Viewer", "Mode 1"))
        self.anypointMode2.setText(_translate("Viewer", "Mode 2"))
        self.label_2.setText(_translate("Viewer", "Alpha"))
        self.label_3.setText(_translate("Viewer", "Beta"))
        self.label_4.setText(_translate("Viewer", "Gamma"))
        self.label_5.setText(_translate("Viewer", "Rho"))
