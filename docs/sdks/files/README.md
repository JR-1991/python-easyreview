# Files
(*files*)

### Available Operations

* [add_file](#add_file) - Adds a new file to the database.
* [get_file_by_id](#get_file_by_id) - Returns a file for a given file ID.
* [get_files](#get_files) - Returns all files.

## add_file

Adds a new file to the database.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.FileInput(
    name='string',
    chat={
        'key': 'string',
    },
    review='7ab63896-cf8d-433f-b203-1872fb817ffe',
)

res = s.files.add_file(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.FileInput](../../models/components/fileinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.AddFileResponse](../../models/operations/addfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_file_by_id

Returns a file for a given file ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.files.get_file_by_id(id='string')

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

## get_files

Returns all files.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.files.get_files()

if res.files is not None:
    # handle response
    pass
```


### Response

**[operations.GetFilesResponse](../../models/operations/getfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
