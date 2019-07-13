# Usage:
*Python 3.5+*<br>
*Set environments to GCP authority if you want this module.*

```python
import bQuery_kookmin as bQuery

bParser = bQuery.BigqueryParser("bigquery-public-data", "crypto_bitcoin")
bParser.run_query('inputs', 'LIMIT 300000')
bParser.read('btcoin_input.txt')
```


### creator
hyunjune kim <br>
Department of Convergence Design and Technology on Kookmin University, Bigdata Laboratory. <br>
Major : Sofware Engineer( or Data Engineer ) <br>
*Researcher in Convergence Research Centor*
