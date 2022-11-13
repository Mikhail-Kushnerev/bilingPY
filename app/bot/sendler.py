from aiohttp import ClientSession


async def send_msg(url, data, method):
    if method == "POST":
        async with ClientSession() as session:
            response = await session.post(
                url,
                headers={
                    'Content-Type': 'application/json'
                },
                json=data
            )
    return response
