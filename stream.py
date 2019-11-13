import subprocess
import requests
import json
from config import Config

class LiveStream(Config):
    ### liveStreams variable is dict {channel_name : livestream_url,}
    liveStreams = {}
    for key, value in Config.channels.items():
        jason = json.loads(requests.get(value, Config.headers).text)
        if jason['pageInfo']['totalResults'] == 1:
            liveStreams.update({key : Config.baseUrl + jason['items'][0]['id']['videoId']})

class Record():
    def __init__(self, channelName, videoUrl):
        self.channelName = channelName
        self.videoUrl = videoUrl

    def startRecording(self):
        proc = subprocess.Popen(['youtube-dl', self.videoUrl], shell=False)
        proc.name = self.channelName
        return proc



    # def startRecording(self):
    #     processes = []
    #     for key, value in self.liveStreams.items():
    #         videoUrl = self.baseUrl + value['items'][0]['id']['videoId']
    #         proc = subprocess.Popen(['youtube-dl', videoUrl], shell=False)
    #         ### Set name to each process
    #         proc.name = key
    #         processes.append(proc)
    #     return processes







