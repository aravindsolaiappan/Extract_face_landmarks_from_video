import os
import subprocess

class FFMPEGFrames:
    def __init__(self, output):
        self.output = output

    def extract_frames(self, input, fps):
        output = input.split('/')[-1].split('.')[0]

        if not os.path.exists(self.output + output):
            os.makedirs(self.output + output)

        query = "ffmpeg -i " + input + " -vf fps=" + str(fps) + " " + self.output + output + "/output%d.png"
        response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
        s = str(response).encode('utf-8')
