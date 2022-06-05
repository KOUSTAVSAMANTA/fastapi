from fastapi import FastAPI
from main import gener
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Course(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/postdata")
def create_course(course: Course):
    x=gener(course.msg)
    return x

# uvicorn sample:app --reload