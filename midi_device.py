import mido

class MidiDevice():
    '''
    message bytes:
    [on/off, note, velocity]
    [144/128, 0~127, 0~127]
    '''
    NOTE_ON = 144
    NOTE_OFF = 128

    def __init__(self):
        mido.set_backend('mido.backends.rtmidi')
        self.inport = None

    def open_device(self, device_name, callback):
        self.inport = mido.open_input(device_name)
        self.inport.callback = callback

    def list_devices(self):
        return mido.get_input_names()

class MidiPedal(MidiDevice):
    def __init__(self, start_note, end_note):
        super().__init__()
        self.start_note = start_note
        self.end_note = end_note
    
    def open_device(self, device_name, callback_start, callback_end):
        def inner_callback(msg):
            on_off, note, _ = msg.bytes()
            # uncomment the next line for testing
            # print(note)
            if note == self.start_note and on_off == MidiDevice.NOTE_OFF:
                callback_start()
            elif note == self.end_note and on_off == MidiDevice.NOTE_ON:
                callback_end()
        super().open_device(device_name, inner_callback)