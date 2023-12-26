# Review
(*review*)

### Available Operations

* [add_review](#add_review) - Adds a new review to the database.
* [get_review_by_id](#get_review_by_id) - Returns a review for a given review ID.
* [update_review](#update_review) - Updates a review for a given review ID.
* [delete_review](#delete_review) - Deletes a review from the database.
* [get_files_by_review_id](#get_files_by_review_id) - Returns all files for a given review ID.
* [get_field_count](#get_field_count) - Returns the number of fields for a given review ID.
* [get_reviews_by_dataset_doi](#get_reviews_by_dataset_doi) - Returns all reviews for a given dataset DOI.
* [get_reviews](#get_reviews) - Returns all reviews.
* [get_reviews_by_reviewer](#get_reviews_by_reviewer) - Returns all reviews for a given reviewer ID.

## add_review

Adds a new review to the database.

### Example Usage

```python
import dateutil.parser
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.ReviewInput(
    revision=109209,
)

res = s.review.add_review(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.ReviewInput](../../models/components/reviewinput.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.AddReviewResponse](../../models/operations/addreviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_review_by_id

Returns a review for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.get_review_by_id(id='string')

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
import dateutil.parser
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.update_review(id='string', review=components.ReviewInput(
    revision=229231,
))

if res.status_code == 200:
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

## delete_review

Deletes a review from the database.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.delete_review(id='string')

if res.status_code == 200:
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

## get_files_by_review_id

Returns all files for a given review ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.get_files_by_review_id(id='string')

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
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.get_field_count(id='string')

if res.status_code == 200:
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

## get_reviews_by_dataset_doi

Returns all reviews for a given dataset DOI.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.get_reviews_by_dataset_doi(doi='string')

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

## get_reviews

Returns all reviews.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.get_reviews()

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

## get_reviews_by_reviewer

Returns all reviews for a given reviewer ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.review.get_reviews_by_reviewer(reviewerid='string')

if res.reviews is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `reviewerid`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetReviewsByReviewerResponse](../../models/operations/getreviewsbyreviewerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
