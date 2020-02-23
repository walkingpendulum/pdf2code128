import os

import pdf2image
from aiohttp import web

import decode_code128_from_pdf


def check_auth(request: web.Request):
    auth_value = request.headers.get('Authorization')
    correct_auth_value = 'Bearer %s' % os.environ['SECRET_TOKEN']
    if not auth_value == correct_auth_value:
        raise web.HTTPForbidden()


async def decode_handler(request: web.Request):
    check_auth(request)

    res = await request.post()
    bytes_data = res['data'].file.read()
    code_data_list = decode_code128_from_pdf.extract_code128(input=bytes_data, extractor=pdf2image.convert_from_bytes)
    return web.json_response(code_data_list)



async def ping_handler(request: web.Request):
    return web.Response(text='pong\n')


app = web.Application(client_max_size=1024*1024*32)
app.add_routes([web.get('/ping', ping_handler)])
app.add_routes([web.post('/decode', decode_handler)])


if __name__ == '__main__':
    web.run_app(app, port=int(os.getenv('PORT', '8080')))
