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
    """
    A wrapper function that makes a call to the remote URL specified as worker_url and fetches the alt text tag.

    This function expects the response to be in the following JSON format:
    {
        "alt_text": "something"
    }

    It may have any other dictionary along with this value but, alt_text is the only mandatory value.

    :param cloud_name: Cloudinary Cloud name for the resource
    :param api_key: API Key to use for fetching the context metadata
    :param api_secret: API Key to use for fetching the context metadata
    :param public_id: The actual resource for which we need the alt_text information
    :param worker_url: The remote service that will make the Cloudinary API call and return the alt_text

    :return: A dictionary object that will return the alt-text value if it was defined for the resource
    """

    logger.debug(u"Cloud Name: {}, Worker URL: {}, Public ID: ".format(cloud_name, worker_url,public_id))

    body = {
        "cloudName": cloud_name,
        "publicId": public_id,
        "apiKey": api_key,
        "apiSecret": api_secret
    }
    client = HttpClient()
    response = client.post_json(worker_url, json_encode(body))
    return response
