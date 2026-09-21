import asyncio
import httpx


async def get_user():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://jsonplaceholder.typicode.com/users/1"
        )
        user = response.json()

        print(response.status_code)
        print(f"User: {user['name']}")
        print(f"email: {user['email']}")



asyncio.run(get_user())