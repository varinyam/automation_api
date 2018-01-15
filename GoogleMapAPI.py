import requests
import webbrowser
import json


search_url="https://maps.googleapis.com/maps/api/place/textsearch/json"
detail_url="https://maps.googleapis.com/maps/api/place/details/json"
query=input("Enter the location")

def result():

    search_payload={"key":'AIzaSyBw3atM-GJeWvxkMqndafuhbO3KZpCgdTE',"query":query}
    search_req=requests.get(search_url,params=search_payload)
    search_json=search_req.json()
    print(search_json)

    place_id=search_json["results"][0]["place_id"]

    details_payload={"key":'AIzaSyBw3atM-GJeWvxkMqndafuhbO3KZpCgdTE',"placeid":place_id}
    detail_resp=requests.get(detail_url,params=details_payload)
    detail_json=detail_resp.json()

    url=detail_json["result"]["url"]
    webbrowser.open(url)

if __name__=='__main__':
    result()

