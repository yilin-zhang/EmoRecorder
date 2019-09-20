# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emotion-recorder.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 424)
        self.instrumentBox = QtWidgets.QComboBox(Dialog)
        self.instrumentBox.setGeometry(QtCore.QRect(150, 130, 104, 26))
        self.instrumentBox.setObjectName("instrumentBox")
        self.instrumentBox.addItem("")
        self.instrumentBox.addItem("")
        self.instrumentBox.addItem("")
        self.instrumentBox.addItem("")
        self.instrumentBox.addItem("")
        self.radioButtonEmotion1 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEmotion1.setGeometry(QtCore.QRect(110, 180, 100, 20))
        self.radioButtonEmotion1.setObjectName("radioButtonEmotion1")
        self.radioButtonEmotion2 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEmotion2.setGeometry(QtCore.QRect(230, 180, 100, 20))
        self.radioButtonEmotion2.setObjectName("radioButtonEmotion2")
        self.radioButtonEmotion3 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEmotion3.setGeometry(QtCore.QRect(40, 240, 100, 20))
        self.radioButtonEmotion3.setObjectName("radioButtonEmotion3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 100, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 280, 361, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.recordButton = QtWidgets.QPushButton(Dialog)
        self.recordButton.setGeometry(QtCore.QRect(140, 330, 113, 32))
        self.recordButton.setObjectName("recordButton")
        self.stopButton = QtWidgets.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(140, 370, 113, 32))
        self.stopButton.setObjectName("stopButton")
        self.timeLabel = QtWidgets.QLabel(Dialog)
        self.timeLabel.setGeometry(QtCore.QRect(180, 300, 51, 20))
        self.timeLabel.setObjectName("timeLabel")
        self.browseButton = QtWidgets.QPushButton(Dialog)
        self.browseButton.setGeometry(QtCore.QRect(140, 60, 141, 32))
        self.browseButton.setObjectName("browseButton")
        self.dirPath = QtWidgets.QLabel(Dialog)
        self.dirPath.setGeometry(QtCore.QRect(20, 30, 361, 16))
        self.dirPath.setObjectName("dirPath")
        self.radioButtonEmotion4 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEmotion4.setGeometry(QtCore.QRect(170, 240, 100, 20))
        self.radioButtonEmotion4.setObjectName("radioButtonEmotion4")
        self.radioButtonEmotion5 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEmotion5.setGeometry(QtCore.QRect(270, 240, 100, 20))
        self.radioButtonEmotion5.setObjectName("radioButtonEmotion5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.instrumentBox.setItemText(0, _translate("Dialog", "Piano"))
        self.instrumentBox.setItemText(1, _translate("Dialog", "Violin"))
        self.instrumentBox.setItemText(2, _translate("Dialog", "Cello"))
        self.instrumentBox.setItemText(3, _translate("Dialog", "Trumpet"))
        self.instrumentBox.setItemText(4, _translate("Dialog", "Saxophone"))
        self.radioButtonEmotion1.setText(_translate("Dialog", "Passionate"))
        self.radioButtonEmotion2.setText(_translate("Dialog", "Cheerful"))
        self.radioButtonEmotion3.setText(_translate("Dialog", "Bittersweet"))
        self.recordButton.setText(_translate("Dialog", "Record"))
        self.stopButton.setText(_translate("Dialog", "Stop"))
        self.timeLabel.setText(_translate("Dialog", "00:00"))
        self.browseButton.setText(_translate("Dialog", "Browse..."))
        self.dirPath.setText(_translate("Dialog", "Select a directory for saving dataset"))
        self.radioButtonEmotion4.setText(_translate("Dialog", "Quirky"))
        self.radioButtonEmotion5.setText(_translate("Dialog", "Aggressive"))

