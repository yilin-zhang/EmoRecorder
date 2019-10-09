import sys, os, datetime, re
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtCore import pyqtSlot
from app_ui import *

from recorder import Recorder
from audio_device import AudioDevice

class RecorderApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # variables
        self.emotion_set = (
            'Passionate',
            'Cheerful',
            'Bittersweet',
            'Quirky',
            'Aggressive'
        )
        self.dataset_path = ''
        self.file_path = ''
        # other settings
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(False)
        self.timer = QtCore.QTimer()
        self._reset_time()
        self._set_device_box()
        # messages
        self.ui.recordButton.clicked.connect(self.start_recording)
        self.ui.stopButton.clicked.connect(self.stop_recording)
        self.ui.browseButton.clicked.connect(self.open_file_dialog)
        self.timer.timeout.connect(self.timer_event)
        self.ui.radioButtonEmotion1.clicked.connect(self.enable_record_button)
        self.ui.radioButtonEmotion2.clicked.connect(self.enable_record_button)
        self.ui.radioButtonEmotion3.clicked.connect(self.enable_record_button)
        self.ui.radioButtonEmotion4.clicked.connect(self.enable_record_button)
        self.ui.radioButtonEmotion5.clicked.connect(self.enable_record_button)

    def enable_record_button(self):
        self.ui.recordButton.setEnabled(True)

    def open_file_dialog(self):
        dname = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.dataset_path = dname
        self.ui.dirPath.setText(dname)

    def start_recording(self):
        name = self.ui.nameEdit.text()
        self.file_path = self._get_save_path(name)
        self.recording_file = Recorder().open(self.file_path, self._get_device_index())
        self.recording_file.start_recording()
        # update objects
        self.ui.promptLabel.setText('')
        self.ui.recordButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)
        self.timer.start(1000)

    def stop_recording(self):
        self.recording_file.stop_recording()
        self.recording_file.close()
        # clean up
        self.timer.stop()
        self._reset_time()
        self.ui.recordButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)
        self.ui.promptLabel.setText('Saved file to: ' + self.file_path)
        self.file_path = ''

    def timer_event(self):
        self.time = self.time.addSecs(1)
        self.ui.timeLabel.setText(self.time.toString('mm:ss'))
    
    def _set_device_box(self):
        # format: "idx - device name"
        devices = AudioDevice().list_devices()
        items = []
        for device in devices:
            index = device['index']
            name = device['name']
            item = str(index) + ' - ' + name
            items.append(item)
        self.ui.deviceBox.addItems(items)
    
    def _get_device_index(self):
        # return the number at the beginning as the index
        return int(re.match('\d+', self.ui.deviceBox.currentText()).group())

    def _reset_time(self):
        self.time = QtCore.QTime(0, 0, 0)
        self.ui.timeLabel.setText('00:00')

    def _get_emotion(self):
        if self.ui.radioButtonEmotion1.isChecked():
            emotion = self.emotion_set[0]
        elif self.ui.radioButtonEmotion2.isChecked():
            emotion = self.emotion_set[1]
        elif self.ui.radioButtonEmotion3.isChecked():
            emotion = self.emotion_set[2]
        elif self.ui.radioButtonEmotion4.isChecked():
            emotion = self.emotion_set[3]
        elif self.ui.radioButtonEmotion5.isChecked():
            emotion = self.emotion_set[4]
        return emotion

    def _get_instruemt(self):
        return self.ui.instrumentBox.currentText()

    def _get_save_path(self, name):
        emotion = self._get_emotion()
        instrument = self._get_instruemt()
        dir_path = os.path.join(self.dataset_path, emotion, instrument)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        filename = name + '-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.wav'
        file_path = os.path.join(dir_path, filename)
        return file_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = RecorderApp()
    w.show()
    sys.exit(app.exec_())