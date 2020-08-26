from motor.motor_asyncio import AsyncIOMotorClient
from loguru import logger

uri = "mongodb://admin:eastwillpass58@121.36.48.65:27017/admin"

def connect_mongo(uri: str):
    connection_args = {
        "zlibCompressionLevel": 7,
        "compressors": "zlib"
    }
    client = AsyncIOMotorClient(uri, **connection_args)
    return client


logger.debug("1")
client = connect_mongo(uri)
db = client.get_database("admin")
result = db.command("db.getName()")
logger.debug(result)
collection = db.get_collection("system.version")
logger.debug("3")

'''
async def find():
    """
    This method finds items from MongoDB collection and
    processes these by using another asynchronous method
    :return: 
    """
    collection = db.get_collection("system.version")

    filter_ = {
        "someField": "someValue"
    }
    projection_ = {
        "_id": False  # don't return the _id
    }
    cursor = collection.find(filter="")

    # it gets interesting here now. Iterate over the cursor asynchronously
    async for item in cursor:
        await do_something_in_an_async_worker_method(item)
'''

async def find_cursor_to_list():
    """
    This method finds items from MongoDB collection and
    asynchronously converts cursor to a list with items
    :return:
    """
    collection = db.get_collection("")

    filter_ = {
        "someField": "someValue"
    }
    projection_ = {
        "_id": False  # don't return the _id
    }
    cursor = collection.find(filter=filter_, projection=projection_)
    # Convert the cursor to a list of items right away.
    # NB! Dangerous with large result sets
    items = await cursor.to_list(length=500)
    return items
