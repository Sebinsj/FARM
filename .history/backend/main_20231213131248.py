from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origin=['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,allo
)