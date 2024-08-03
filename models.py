# models.py

from pydantic import BaseModel
from typing import List, Optional

class MovieQuery(BaseModel):
    fields: Optional[List[str]] = None
    search_field: Optional[str] = None
    search_value: Optional[str] = None
