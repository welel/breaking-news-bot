from pydantic import BaseModel, Field


class News(BaseModel):
    title: str
    description: str | None
    url: str
    image_url: str | None = Field(alias="urlToImage")

    class Config:
        extra = "allow"
