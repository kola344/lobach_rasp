import aiohttp
import config
import asyncio
from datetime import datetime

async def get_group_id(group):
    async with aiohttp.ClientSession() as session:
        data = {"term": group, "type": "group"}
        try:
            async with session.get(config.api_url_groups, params=data, ssl=False) as response:
                data = await response.json()
                return data[0]["id"], data[0]["label"], data[0]["description"]
        except:
            return None

async def get_schedule(group_id, date_start, date_finish):
    url = config.api_url_get_schelude.replace("%group_id%", str(group_id))
    async with aiohttp.ClientSession() as session:
        # %group_id%, start=(date), finish=(date), lng=1
        data = {"start": date_start, "finish": date_finish, "lng": 1}
        try:
            async with session.get(url, params=data, ssl=False) as response:
                data = await response.json()
                return data
        except:
            return None

if __name__ == "__main__":
    asyncio.run(get_group_id("3824Б1ПИ123"))