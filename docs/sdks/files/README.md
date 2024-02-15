# Files
(*files*)

### Available Operations

* [get_file_by_id](#get_file_by_id) - Returns a file for a given file ID.
* [update_file](#update_file) - Updates a file for a given file ID.
* [partial_update_file](#partial_update_file) - Updates a file for a given file ID.

## get_file_by_id

Returns a file for a given file ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.files.get_file_by_id(id='<value>')

if res.file is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFileByIDResponse](../../models/operations/getfilebyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_file

Updates a file for a given file ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.files.update_file(id='<value>', file=components.FileInput(
    name='<value>',
    review='9923feda-142e-468a-afba-01ad05b1c7dc',
))

if res.file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `file`                                                       | [components.FileInput](../../models/components/fileinput.md) | :heavy_check_mark:                                           | N/A                                                          |


### Response

**[operations.UpdateFileResponse](../../models/operations/updatefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_file

Updates a file for a given file ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.files.partial_update_file(id='<value>', patched_file=components.PatchedFile())

if res.file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `patched_file`                                                             | [Optional[components.PatchedFile]](../../models/components/patchedfile.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.PartialUpdateFileResponse](../../models/operations/partialupdatefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
