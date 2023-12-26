# easyreview

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install easyreview
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [dataset](docs/sdks/dataset/README.md)

* [fetch_dataset_from_doi](docs/sdks/dataset/README.md#fetch_dataset_from_doi) - Fetches a dataset from a Dataverse installation and adds it to the database. This function will also check whether the given dataset is already present in the database and thus returns the entry. If not, a new one will be created and returned from this endpoint.

### [field](docs/sdks/field/README.md)

* [get_field_by_id](docs/sdks/field/README.md#get_field_by_id) - Returns a field for a given field ID.
* [update_field](docs/sdks/field/README.md#update_field) - Updates a field for a given field ID.

### [files](docs/sdks/files/README.md)

* [add_file](docs/sdks/files/README.md#add_file) - Adds a new file to the database.
* [get_file_by_id](docs/sdks/files/README.md#get_file_by_id) - Returns a file for a given file ID.
* [get_files](docs/sdks/files/README.md#get_files) - Returns all files.

### [review](docs/sdks/review/README.md)

* [add_review](docs/sdks/review/README.md#add_review) - Adds a new review to the database.
* [get_review_by_id](docs/sdks/review/README.md#get_review_by_id) - Returns a review for a given review ID.
* [update_review](docs/sdks/review/README.md#update_review) - Updates a review for a given review ID.
* [delete_review](docs/sdks/review/README.md#delete_review) - Deletes a review from the database.
* [get_files_by_review_id](docs/sdks/review/README.md#get_files_by_review_id) - Returns all files for a given review ID.
* [get_field_count](docs/sdks/review/README.md#get_field_count) - Returns the number of fields for a given review ID.
* [get_reviews_by_dataset_doi](docs/sdks/review/README.md#get_reviews_by_dataset_doi) - Returns all reviews for a given dataset DOI.
* [get_reviews](docs/sdks/review/README.md#get_reviews) - Returns all reviews.
* [get_reviews_by_reviewer](docs/sdks/review/README.md#get_reviews_by_reviewer) - Returns all reviews for a given reviewer ID.

### [reviewers](docs/sdks/reviewers/README.md)

* [add_reviewer](docs/sdks/reviewers/README.md#add_reviewer) - Adds a new reviewer to the database.
* [get_reviewer_by_id](docs/sdks/reviewers/README.md#get_reviewer_by_id) - Returns a reviewer for a given reviewer ID.
* [get_reviewers](docs/sdks/reviewers/README.md#get_reviewers) - Returns all reviewers.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = None
try:
    res = s.dataset.fetch_dataset_from_doi(doi='string', site_url='string', api_token='string')
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.review is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://localhost:8000` | None |

#### Example

```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    server_idx=0,
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.dataset.fetch_dataset_from_doi(doi='string', site_url='string', api_token='string')

if res.review is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    server_url="http://localhost:8000",
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.dataset.fetch_dataset_from_doi(doi='string', site_url='string', api_token='string')

if res.review is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import easyreview
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = easyreview.EasyReview(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name       | Type       | Scheme     |
| ---------- | ---------- | ---------- |
| `password` | http       | HTTP Basic |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
