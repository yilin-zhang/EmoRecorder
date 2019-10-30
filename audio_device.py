import pyaudio

class AudioDevice():
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.info = self.p.get_host_api_info_by_index(0)

    def list_devices(self):
        # [{id: 0, name: "abc"}, {id: 1, name: "def"}]
        device_list = []
        for i in range(0, self.info.get('deviceCount')):
            max_input_channels = (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels'))
            if max_input_channels > 0:
                index = i
                name = self.p.get_device_info_by_host_api_device_index(0, i).get('name')
                device_list.append({'index': index, 'name': name, 'channels': max_input_channels})
        return device_list