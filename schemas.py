from pydantic import BaseModel


from pydantic import BaseModel
from typing import List

# article
class ArticleBase(BaseModel):
    title: str
    content : str
    published : bool
    creator_id : int
    
# user inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():  # this converts from ORM to this type
        orm_mode = True

class ArticleDisplay(BaseModel):
    title: str
    content : str
    published : bool
    user: User
    class Config():  # this converts from ORM to this type
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

# article inside UserDisplay
class Article(BaseModel):
    title: str
    content : str
    published : bool
    class Config():  # this converts from ORM to this type
        orm_mode = True

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():  # this converts from ORM to this type
        orm_mode = True

