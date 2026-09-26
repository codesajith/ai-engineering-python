import asyncio
import httpx


BASE_URL = "https://jsonplaceholder.typicode.com"


async def get_user(client, user_id):

    response = await client.get(
        f"{BASE_URL}/users/{user_id}"
    )

    user = response.json()

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    }


async def main():

    async with httpx.AsyncClient() as client:

        # Your code here


asyncio.run(main())

