# ERROR: Content warning -- check if YouTube account can access stream via browser
import requests
# import json
from datetime import datetime

class Config():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    authKeys = ['xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']

    baseUrl = 'https://www.youtube.com/watch?v='
    api = ['https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=',
           '&type=video&eventType=live&key=']
    authCheck = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC4QobU6STFB0P71PMvOGN5A&type=video&eventType=live&key='  # Var for check if auth key is valid

    channelId = {
        'Telewizja wPolsce' : 'UCPiu4CZlknkTworskK79CPg',
        'Rzeczpospolita TV' : 'UCpchzx2u5Ab8YASeJsR1WIw',
    }

    mainDownloadPath = r'./downloads'

    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')


class ChannelsAPI(Config):   # { name : api_link_to_channel_to_get_json_response }
    channels = {}
    for auth in Config.authKeys:
        if 'error' not in requests.get(Config.authCheck + auth, Config.headers).text:
            for name, id in Config.channelId.items():
                channels.update({name : Config.api[0] + id + Config.api[1] + auth})
            break
