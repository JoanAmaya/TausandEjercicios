import abacusSoftware.__GUI_images__ as __GUI_images__

import pyAbacus as pa
from abacusSoftware.constants import __version__
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from abacusSoftware.__about__ import Ui_Dialog as Ui_Dialog_about

class AboutWindow(QtWidgets.QDialog, Ui_Dialog_about):
    def __init__(self, parent = None):
        super(AboutWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.setupUi(self)
        self.parent = parent

        image = QtGui.QPixmap(':/splash.png')
        image = image.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(image)

        tausand = '<a href="https://www.tausand.com/"> https://www.tausand.com </a>'
        pages =  '<a href="https://github.com/Tausand-dev/AbacusSoftware"> https://github.com/Tausand-dev/AbacusSoftware </a>'
        message = "Abacus Software is a suite of tools build to ensure your experience with Tausand's coincidence counters becomes simplified. \n\nSoftware Version: %s\nPyAbacus Version: %s\n\n"%(__version__, pa.__version__)
        self.message_label.setText(message)
        self.visit_label = QtWidgets.QLabel()
        self.github_label = QtWidgets.QLabel()
        self.pages_label = QtWidgets.QLabel()

        self.visit_label.setText("Visit us at: %s "%tausand)
        self.github_label.setText("More information on Abacus Software implementation can be found at: %s"%pages)
        self.verticalLayout.addWidget(self.visit_label)
        self.verticalLayout.addWidget(self.github_label)

        self.visit_label.linkActivated.connect(self.open_link)
        self.github_label.linkActivated.connect(self.open_link)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.verticalLayout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def open_link(self, link):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(link))


class AboutMeWindow(QtWidgets.QDialog, Ui_Dialog_about):
    def __init__(self, parent=None):
        super(AboutMeWindow, self).__init__(parent)
        title="About Me"
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.setupUi(self)
        self.setWindowTitle(title)
        self.parent = parent
        self.setFixedSize(480,400)
        self.label = QLabel(self)
        self.label.setGeometry(40,40,440,360)
        
        self.label.setText("A positive experience I had while programming occurred when I discovered the possibility of managing any electronic device from a computer."
                           "At a company called CIMA S.A.S, there was a device known as Wavetek, which our work group regarded as a relic due to its longevity, though it was expected to cease functioning at any moment."
                           "However, one day the chief engineer assigned another employee to create a Python program to control it, and he asked me to assist him in learning about the process."
                           "At that point, I thought it was an impossible task."
                           "Initially, the employee utilized a Raspberry Pi to establish a connection between the Wavetek and the computer."
                           "Subsequently, he utilized an old project with a graphical interface designed for similar devices."
                           "He then proceeded to create functions in a library I had never encountered before, called RPi.GPIO, which was specifically designed for Raspberry Pi controllers."
                           "Despite his confidence in the program, I remained skeptical."
                           "However, when he executed the program and modified the parameters of the AC current signal through the interface, setting it to 200 mA, I was surprised to see the parameters change on the device."
                           "There was still one remaining task: initiating the signal required pressing a giant button to generate the current."
                           "To my surprise, he pushed start button from the graphical interface, and the current began to flow."
                           "This experience altered my perspective; if a device manufactured in 1995 could be controlled from a computer, why we couldn't control other devices like a modern refrigerators or blenders?"
                           "With the right tools, why not control every aspect of life from a computer?")
        
        self.label.setWordWrap(True)
        self.label.adjustSize()
        self.label.setAlignment(QtCore.Qt.AlignJustify)
        for child in self.findChildren(QtWidgets.QLabel):
            if child.text() == "TextLabel":
                child.hide()
        
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.setGeometry(220, 360, 40, 30)


