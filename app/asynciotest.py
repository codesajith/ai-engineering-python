import asyncio

async def say_hello():
    await asyncio.sleep(2)
    print("Hello")

#asyncio.run(say_hello())

async def fetch_data():
    print("Starting...")
    await asyncio.sleep(2)
    print("Data received")

#asyncio.run(fetch_data())


async def fetch_users():
    print("Fetching users...")
    await asyncio.sleep(2)
    print("Users received")

async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(2)
    print("Orders received")

async def call_model_a():
    print("Calling Model A...")
    await asyncio.sleep(2)
    return "Model A response"


async def call_model_b():
    print("Calling Model B...")
    await asyncio.sleep(3)
    return "Model B response"


async def call_model_c():
    print("Calling Model C...")
    await asyncio.sleep(1)
    return "Model C response"

async def get_user():
    await asyncio.sleep(2)
    return {"user": "Sarah"}


async def get_preferences():
    await asyncio.sleep(1)
    return {"theme": "dark"}


async def get_ai_profile():
    await asyncio.sleep(3)
    return {"model": "Gemini"}

async def main():
   result = await asyncio.gather(
    get_user(),
    get_preferences(),
    get_ai_profile()
    )
   print("User : " + str(result[0])) 
   print("Preferences: " + str(result[1])) 
   print("AI Profile: " + str(result[2])) 

asyncio.run(main())