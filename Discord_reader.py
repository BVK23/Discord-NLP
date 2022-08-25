from gettext import install



import requests
import json

def retrieve(channelid):
    headers={
    'authorization':'NjkzMTU0NjU3NDgwMDgxNjA5.GOnVxu.OC3diK9gQnJdJ8SkuEe7mt_h45yb2-m9QmVElA',
    
    }
    parame= {'limit':100}
    r= requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers,params=parame)
    print(r)
    #jsonn=json.loads(r.text)
    jsonn=r.json()
    j=1
    for value in jsonn:
        # if j<100:
        #     j+=1
        #     continue
        print(value,'\n')
        print(value['id'],'\n')
        # if value['timestamp'].split('T')[0] > '2022-04-20':
        #      print(value['content'],'\n')
       
retrieve(977862006818349076)


#'date':'Mon, 27 Jun 2022 13:51:33 GMT'