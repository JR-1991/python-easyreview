<!-- Start SDK Example Usage [usage] -->
```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.dataset.fetch_dataset_from_doi(doi='string', site_url='string', api_token='string')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->