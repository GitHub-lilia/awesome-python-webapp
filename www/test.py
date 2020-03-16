import orm,asyncio
from aiohttp import web
from models import User, Blog, Comment

from config import configs

async def test(loop):
    await orm.create_pool(loop,**configs.db)

    u = User(name='Test', email='test1@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()