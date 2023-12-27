# Fields
(*fields*)

### Available Operations

* [get_field_by_id](#get_field_by_id) - Returns a field for a given field ID.
* [update_field](#update_field) - Updates a field for a given field ID.
* [partial_update_field](#partial_update_field) - Updates a field for a given field ID.

## get_field_by_id

Returns a field for a given field ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.fields.get_field_by_id(id='string')

if res.field is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFieldByIDResponse](../../models/operations/getfieldbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_field

Updates a field for a given field ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.fields.update_field(id='string', field=components.FieldInput(
    name='string',
    chat={
        'key': 'string',
    },
    value='string',
    history={
        'key': 'string',
    },
))

if res.field is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `field`                                                        | [components.FieldInput](../../models/components/fieldinput.md) | :heavy_check_mark:                                             | N/A                                                            |


### Response

**[operations.UpdateFieldResponse](../../models/operations/updatefieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_field

Updates a field for a given field ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.fields.partial_update_field(id='string', patched_field=components.PatchedField(
    chat={
        'key': 'string',
    },
    history={
        'key': 'string',
    },
))

if res.field is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `patched_field`                                                              | [Optional[components.PatchedField]](../../models/components/patchedfield.md) | :heavy_minus_sign:                                                           | N/A                                                                          |


### Response

**[operations.PartialUpdateFieldResponse](../../models/operations/partialupdatefieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
