# Reviewers
(*reviewers*)

### Available Operations

* [get_reviewer_by_id](#get_reviewer_by_id)
* [add_reviewer](#add_reviewer)
* [get_reviewers](#get_reviewers)

## get_reviewer_by_id

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

## add_reviewer

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

if res.status_code == 200:
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

## get_reviewers

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
