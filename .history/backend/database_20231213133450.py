from  model import Todo

#mongodb driver
import motor.motor_asyncio

client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database=client.TodoList
collection_name=database.todo

async def fetch_one_todo(title):
    document=await collection_name.find_one({"title":title})
    return document

async