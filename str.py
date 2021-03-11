import asyncio

from pyrogram import Client


print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Client(":memory:", api_id=int(input("2279350")), api_hash=input("aead80ba4d8b62830a90247b92821a41")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
