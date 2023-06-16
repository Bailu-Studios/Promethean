import aiohttp

from promethean.requests.exceptions.http_request_exception import HttpRequestException

aiohttp.ClientSession()


class HTTPClient:
    base_url: str
    session: aiohttp.ClientSession
    headers: dict

    def __init__(self, base_url: str, headers: dict = None) -> None:
        if headers is None:
            headers = {}
        self.headers = headers
        self.base_url = base_url
        self.session = aiohttp.ClientSession(base_url, headers=headers)

    def set_headers(self, headers: dict = None):
        if headers is not None:
            self.headers = headers

    async def post(self, url: str = '', args: dict = None, headers: dict = None) -> dict:
        if headers is None:
            headers = self.headers
        if args is None:
            args = {}
        async with self.session.post(url, data=args, headers=headers) as context:
            context: dict = dict(context.json())
            if context['retcode'] == 0:
                return context['data']
            else:
                raise HttpRequestException(context['message'])

    async def get(self, url: str = '', args: dict = None, headers: dict = None) -> dict:
        if headers is None:
            headers = self.headers
        if args is None:
            args = {}
        url = HTTPClient.handle_url(url, args)
        async with self.session.get(url, headers=headers) as context:
            context: dict = dict(context.json())
            if context['retcode'] == 0:
                return context['data']
            else:
                raise HttpRequestException(context['message'])

    async def put(self, url: str = '', args: dict = None, headers: dict = None) -> dict:
        if headers is None:
            headers = self.headers
        if args is None:
            args = {}
        async with self.session.put(url, data=args, headers=headers) as context:
            context: dict = dict(context.json())
            if context['retcode'] == 0:
                return context['data']
            else:
                raise HttpRequestException(context['message'])

    async def delete(self, url: str = '', args: dict = None, headers: dict = None) -> dict:
        if headers is None:
            headers = self.headers
        if args is None:
            args = {}
        url = HTTPClient.handle_url(url, args)
        async with self.session.delete(url, headers=headers) as context:
            context: dict = dict(context.json())
            if context['retcode'] == 0:
                return context['data']
            else:
                raise HttpRequestException(context['message'])

    @classmethod
    def handle_url(cls, url: str = '', args: dict = None) -> str:
        if len(args) != 0:
            url += '?'
            for k, v in args:
                if not url.endswith('?'):
                    url += '&'
                url += f'{k}={v}'
        return url
