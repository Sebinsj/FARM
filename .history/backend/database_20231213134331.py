from  model import Todo

#mongodb driver
import motor.motor_asyncio

client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database=client.TodoList
collection_name=database.todo

async def fetch_one_todo(title):
    document=await collection_name.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos=[]
    cursor=collection_name.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document=todo
    result=await collection_name.insert_one(document) 
    return document 

async def update_todo(title,desc):
    await collection_name.update_one({"title":title},{"$set":{
        "description":desc
    }})
    document=await collection_name.find_one({"title":title})
    return document

async def remove_todo()



