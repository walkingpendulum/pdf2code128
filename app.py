from aiohttp import web
import os


async def hello(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes([web.get('/', hello)])

if __name__ == '__main__':
    web.run_app(app, port=int(os.getenv('PORT', '8080')))
