#!/bin/python
import time

import pyaudio

# Choose your desired settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5


def record_sound():
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        if i % 10 == 0:
            print(".", end="", flush=True)
        data = stream.read(CHUNK)
        frames.append(data)

    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()

    return frames


def play_sound(frames):
    audio = pyaudio.PyAudio()

    # start Playing
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

    print("playing...")
    for frame in frames:
        stream.write(frame)
    print("finished playing")

    # stop Playing
    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    record = record_sound()
    play_sound(record)
