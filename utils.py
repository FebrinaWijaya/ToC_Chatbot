import os
import requests
 

GRAPH_URL = "https://graph.facebook.com/v2.6"
# your page access token
#ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN = "EAAaOfEoALZC0BAHgVj0iaXsr9jaRC1JagSWoSYyZByk3vK2ZCA6E0G6LBzCMcwnzgUnZAyyndlDvmYYqB7CvsxHL53DO1wSA4S7PH4zO2DEsL5fXZCQCHTCzZCWhYzW17rUXr2GN0Bwmiy6pD0OI5ZAOw4AFyFHbSLy1GPqYvZBpzS3PU7lSKpxF"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
