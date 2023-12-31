"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from easyreview import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedField:
    accepted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accepted') }, 'form': { 'field_name': 'accepted' }, 'multipart_form': { 'field_name': 'accepted' }})
    chat: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chat'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'chat', 'json': True }, 'multipart_form': { 'field_name': 'chat', 'json': True }})
    compound: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compound') }, 'form': { 'field_name': 'compound' }, 'multipart_form': { 'field_name': 'compound' }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    history: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('history'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'history', 'json': True }, 'multipart_form': { 'field_name': 'history', 'json': True }})
    metadatablock: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadatablock') }, 'form': { 'field_name': 'metadatablock' }, 'multipart_form': { 'field_name': 'metadatablock' }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'value' }, 'multipart_form': { 'field_name': 'value' }})
    

