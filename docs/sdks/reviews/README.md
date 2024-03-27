# Reviews
(*reviews*)

### Available Operations

* [get_reviews](#get_reviews) - Returns all reviews
* [get_files_by_review_id](#get_files_by_review_id) - Returns all files for a given review ID.
* [get_field_count](#get_field_count) - Returns the number of fields for a given review ID.
* [get_review_by_id](#get_review_by_id) - Returns a review for a given review ID.
* [update_review](#update_review) - Updates a review for a given review ID.
* [partial_update_review](#partial_update_review) - Partially updates a review for a given review ID.
* [delete_review](#delete_review) - Deletes a review from the database.
* [get_reviews_by_dataset_doi](#get_reviews_by_dataset_doi) - Returns all reviews for a given dataset DOI.
* [fetch_dataset_from_doi](#fetch_dataset_from_doi) - Fetches a dataset from a Dataverse installation and adds it to the database. This function will also check whether the given dataset is already present in the database and thus returns the entry. If not, a new one will be created and returned from this endpoint.
* [get_reviews_by_reviewer](#get_reviews_by_reviewer) - Returns all reviews for a given reviewer ID.

## get_reviews

Returns all reviews

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.get_reviews()

if res.reviews is not None:
    # handle response
    pass

```


### Response

**[operations.GetReviewsResponse](../../models/operations/getreviewsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_files_by_review_id

Returns all files for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.get_files_by_review_id(id='<value>')

if res.files is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFilesByReviewIDResponse](../../models/operations/getfilesbyreviewidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_field_count

Returns the number of fields for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.get_field_count(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFieldCountResponse](../../models/operations/getfieldcountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_review_by_id

Returns a review for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.get_review_by_id(id='<value>')

if res.review is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetReviewByIDResponse](../../models/operations/getreviewbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_review

Updates a review for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.update_review(id='<value>', review=components.ReviewInput(
    revision=229231,
))

if res.review is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `review`                                                         | [components.ReviewInput](../../models/components/reviewinput.md) | :heavy_check_mark:                                               | N/A                                                              |


### Response

**[operations.UpdateReviewResponse](../../models/operations/updatereviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_review

Partially updates a review for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.partial_update_review(id='<value>', patched_review=components.PatchedReview())

if res.review is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `patched_review`                                                               | [Optional[components.PatchedReview]](../../models/components/patchedreview.md) | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.PartialUpdateReviewResponse](../../models/operations/partialupdatereviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_review

Deletes a review from the database.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.delete_review(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteReviewResponse](../../models/operations/deletereviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_reviews_by_dataset_doi

Returns all reviews for a given dataset DOI.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.get_reviews_by_dataset_doi(doi='<value>')

if res.review is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `doi`              | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetReviewsByDatasetDOIResponse](../../models/operations/getreviewsbydatasetdoiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## fetch_dataset_from_doi

Fetches a dataset from a Dataverse installation and adds it to the database. This function will also check whether the given dataset is already present in the database and thus returns the entry. If not, a new one will be created and returned from this endpoint.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.fetch_dataset_from_doi(doi='<value>', site_url='<value>', api_token='<value>')

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

## get_reviews_by_reviewer

Returns all reviews for a given reviewer ID.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviews.get_reviews_by_reviewer(id='<value>')

if res.reviews is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetReviewsByReviewerResponse](../../models/operations/getreviewsbyreviewerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
