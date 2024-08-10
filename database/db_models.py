# from pydantic import BaseModel, Field
# from typing import List, Optional
# from datetime import datetime
# from bson import ObjectId

# class Movie(BaseModel):
#     # id: Optional[str] = Field(alias="_id")
#     name: str
#     rank: int
#     description: Optional[str] = None
#     actors: List[str]  # Store actor names for simplicity
#     featured_review: Optional[str] = None
#     created_at: datetime
#     updated_at: datetime

# class Actor(BaseModel):
#     # id: Optional[str] = Field(alias="_id")
#     name: str
#     birthdate: Optional[str] = None
#     movies: List[str]  # Store movie IDs as strings for simplicity

#     class Config:
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}




# database/db_models.py

from pydantic import BaseModel, Field
from typing import List, Optional

class Movie(BaseModel):
    name: str
    actors: List[str]
    rank: Optional[int]
    description: Optional[str]
    featured_review: Optional[str]
    created_at: Optional[str] = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: Optional[str] = Field(default_factory=lambda: datetime.utcnow().isoformat())

class Actor(BaseModel):
    #id: Optional[str] = Field(alias="_id")
    name: str
    #birthdate: Optional[str] = None
    movies: List[str]
