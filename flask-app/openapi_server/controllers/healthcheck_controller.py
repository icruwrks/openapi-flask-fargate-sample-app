import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.healthcheck200_response import Healthcheck200Response  # noqa: E501
from openapi_server import util


def healthcheck():  # noqa: E501
    """Health check

    Health check # noqa: E501


    :rtype: Union[Healthcheck200Response, Tuple[Healthcheck200Response, int], Tuple[Healthcheck200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
