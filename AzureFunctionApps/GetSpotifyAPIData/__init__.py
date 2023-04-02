import logging
import azure.functions as func
import requests
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    token = req.params.get("token")
    artist_name = req.params.get("artist_name")
    limit = req.params.get("limit")

    try: 
        headers = {"Authorization": "Bearer " + token}
        url = "https://api.spotify.com/v1/search"
        query = f"?q={artist_name}&type=artist&limit={limit}"
        query_url = url + query 
        result = requests.get(query_url, headers=headers)
        json_result = json.loads(result.content)
    except:
        token = "token is not provided or is incorrect"

    return func.HttpResponse(str(json_result))

