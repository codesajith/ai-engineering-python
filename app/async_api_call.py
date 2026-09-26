import asyncio
import httpx


BASE_URL = "https://jsonplaceholder.typicode.com"


async def get_user(client, user_id):

    try:
        response = await client.get(
            f"{BASE_URL}/users/{user_id}"
        )

        if response.status_code == 404:
            return {"error": "User not found"}

        response.raise_for_status()

        user = response.json()

        return {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }

    except httpx.HTTPStatusError:
        return {"error": "Request failed"}



async def main():

    async with httpx.AsyncClient() as client:
      users = await asyncio.gather(
       get_user(client,1),
       get_user(client,2),
       get_user(client,3),
       get_user(client,999)
        )

    print(users)

        # Your code here


asyncio.run(main())