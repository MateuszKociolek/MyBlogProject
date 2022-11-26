from fastapi import APIRouter

from models.post import Post
from config.db import conn
from schemas.post import postEntity, postsEntity
from bson import ObjectId

post = APIRouter()

@post.get('/')
async def findAllPosts():
    print(postsEntity(conn.local.post.find()))
    return postsEntity(conn.local.post.find())

@post.post('/')
async def addPost(post: Post):
    conn.local.post.insert_one(dict(post))
    return postsEntity(conn.local.post.find())

@post.delete('/{id}')
async def deleteById(id):
    return postEntity(conn.local.post.find_one_and_delete({"_id":ObjectId(id)}))