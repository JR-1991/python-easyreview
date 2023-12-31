"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import file as components_file
from ...models.components import file_input as components_file_input
from typing import Optional


@dataclasses.dataclass
class UpdateFileRequest:
    file: components_file_input.FileInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class UpdateFileResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    file: Optional[components_file.File] = dataclasses.field(default=None)
    

