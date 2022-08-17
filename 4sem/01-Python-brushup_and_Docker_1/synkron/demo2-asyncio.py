import time
import requests
import asyncio


urls = ['https://nytimes.com',
    'https://washingtonpost.com',
    'https://python.org',
    'https://us.pycon.org']

sizes = {}

async def measure_url_content(one_url):
    print(one_url)
    content = requests.get(one_url).content
    sizes[one_url] = len(content)

loop = asyncio.get_event_loop()

start_time = time.time()
for one_url in urls:
    loop.create_task(measure_url_content(one_url))

tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks)
loop.run_until_complete(group)

total_time = time.time() - start_time
print(f'It took {total_time} seconds')