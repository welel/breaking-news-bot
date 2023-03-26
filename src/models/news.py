from pydantic import BaseModel


class News(BaseModel):
    title: str
    description: str | None
    url: str
    urlToImage: str | None

    class Config:
        extra = "allow"
