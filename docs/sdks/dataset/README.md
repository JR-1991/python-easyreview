# Dataset
(*dataset*)

### Available Operations

* [fetch_dataset_from_doi](#fetch_dataset_from_doi) - Fetches a dataset from a Dataverse installation and adds it to the database. This function will also check whether the given dataset is already present in the database and thus returns the entry. If not, a new one will be created and returned from this endpoint.

## fetch_dataset_from_doi

Fetches a dataset from a Dataverse installation and adds it to the database. This function will also check whether the given dataset is already present in the database and thus returns the entry. If not, a new one will be created and returned from this endpoint.

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
