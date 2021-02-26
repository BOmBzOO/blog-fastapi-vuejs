from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, validator

from .comment import CommentSerializer


class PostSerializer(BaseModel):
    id: str
    title: str
    content: str
    comments: List[CommentSerializer] = []

    created_by: str
    created_at: datetime
    updated_at: datetime


class PostInSerializer(BaseModel):
    title: str
    content: str

    @validator('title', 'content')
    def validate_empty_data(cls, v):
        if not v:
            raise ValueError('This field is required')
        return v

    @validator('title')
    def validate_title(cls,v):
        if len(v) < 5:
            raise ValueError('Minimum length of title is 5 chars')
        return v


class PostInPatchSerializer(BaseModel):
    title: Optional[str]
    content: Optional[str]
