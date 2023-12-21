# Field
(*field*)

### Available Operations

* [get_field_by_id](#get_field_by_id)
* [update_field](#update_field)

## get_field_by_id

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.field.get_field_by_id(id='string')

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

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.field.update_field(id='string', field=components.FieldInput(
    name='string',
    chat={
        'key': 'string',
    },
    value='string',
    history={
        'key': 'string',
    },
))

if res.status_code == 200:
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
