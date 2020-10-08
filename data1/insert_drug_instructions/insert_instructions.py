import asyncio

from insert_drug_instructions.insert_Qiju_Dihuang_Wan import insert_Qiju_Dihuang_Wan

async def main():
    await insert_Qiju_Dihuang_Wan()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())