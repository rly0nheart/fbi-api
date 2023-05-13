import requests
import re
import json

def __get_api_response(url: str) -> dict:
    """
    Sends a GET request to the specified URL and returns the response as a dictionary.

    :param url: The URL to send the request to.

    :return: A dictionary containing the JSON response from the API.

    Raises:
        Exception: If there is an error with the request.
    """
    try:
        with requests.get(url) as response:
            # JSON data
            if "json" in response.headers["Content-Type"]:
                data = response.json()

            # HTML Parsing for JSON data
            else:
                # FILTERING HTML TO EXTRACT JSON
                # Remove HTML tags and unwanted characters and some extra filters 
                cleaned_text=re.sub('<[^<]+?>|\\\\xa0|\\\\r\\\\n|\r\n', '',response.text)
                cleaned_text=re.sub("\\\\\\'",'Ø',cleaned_text)
                cleaned_text=re.sub('"','\\"',cleaned_text)
                
                # replace single quotes with double quotes
                # cleaned_text=re.sub(r"'([^']+)':", r'"\1":',cleaned_text,flags=re.DOTALL)
                # cleaned_text=re.sub(r":(.{0,4}?)'([^']+)'(.{0,4}?,)", r':\1"\2"\3',cleaned_text,flags=re.DOTALL)

                cleaned_text = re.sub('\'', '"',cleaned_text)
                #replace None with null
                cleaned_text = re.sub('None', 'null',cleaned_text)
                cleaned_text = re.sub("Ø",'\'',cleaned_text)
                # Convert cleaned text to JSON
                data = json.loads(cleaned_text)              
        return data
    except Exception as e:
        raise Exception(e)
