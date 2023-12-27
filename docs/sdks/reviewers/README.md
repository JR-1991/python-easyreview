# Reviewers
(*reviewers*)

### Available Operations

* [get_reviewers](#get_reviewers) - Returns all reviewers
* [add_reviewer](#add_reviewer) - Adds a new reviewer to the database.
* [get_reviewer_by_id](#get_reviewer_by_id) - Returns a reviewer for a given reviewer ID.
* [update_reviewer](#update_reviewer) - Updates a reviewer for a given reviewer ID.
* [partial_update_reviewer](#partial_update_reviewer) - Partially updates a reviewer for a given reviewer ID.
* [delete_reviewer](#delete_reviewer) - Deletes a reviewer from the database.

## get_reviewers

Returns all reviewers

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviewers.get_reviewers()

if res.reviewers is not None:
    # handle response
    pass
```


### Response

**[operations.GetReviewersResponse](../../models/operations/getreviewersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_reviewer

Adds a new reviewer to the database.

### Example Usage

```python
import easyreview
from easyreview.models import components

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.ReviewerInput(
    username='Myriam_Batz70',
    first_name='Raphaelle',
    last_name='Grant',
    email='Tremaine38@gmail.com',
)

res = s.reviewers.add_reviewer(req)

if res.reviewer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.ReviewerInput](../../models/components/reviewerinput.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.AddReviewerResponse](../../models/operations/addreviewerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_reviewer_by_id

Returns a reviewer for a given reviewer ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviewers.get_reviewer_by_id(id='string')

if res.reviewer is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetReviewerByIDResponse](../../models/operations/getreviewerbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_reviewer

Updates a reviewer for a given reviewer ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviewers.update_reviewer(id='string', reviewer=components.ReviewerInput(
    username='Oran.Bergnaum91',
    first_name='Ressie',
    last_name='Langosh',
    email='Tomas_Dicki@gmail.com',
))

if res.reviewer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `reviewer`                                                           | [components.ReviewerInput](../../models/components/reviewerinput.md) | :heavy_check_mark:                                                   | N/A                                                                  |


### Response

**[operations.UpdateReviewerResponse](../../models/operations/updatereviewerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_reviewer

Partially updates a reviewer for a given reviewer ID.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviewers.partial_update_reviewer(id='string', patched_reviewer=components.PatchedReviewer())

if res.reviewer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `patched_reviewer`                                                                 | [Optional[components.PatchedReviewer]](../../models/components/patchedreviewer.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |


### Response

**[operations.PartialUpdateReviewerResponse](../../models/operations/partialupdatereviewerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_reviewer

Deletes a reviewer from the database.

### Example Usage

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.reviewers.delete_reviewer(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteReviewerResponse](../../models/operations/deletereviewerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
