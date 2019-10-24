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
        self.emotion_set_1 = (
            'Pleasure',
            'Joy',
            'Pride',
            'Amusement',
            'Interest',
        )
        self.emotion_set_2 = (
            'Anger',
            'Hate',
            'Contempt',
            'Disgust',
            'Fear',
        )
        self.emotion_set_3 = (
            'Disappointment',
            'Shame',
            'Regret',
            'Guilt',
            'Sadness',
        )
        self.emotion_set_4 = (
            'Compassion',
            'Relief',
            'Admiration',
            'Love',
            'Contentment',
        )
        self.dataset_path = ''
        self.file_path = ''
        self.name_confirmed = False
        self.emotion_selected = False
        self.is_recording = False
        # other settings
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(False)
        self.ui.editButton.setEnabled(False)
        self.timer = QtCore.QTimer()
        self._reset_time()
        self._set_device_box()
        # messages
        self.ui.recordButton.clicked.connect(self.start_recording)
        self.ui.stopButton.clicked.connect(self.stop_recording)
        self.ui.browseButton.clicked.connect(self.open_file_dialog)
        self.timer.timeout.connect(self.timer_event)
        self.ui.confirmButton.clicked.connect(self.confirm_name)
        self.ui.editButton.clicked.connect(self.edit_name)
        self.ui.radioButtonEmotion1.clicked.connect(self.select_emotion)
        self.ui.radioButtonEmotion2.clicked.connect(self.select_emotion)
        self.ui.radioButtonEmotion3.clicked.connect(self.select_emotion)
        self.ui.radioButtonEmotion4.clicked.connect(self.select_emotion)
        self.ui.radioButtonEmotion5.clicked.connect(self.select_emotion)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            if self.ui.recordButton.isEnabled():
                self.ui.recordButton.clicked.emit()
            elif self.ui.stopButton.isEnabled():
                self.ui.stopButton.clicked.emit()

    def select_emotion(self):
        self.emotion_selected = True
        self._update_button_status()
    
    def confirm_name(self):
        self.name_confirmed = True
        self._update_button_status()

    def edit_name(self):
        self.name_confirmed = False
        self._update_button_status()

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
        # update the buttons' status
        self.is_recording = True
        self._update_button_status()
        # clean up any text in promptLabel
        self.ui.promptLabel.setText('')
        # start counting
        self.timer.start(1000)

    def stop_recording(self):
        self.recording_file.stop_recording()
        self.recording_file.close()
        # clean up
        # update the buttons' status
        self.is_recording = False
        self._update_button_status()
        # reset the timer
        self.timer.stop()
        self._reset_time()
        # show the path
        self.ui.promptLabel.setText('Saved file to: ' + self.file_path)
        # reset the file path
        self.file_path = ''

    def timer_event(self):
        self.time = self.time.addSecs(1)
        self.ui.timeLabel.setText(self.time.toString('mm:ss'))
    
    def _update_button_status(self):
        # Update the buttons of name confirmation
        if self.name_confirmed:
            self.ui.editButton.setEnabled(True)
            self.ui.confirmButton.setEnabled(False)
            self.ui.nameEdit.setEnabled(False)
        else:
            self.ui.editButton.setEnabled(False)
            self.ui.confirmButton.setEnabled(True)
            self.ui.nameEdit.setEnabled(True)

        # Users can press record only after confirming the name
        # and selecting a emotion.
        if self.emotion_selected and self.name_confirmed:
            if self.is_recording:
                self.ui.recordButton.setEnabled(False)
                self.ui.stopButton.setEnabled(True)
            else:
                self.ui.recordButton.setEnabled(True)
                self.ui.stopButton.setEnabled(False)
        else:
            self.ui.recordButton.setEnabled(False)
            self.ui.stopButton.setEnabled(False)

        
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
            emotion = self.emotion_set_1[0]
        elif self.ui.radioButtonEmotion2.isChecked():
            emotion = self.emotion_set_1[1]
        elif self.ui.radioButtonEmotion3.isChecked():
            emotion = self.emotion_set_1[2]
        elif self.ui.radioButtonEmotion4.isChecked():
            emotion = self.emotion_set_1[3]
        elif self.ui.radioButtonEmotion5.isChecked():
            emotion = self.emotion_set_1[4]

        elif self.ui.radioButtonEmotion6.isChecked():
            emotion = self.emotion_set_2[0]
        elif self.ui.radioButtonEmotion7.isChecked():
            emotion = self.emotion_set_2[1]
        elif self.ui.radioButtonEmotion8.isChecked():
            emotion = self.emotion_set_2[2]
        elif self.ui.radioButtonEmotion9.isChecked():
            emotion = self.emotion_set_2[3]
        elif self.ui.radioButtonEmotion10.isChecked():
            emotion = self.emotion_set_2[4]

        elif self.ui.radioButtonEmotion11.isChecked():
            emotion = self.emotion_set_3[0]
        elif self.ui.radioButtonEmotion12.isChecked():
            emotion = self.emotion_set_3[1]
        elif self.ui.radioButtonEmotion13.isChecked():
            emotion = self.emotion_set_3[2]
        elif self.ui.radioButtonEmotion14.isChecked():
            emotion = self.emotion_set_3[3]
        elif self.ui.radioButtonEmotion15.isChecked():
            emotion = self.emotion_set_3[4]

        elif self.ui.radioButtonEmotion16.isChecked():
            emotion = self.emotion_set_4[0]
        elif self.ui.radioButtonEmotion17.isChecked():
            emotion = self.emotion_set_4[1]
        elif self.ui.radioButtonEmotion18.isChecked():
            emotion = self.emotion_set_4[2]
        elif self.ui.radioButtonEmotion19.isChecked():
            emotion = self.emotion_set_4[3]
        elif self.ui.radioButtonEmotion20.isChecked():
            emotion = self.emotion_set_4[4]

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