
from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()




@app.get("/ping")
def read_hello(request: Request):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)
    return JSONResponse(content="pong", status_code=200)


@app.get("/home")
def welcome_home(request: Request):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text.htlm":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=404)
    return JSONResponse(content="welcome home ", status_code=200 , media_type=text.html )




@app.post("/posts")

class WelcomeRequest(BaseModel):
    author: str
    title : str
    content : str
    creation_datetime : str

def welcome_user(request: WelcomeRequest):
    return {f"info {request.author , request.title , request.content , request.creation_datetime}"}


@app.get("/posts")
def get_posts(request: WelcomeRequest):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)
    return JSONResponse(content=WelcomeRequest, status_code=200)