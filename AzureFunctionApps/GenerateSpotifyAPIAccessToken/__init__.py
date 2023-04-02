import logging
import azure.functions as func
import base64
import requests
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    client_id = req.params.get("client_id")
    client_secret = req.params.get("client_secret")

    try: 
        auth_string = client_id + ":" + client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = requests.post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
    except:
        token = "client_id or client_secret not provided or incorrect"

    return func.HttpResponse(token)

