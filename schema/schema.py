from pydantic import BaseModel


class JokeSchema(BaseModel):
    joke: str
