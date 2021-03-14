# Coincappy
Simple Python wrapper around CoinMarketCap free endpoints.

## Installing

Install from PyPI using pip:

    pip install coincappy

Install directly from repository:

    pip install git+https://github.com/kiwioverseas/coincappy.git

## Usage

Response data is in JSON format.

    from coincappy import CoinMarketCap

    cmc = CoinMarketCap(API_KEY)
    response = cmc.crypto_quotes(symbol='BTC')
    
    print(response['BTC'][0]['quote']['USD']['price'])

## Endpoints

CoinMarketCap API documentation is available at https://coinmarketcap.com/api/documentation/v1/

Endpoints available using the basic/free plan are supported:

**crypto_metadata()**

GET cryptocurrency/info  
Static metadata for one or more cryptocurrencies.

Requires id, slug or symbol. Optional parameters are described in API documentation.

    response = cmc.crypto_metadata(id=1)

**crypto_cmc_map()**

GET /cryptocurrency/map  
Mapping of cryptocurrencies to CoinMarketCap ids.

Optional parameters are described in API documentation.

    response = cmc.crypto_cmc_map()
    response = cmc.crypto_cmc_map(symbol='BTC')

**crypto_listings()**

GET /cryptocurrency/listings/latest  
Latest cryptocurrency market data.

Optional parameters are described in API documentation.

    response = cmc.crypto_listings()
    response = cmc.crypto_listings(market_cap_min=10000000000)

**crypto_quotes()**

GET /cryptocurrency/quotes/latest  
Latest cryptocurrency market quotes.

Requires id, slug or symbol. Optional parameters are described in API documentation.

    response = cmc.crypto_quotes(id=1)
    response = cmc.crypto_quotes(id=1, convert='NZD')

**market_metrics()**

GET /global-metrics/quotes/latest  
Latest global cryptocurrency market metrics.

Optional parameters are described in API documentation.

    response = cmc.market_metrics()

**convert_currency()**

GET /tools/price-conversion  
Coverts one cryptocurrency or fiat currency into another.

Requires amount and id or slug. Optional parameters are described in API documentation.

    response = cmc.convert_currency(amount=100, id=1)

**fiat_cmc_map()**

GET /fiat/map  
Mapping of fiat currencies to unique CoinMarketCap ids.

Optional parameters are described in API documentation.

    response = cmc.fiat_cmc_map()

**account_info()**

GET /key/info  
API key details and usage stats.

    response = cmc.account_info()