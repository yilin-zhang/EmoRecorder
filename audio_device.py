import pyaudio

class AudioDevice:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.info = p.get_host_api_info_by_index(0)

    def list_devices(self):
        # [{id: 0, name: "abc"}, {id: 1, name: "def"}]
        device_list = []
        for i in range(0, self.info.get('deviceCount')):
            if(self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                index = i
                name = self.p.get_device_info_by_host_api_device_index(0, i).get('name')
                device_list.append({'index': index, 'name': name})
        return device_list
    
    def get_device_index(self, device_name):
        pass        