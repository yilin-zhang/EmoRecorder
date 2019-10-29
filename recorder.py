# -*- coding: utf-8 -*-
'''recorder.py
Provides WAV recording functionality via two approaches:
Blocking mode (record for a set duration):
>>> rec = Recorder(channels=2)
>>> with rec.open('blocking.wav', 'wb') as recfile:
...     recfile.record(duration=5.0)
Non-blocking mode (start and stop recording):
>>> rec = Recorder(channels=2)
>>> with rec.open('nonblocking.wav', 'wb') as recfile2:
...     recfile2.start_recording()
...     time.sleep(5.0)
...     recfile2.stop_recording()
'''
import pyaudio
import wave
import numpy as np
import math

class Recorder(object):
    '''A recorder class for recording audio to a WAV file.
    Records in mono by default.
    '''

    def __init__(self, channels=1, rate=44100, frames_per_buffer=1024):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer

    def open(self, fname, input_device_index=None, mode='wb'):
        return RecordingFile(fname, mode, self.channels, self.rate,
                            input_device_index, self.frames_per_buffer)

class RecordingFile(object):
    def __init__(self, fname, mode, channels, 
                rate, input_device_index, frames_per_buffer):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None
        self.input_device_index = input_device_index
        self._playback_stream = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def record(self, duration):
        # Use a stream with no callback function in blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        input_device_index = self.input_device_index,
                                        frames_per_buffer=self.frames_per_buffer)
        for _ in range(int(self.rate / self.frames_per_buffer * duration)):
            audio = self._stream.read(self.frames_per_buffer)
            self.wavefile.writeframes(audio)
        return None

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        input_device_index = self.input_device_index,
                                        frames_per_buffer=self.frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()

        self._playback_stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        output=True,
                                        frames_per_buffer=self.frames_per_buffer)
        self._playback_stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        self._playback_stream.stop_stream()
        return self
    
    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            # visualization
            self._visualize(in_data)
            # playback
            self._playback_stream.write(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile

    def _visualize(self, in_data):
        data = np.fromstring(in_data, dtype=np.int16)
        peak = np.max(np.abs(data)) * 2
        num = round(20 * math.log10(peak / 2**16))
        if num < -50:
            bars = ''
        elif num >= -18:
            bars = '#' * (50 - 18) + '*' * (18 + num)
        else:
            bars = '#' * (50 + num)
        print("%02d %s" % (num, bars))