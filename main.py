
from router import product
from http.client import HTTPException
from fastapi import FastAPI, Request, status
from exceptions import StoryException
from router import blog_get
from router import blog_post, article
from auth import authentication
from db.database import engine
from db import models
from router import user
from fastapi.responses import JSONResponse, PlainTextResponse


app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc : StoryException):
  return JSONResponse(status_code=418,content={"detail" : exc.name})

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc : StoryException):
#   return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


models.Base.metadata.create_all(engine) # creates the db(only if not there)
# if u change something in the tables u want to recreate it 