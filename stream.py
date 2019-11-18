import subprocess
import requests
import json
from config import Config

class ProcManager:
    def inactiveKiller(self, processes):  # # Delete inactive subprocess object (subrocess_object.poll() != None)
        if processes != None or processes > 0:
            for p in processes:
                if p.poll() != None:
                    processes.remove(p)
            return processes
        else:
            processes = [] # Prevent NoneType
            return processes
            
            
    def compareProcStream(self, processes, liveStreams):  # Def returns dict of stremas to start be recording
        if len(processes) == 0:
            return liveStreams  # No processes running thus all live streams can be recorder
        else:
            if len(liveStreams) > 0:  # 1 on more live streams
                for p in processes:
                    keys = tuple(liveStreams.keys())
                    for key in keys:
                        if p.name == key:
                            del liveStreams[key]
                            newStreams = liveStreams  # # Dict of live, but not recording now streams (just naming change)
                    return newStreams
            else:
                return dict()  # Zero live streams returns empty dict object


class Record():
    def startRecording(self, channelName, videoUrl):
        proc = subprocess.Popen(['youtube-dl', videoUrl], shell=False)
        proc.name = channelName
        return proc


class LiveStream(Config):
    liveStreams = {}  ### liveStreams variable is dict {channel_name : livestream_url,}
    for key, value in Config.channels.items():
        jason = json.loads(requests.get(value, Config.headers).text)
        if jason['pageInfo']['totalResults'] == 1:
            liveStreams.update({key: Config.baseUrl + jason['items'][0]['id']['videoId']})


class Main(ProcManager, Record, LiveStream):
    # def __init__(self, processes): # for scheduling main instead of main() must be called
    #     self.processes = processes

    def exec(self, processes):
        liveStreams = LiveStream()  # Get list of streams live
        manager = ProcManager()
        manager.inactiveKiller(processes)
        newStreams = manager.compareProcStream(manager.inactiveKiller(processes), liveStreams.liveStreams) # Dict of live, but not recording now streams
        lenghtStreams = len(newStreams)
        # if len(newStreams) != int():
        #     lenghtStreams = 0 # NoneType fix
        # else:
        #     lenghtStreams = len(newStreams)  # Create variable before value is assigned
        #
        if lenghtStreams > 0:
            for key, value in newStreams.items():
                rec = Record()
                processes.append(rec.startRecording(key, value))
            return processes
        else: # Zero new streams
            return list()
            
            
            