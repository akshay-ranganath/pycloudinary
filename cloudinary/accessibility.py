import urllib
import logging
from cloudinary.http_client import HttpClient
from cloudinary.utils import json_encode

logger = logging.getLogger("Cloudinary")
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def fetch_alt_tags(
        cloud_name,
        api_key,
        api_secret,
        public_id,
        worker_url
):
    logger.debug(u"Cloud Name: {}, Worker URL: {}".format(cloud_name, worker_url))
    response = None

    body = {
        "cloudName": cloud_name,
        "publicId": public_id,
        "apiKey": api_key,
        "apiSecret": api_secret
    }
    client = HttpClient()
    response = client.post_json(worker_url, json_encode(body))
    return response


if __name__=="__main__":
    response = fetch_alt_tags(
        'alttextgenerator',
        '567644436894257',
        '0EWAGKIvQJd_U3VWXWVi5SHf0uE',
        'aqqcwtmphkpbqmqkix9x',
        'https://testfetch.cloudinary.workers.dev/'
    )

    print(response)
