<!-- Start SDK Example Usage [usage] -->
```python
import easyreview
from easyreview.models import components, operations

s = easyreview.EasyReview(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.fields.get_field_by_id(id='string')

if res.field is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->