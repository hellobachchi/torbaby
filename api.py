import requests
from requests.structures import CaseInsensitiveDict 
import json 

from torrentool.api import Torrent
def login():
    url = "https://my.torrentcheap.com/api/auth/login"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = """
    {
        "username": "shabeer",
        "password": "5QrklTPiGGmStd93xaWg08Mljfo5M9fWLcJ/qvpzQ0pimUly64PoM/W64vOmxwuKsMB3jj0KlV2dTu6y2LRMTj4Lrk4/J7iekZzV7DAy2gNdZNqZSOEVIuZimi/FfCID4HwJscjt8K8/ediuwaOr7YZx9+y/JzjTVbOA/ndbYfw="
    }
    """


    resp = requests.post(url, headers=headers, data=data)


    credentials  = json.loads(resp.text)
    return credentials
 
def send_mag_link(torlink): 
    
    url = "https://my.torrentcheap.com/api/torrent/downloadMagnetTorrent"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzaGFiZWVyIiwiaXNzIjoiaHR0cDovL3RvcnJlbnRjaGVhcC5jb20iLCJleHAiOjE2NzExMDIwMDUsImp0aSI6ImJkZTA0OGQ2LTQ4ZjktNDE3My1hMTJhLTgwMzVhMThlMTU3MyJ9.FXEIj-x-DpXSqiOZ8i_SmTtpipFBv0mt-JJ5x2OPSSs2JFJ6aPW85O_BuxOi5LWj8yTGWSoh3UqRN1dSaikKdw"
    headers["Content-Type"] = "application/json"

    data = '{"magnet": "'+torlink+'"}'
    resp = requests.post(url, headers=headers, data=data)

    return resp.status_code 

def list_movies():
    url = "https://my.torrentcheap.com/api/torrent/getPagedUserTorrents"


    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzaGFiZWVyIiwiaXNzIjoiaHR0cDovL3RvcnJlbnRjaGVhcC5jb20iLCJleHAiOjE2NzExMDIwMDUsImp0aSI6ImJkZTA0OGQ2LTQ4ZjktNDE3My1hMTJhLTgwMzVhMThlMTU3MyJ9.FXEIj-x-DpXSqiOZ8i_SmTtpipFBv0mt-JJ5x2OPSSs2JFJ6aPW85O_BuxOi5LWj8yTGWSoh3UqRN1dSaikKdw"
    headers["Content-Type"] = "application/json"

    data = """
    {
        "page": 1,
        "rows": 100
    }
    """


    resp = requests.post(url, headers=headers, data=data)
    return json.loads(resp.text)
    
 
def torrent(myfile):

    if myfile['file_size'] > 2000000:
        return("This file is too large Buddy!")
    else:
        with open('torrents/'+myfile['file_id'], 'wb') as f:
            myfile.download(out=f)
        try:
            torrent = Torrent.from_file('torrents/'+myfile['file_id'])
            send_mag_link(torrent.magnet_link) 
            return (torrent.magnet_link)
        except:
            return(
                "NOPE Buddy! This is not a torrent file or It has been courrpted!") 
def gen_dow_link(hash): 
    url = "https://my.torrentcheap.com/api/torrent/initiateTorrentZipDownload"


    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzaGFiZWVyIiwiaXNzIjoiaHR0cDovL3RvcnJlbnRjaGVhcC5jb20iLCJleHAiOjE2NzExMDIwMDUsImp0aSI6ImJkZTA0OGQ2LTQ4ZjktNDE3My1hMTJhLTgwMzVhMThlMTU3MyJ9.FXEIj-x-DpXSqiOZ8i_SmTtpipFBv0mt-JJ5x2OPSSs2JFJ6aPW85O_BuxOi5LWj8yTGWSoh3UqRN1dSaikKdw"
    headers["Content-Type"] = "application/json"

    data = "{\"torrentHash\": \""+hash+"\"} "
    resp = requests.post(url, headers=headers, data=data)
    return json.loads(resp.text)['result']['downloadLink']
if __name__=='__main__': 
    gen_dow_link('9455c66293f7d0cfbcd2c6fe8410602373014a08')
