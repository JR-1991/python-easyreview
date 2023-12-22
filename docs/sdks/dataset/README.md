# Dataset
(*dataset*)

### Available Operations

* [fetch_dataset_from_doi](#fetch_dataset_from_doi)

## fetch_dataset_from_doi

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.dataset.fetch_dataset_from_doi(doi='string', site_url='string', api_token='string')

if res.review is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `doi`                                | *str*                                | :heavy_check_mark:                   | DOI of the dataset                   |
| `site_url`                           | *str*                                | :heavy_check_mark:                   | URL to the dataset                   |
| `api_token`                          | *Optional[str]*                      | :heavy_minus_sign:                   | API Token to access hidden datasets. |


### Response

**[operations.FetchDatasetFromDOIResponse](../../models/operations/fetchdatasetfromdoiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
