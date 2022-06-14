from typing import Any
from pydantic import BaseModel, Field, validator


class TrafficDataItem(BaseModel):
    country: str = Field(..., alias="SpatialDim")
    genders: str = Field(..., alias="Dim1")
    rate: float = Field(..., alias="NumericValue")
    year: int = Field(..., alias="TimeDim")

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)


class WorkItem(BaseModel):
    country: str
    year: int
    rate: float

    @validator("country")
    def three_characters(cls, v):
        if len(v) != 3:
            raise ValueError("Country should be only 3 characters")
