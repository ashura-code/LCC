from fastapi import APIRouter
from models.comment import *
from services.comment_service import CommentService

router = APIRouter()

service = CommentService()

@router.post('/comments')
def creates_a_new_comment():
    return {'status': 'ok'}
