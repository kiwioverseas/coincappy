#!/usr/bin/env python
# Coincappy: Simple Python wrapper around CoinMarketCap free endpoints.

import time
from random import randint
import requests


class RateLimitExceededError(Exception):
    """
    Exception for exceeding API key's rate limit.
    """
    pass


class CoinMarketCap():
    def __init__(self, key=None, timeout=60, rate_limit_retry=False, retry_delay=10, retry_attempts=1):
        if key is None:
            raise ValueError('API key not provided')
        else:
            self.key = key
        
        self.url = 'https://pro-api.coinmarketcap.com/'
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers = {
            'Accepts': 'application/json',
            'Accept-Encoding': 'deflate, gzip',
            'X-CMC_PRO_API_KEY': key
            }
        self.retry = rate_limit_retry
        self.retry_delay = retry_delay
        self.retry_attempts = retry_attempts

    def _query(self, apiversion, urlpath, params_dict=None):
        url = self.url + apiversion + urlpath
        num_retries = 0
        while True:
            response = self.session.get(
                url,
                headers=self.session.headers,
                timeout=self.timeout,
                params=params_dict,
                )

            if response.status_code == 200:
                break
            elif response.status_code == 429 and response.json()['status']['error_code'] in [1009, 1010]:
                raise RateLimitExceededError(response.json()['status']['error_message'])
            elif response.status_code in [429, 500] and rate_limit_retry and num_retries <= self.retry_attempts:
                time.sleep(self.retry_delay + randint(0, 1000)/1000)
                num_retries += 1
                self.retry_delay = 2 ** num_retries * self.retry_delay
            else:
                response.raise_for_status()

        return response.json()['data']

    def crypto_metadata(self, **kwargs):
        """
        Returns all static metadata available for one or more cryptocurrencies.

        GET /cryptocurrency/info

        Required parameters:
        id (string): One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: "1,2"
        slug (string): Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
        symbol (string): Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH".

        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        """
        apiversion = 'v2'
        urlpath = '/cryptocurrency/info'

        req_params = ['id','slug','symbol']
        if not any(arg in req_params for arg in kwargs):
            raise ValueError('Required parameter not provided: {}'.format(', '.join(req_params)))

        return self._query(apiversion, urlpath, kwargs.items())

    def crypto_cmc_map(self, **kwargs):
        """
        Returns a mapping of all cryptocurrencies to unique CoinMarketCap ids.

        GET /cryptocurrency/map
        
        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap
        """
        apiversion = 'v1'
        urlpath = '/cryptocurrency/map'

        return self._query(apiversion, urlpath, kwargs.items())

    def crypto_listings(self, **kwargs):
        """
        Returns a paginated list of all active cryptocurrencies with latest market data.

        GET /cryptocurrency/listings/latest

        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
        """
        apiversion = 'v1'
        urlpath = '/cryptocurrency/listings/latest'

        return self._query(apiversion, urlpath, kwargs.items())

    def crypto_quotes(self, **kwargs):
        """
        Returns the latest market quote for 1 or more cryptocurrencies.

        GET /cryptocurrency/quotes/latest

        Required parameters:
        id (string): One or more comma-separated cryptocurrency CoinMarketCap IDs. Example: "1,2"
        slug (string): Alternatively pass a comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
        symbol (string): Alternatively pass one or more comma-separated cryptocurrency symbols. Example: "BTC,ETH"
        
        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest
        """
        apiversion = 'v2'
        urlpath = '/cryptocurrency/quotes/latest'

        req_params = ['id','slug','symbol']
        if not any(arg in req_params for arg in kwargs):
            raise ValueError('Required parameter not provided: {}'.format(', '.join(req_params)))

        return self._query(apiversion, urlpath, kwargs.items())

    def market_metrics(self, **kwargs):
        """
        Returns the latest global cryptocurrency market metrics.

        GET /global-metrics/quotes/latest

        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest

        """
        apiversion = 'v1'
        urlpath = '/global-metrics/quotes/latest'

        return self._query(apiversion, urlpath, kwargs.items())

    def convert_currency(self, **kwargs):
        """
        Convert an amount of one cryptocurrency or fiat currency into one or more different currencies utilizing the latest market rate for each currency.

        GET /tools/price-conversion

        Required parameters:
        amount (number): An amount of currency to convert. Example: 10.43
        id (string): The CoinMarketCap currency ID of the base cryptocurrency or fiat to convert from. Example: "1"
        symbol (string): Alternatively the currency symbol of the base cryptocurrency or fiat to convert from. Example: "BTC"

        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPriceconversion
        """
        apiversion = 'v1'
        urlpath = '/tools/price-conversion'

        req_params = ['id','symbol']
        if 'amount' not in kwargs or not any(arg in req_params for arg in kwargs):
            raise ValueError('Required parameter not provided: {}'.format('amount, ' + ', '.join(req_params)))

        return self._query(apiversion, urlpath, kwargs.items())

    def fiat_cmc_map(self, **kwargs):
        """
        Returns a mapping of all supported fiat currencies to unique CoinMarketCap ids.

        GET /fiat/map

        Optional parameters:
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap
        """
        apiversion = 'v1'
        urlpath = '/fiat/map'

        return self._query(apiversion, urlpath, kwargs.items())

    def account_info(self):
        """
        Returns API key details and usage stats.

        GET /key/info
        """
        apiversion = 'v1'
        urlpath = '/key/info'

        return self._query(apiversion, urlpath)