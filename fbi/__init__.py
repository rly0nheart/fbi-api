from typing import Union, Literal
from fbi.connection import get_api_response


def wanted(person_classification: Union[Literal['Main'], Literal['Accomplice'], Literal['Victim']] = None,
           page_size: int = 20, page: int = 1, sort_order: Union[Literal['asc'], Literal['desc']] = None) -> dict:
    """
    Get listing of wanted people
    :param person_classification: person classification
    :param page_size: number of items to return
    :param page: page of result listing
    :param sort_order: result sort order
    :return: a list of result dictionaries
    """
    if person_classification is None:
        person_classification = ""
    else:
        person_classification = f"&person_classification={person_classification}"

    if sort_order is None:
        sort_order = ""
    else:
        sort_order = f"&sort_order={sort_order}"

    response = get_api_response(f"https://api.fbi.gov/@wanted?pageSize={page_size}&page={page}{person_classification}")
    return response['items']


def wanted_person(person_id: str) -> dict:
    """
    Retrieve information on wanted person
    :param person_id: id of wanted person
    :return: a dictionary of person's information
    """
    return get_api_response(f"https://api.fbi.gov/@wanted-person/{person_id}")


def art_crimes(page_size: int = 20, page: int = 1, sort_order: Union[Literal['asc'], Literal['desc'], None] = None,
               reference_number: Union[int, str] = None) -> dict:
    """
    Get listing of national art theft
    :param page_size: number of items to return
    :param page: page of result listing
    :param sort_order: result sort order
    :param reference_number: art crime reference number
    :return: a list of result dictionaries
    """
    if reference_number is None:
        reference_number = ""
    else:
        reference_number = f"&referenceNumber={reference_number}"

    if sort_order is None:
        sort_order = ""
    else:
        sort_order = f"&sort_order={sort_order}"

    response = get_api_response(f"https://api.fbi.gov/@artcrimes?pageSize={page_size}&page={page}"
                                f"{sort_order}{reference_number}")
    return response['items']


def art_crime(crime_id: str) -> dict:
    """
    Retrieve information on an art crime
    :param crime_id: id of an art crime
    :return: dictionary of an art crime's information
    """
    return get_api_response(f"https://api.fbi.gov/@artcrimes/{crime_id}")
