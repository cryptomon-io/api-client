
# API Client

Client implementation of Cryptomon API (https://api.cryptomon.io/swagger-ui.html).


### Run Python code

To run the code below:

1. Click on the cell to select it.
2. Press `SHIFT+ENTER` on your keyboard or press the play button (<button class='fa fa-play icon-play btn btn-xs btn-default'></button>) in the toolbar above.

A full tutorial for using the notebook interface is available [here](ipython_examples/Notebook/Index.ipynb).


```python
from ApiClient import ApiClient

CLIENT_ID = "<API_CLIENT_ID>";
CLIENT_SECRET = "<API_CLIENT_SECRET>"

c = ApiClient(CLIENT_ID, CLIENT_SECRET);
c.request_access()

params = {
    "market" : "BITSTAMP",
    "currencyPair" : "BTC_USD",
    "period" : "ONE_HOUR",
    "ascending" : "true",
    "limit" : "1"
}
r = c.get("https://api.cryptomon.io/api/v1/candles", params)

print("Total rows from API: {}".format(len(r)))

```

    Requesting access_token...
    Success, access_token: b69084f1-527b-23b8-b770-820e4d4fd928, expires_in: 2879
    Request, url: https://api.cryptomon.io/api/v1/candles, params: {'limit': '1', 'market': 'BITSTAMP', 'ascending': 'true', 'period': 'ONE_HOUR', 'currencyPair': 'BTC_USD'}
    Success, status_code: 200
    Total rows from API: 1



```python
# Let's convert this notebook to a README for the GitHub project's title page:
!jupyter nbconvert --to markdown main.ipynb
!mv main.md README.md
```

    [NbConvertApp] Converting notebook main.ipynb to markdown
    [NbConvertApp] Writing 1446 bytes to main.md
