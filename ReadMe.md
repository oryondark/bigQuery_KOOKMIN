# Usage:
*Python 3.5+*<br>
*Set environments to GCP authority if you want this module.*

```python
import bQuery_kookmin_library_forParsing as bQuery

bParser = bQuery.BigqueryParser("bigquery-public-data", "crypto_bitcoin")
bParser.run_query('inputs', 'LIMIT 300000')
bParser.read('btcoin_input.txt')
```
