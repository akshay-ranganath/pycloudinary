import logging
from cloudinary.http_client import HttpClient
from cloudinary.utils import json_encode

import cloudinary

logger = logging.getLogger("Cloudinary")
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def fetch_alt_tags(
        public_id,
        remote_url
):
    """
    A wrapper function that makes a call to the remote URL specified as worker_url and fetches the alt text tag.

    This function expects the response to be in the following JSON format:
    {
        "alt_text": "something"
    }

    It may have any other dictionary along with this value but, alt_text is the only mandatory value.

    :param public_id: Object for which we require the alt-text
    :param remote_url: API endpoint that will be returning the alt-text information

    :return: JSON object that will include the alt-text if one is present
    """
    body = {
        "cloudName": cloudinary.config().cloud_name,
        "apiKey": cloudinary.config().api_key,
        "apiSecret": cloudinary.config().api_secret,
        "publicId": public_id
    }
    client = HttpClient()
    response = client.post_json(remote_url, json_encode(body))
    return response


