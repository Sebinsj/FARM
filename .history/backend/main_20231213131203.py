from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origin=['https://localhost:300']