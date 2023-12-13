from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origin=['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=['*'],
    allow_headers=['*'],
)
@app.get("/")
def read_root():
    return {"ping":"pong"}