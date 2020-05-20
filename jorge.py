import requests
import json


def talk():
    msg = input("Pergunte ao Jorge: ")
    url = 'http://api.brainshop.ai/get?bid=31054&key=Vz2K3JlDJ77Vnh5H&uid=[uid]&msg=' + msg

    querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":"Hello!"}

    headers = {
        'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
        'x-rapidapi-key': "1cdd86cb4amshbd682eb5d7ea0e4p1d58b5jsncdc3418e14c7"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    js = json.loads(response.text)
    
    print(js['cnt'])
    print('----------------------------------')
    talk()

talk()
