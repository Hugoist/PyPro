import asyncio
from aiohttp import web


async def handle_root(request):
    """Handles the root route '/'."""
    return web.Response(text="Hello, World!")


async def handle_slow(request):
    """Simulates a long operation with 10 seconds delay."""
    await asyncio.sleep(10)
    return web.Response(text="Operation completed")


async def main():
    """Sets up and runs the aiohttp server."""
    app = web.Application()
    app.add_routes([
        web.get('/', handle_root),
        web.get('/slow', handle_slow)
    ])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    print("Server running on http://localhost:8080")
    await site.start()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
