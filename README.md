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

Static metadata for one or more cryptocurrencies.

GET cryptocurrency/info  

Requires id, slug or symbol. Optional parameters are described in API documentation.

    response = cmc.crypto_metadata(id=1)

**crypto_cmc_map()**

Mapping of cryptocurrencies to CoinMarketCap ids.

GET /cryptocurrency/map  

Optional parameters are described in API documentation.

    response = cmc.crypto_cmc_map()
    response = cmc.crypto_cmc_map(symbol='BTC')

**crypto_listings()**

Latest cryptocurrency market data.

GET /cryptocurrency/listings/latest  

Optional parameters are described in API documentation.

    response = cmc.crypto_listings()
    response = cmc.crypto_listings(market_cap_min=10000000000)

**crypto_quotes()**

Latest cryptocurrency market quotes.

GET /cryptocurrency/quotes/latest  

Requires id, slug or symbol. Optional parameters are described in API documentation.

    response = cmc.crypto_quotes(id=1)
    response = cmc.crypto_quotes(id=1, convert='NZD')

**market_metrics()**

Latest global cryptocurrency market metrics.

GET /global-metrics/quotes/latest  

Optional parameters are described in API documentation.

    response = cmc.market_metrics()

**convert_currency()**

Coverts one cryptocurrency or fiat currency into another.

GET /tools/price-conversion  

Requires amount and id or slug. Optional parameters are described in API documentation.

    response = cmc.convert_currency(amount=100, id=1)

**fiat_cmc_map()**

Mapping of fiat currencies to unique CoinMarketCap ids.

GET /fiat/map  

Optional parameters are described in API documentation.

    response = cmc.fiat_cmc_map()

**account_info()**

API key details and usage stats.

GET /key/info  

    response = cmc.account_info()