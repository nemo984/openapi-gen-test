import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_pet import NewPet  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server import util


def add_pet(new_pet):  # noqa: E501
    """add_pet

    Creates a new pet in the store. Duplicates are allowed # noqa: E501

    :param new_pet: Pet to add to the store
    :type new_pet: dict | bytes

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_pet = NewPet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pet(id):  # noqa: E501
    """delete_pet

    deletes a single pet based on the ID supplied # noqa: E501

    :param id: ID of pet to delete
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_pet_by_id(id):  # noqa: E501
    """find_pet_by_id

    Returns a user based on a single ID, if the user does not have access to the pet # noqa: E501

    :param id: ID of pet to fetch
    :type id: int

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_pets(tags=None, limit=None):  # noqa: E501
    """find_pets

    Returns all pets from the system that the user has access to Nam sed condimentum est. Maecenas tempor sagittis sapien, nec rhoncus sem sagittis sit amet. Aenean at gravida augue, ac iaculis sem. Curabitur odio lorem, ornare eget elementum nec, cursus id lectus. Duis mi turpis, pulvinar ac eros ac, tincidunt varius justo. In hac habitasse platea dictumst. Integer at adipiscing ante, a sagittis ligula. Aenean pharetra tempor ante molestie imperdiet. Vivamus id aliquam diam. Cras quis velit non tortor eleifend sagittis. Praesent at enim pharetra urna volutpat venenatis eget eget mauris. In eleifend fermentum facilisis. Praesent enim enim, gravida ac sodales sed, placerat id erat. Suspendisse lacus dolor, consectetur non augue vel, vehicula interdum libero. Morbi euismod sagittis libero sed lacinia.  Sed tempus felis lobortis leo pulvinar rutrum. Nam mattis velit nisl, eu condimentum ligula luctus nec. Phasellus semper velit eget aliquet faucibus. In a mattis elit. Phasellus vel urna viverra, condimentum lorem id, rhoncus nibh. Ut pellentesque posuere elementum. Sed a varius odio. Morbi rhoncus ligula libero, vel eleifend nunc tristique vitae. Fusce et sem dui. Aenean nec scelerisque tortor. Fusce malesuada accumsan magna vel tempus. Quisque mollis felis eu dolor tristique, sit amet auctor felis gravida. Sed libero lorem, molestie sed nisl in, accumsan tempor nisi. Fusce sollicitudin massa ut lacinia mattis. Sed vel eleifend lorem. Pellentesque vitae felis pretium, pulvinar elit eu, euismod sapien.  # noqa: E501

    :param tags: tags to filter by
    :type tags: List[str]
    :param limit: maximum number of results to return
    :type limit: int

    :rtype: Union[List[Pet], Tuple[List[Pet], int], Tuple[List[Pet], int, Dict[str, str]]
    """
    return 'do some magic!'
