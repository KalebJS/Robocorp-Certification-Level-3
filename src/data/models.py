from typing import Any
from pydantic import BaseModel, Field


class TrafficDataItem(BaseModel):
    country: str = Field(..., alias="SpatialDim")
    genders: str = Field(..., alias="Dim1")
    rate: float = Field(..., alias="NumericValue")
    year: int = Field(..., alias="TimeDim")

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

        # __pydantic_self__year
