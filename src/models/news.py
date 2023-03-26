from pydantic import BaseModel


class News(BaseModel):
    title: str
    description: str
    url: str
    urlToImage: str

    class Config:
        extra = "allow"
