import asyncio

async def greet(word):
    for i in range(5):
        await asyncio.sleep(0.001)
        print(word)

loop = asyncio.get_event_loop()

loop.create_task(greet('hello'))
loop.create_task(greet('goodbye'))

tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks)
loop.run_until_complete(group)
