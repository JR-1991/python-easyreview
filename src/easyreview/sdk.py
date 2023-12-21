"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .dataset import Dataset
from .field import Field
from .reviewers import Reviewers
from .reviews import Reviews
from .sdkconfiguration import SDKConfiguration
from easyreview import utils
from easyreview.models import components
from typing import Callable, Dict, Union

class EasyReview:
    r"""EasyReview API: Backend used for the EasyReview app to manage reviews."""
    dataset: Dataset
    field: Field
    reviewers: Reviewers
    reviews: Reviews

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[components.Security,Callable[[], components.Security]] = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: Union[components.Security,Callable[[], components.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.dataset = Dataset(self.sdk_configuration)
        self.field = Field(self.sdk_configuration)
        self.reviewers = Reviewers(self.sdk_configuration)
        self.reviews = Reviews(self.sdk_configuration)
    