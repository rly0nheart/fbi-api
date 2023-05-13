import requests


def get_api_response(url: str) -> dict:
    """
    Sends a GET request to the specified URL and returns the response as a dictionary.

    :param url: The URL to send the request to.

    :return: A dictionary containing the JSON response from the API.

    Raises:
        Exception: If there is an error with the request.
    """
    try:
        with requests.get(url) as response:
            data = response.json()
        return data
    except Exception as e:
        raise Exception(e)
