from pydantic import BaseModel, Field

class Config(BaseModel):
    mute_times: list[int] = Field(default=[1, 5, 10, 30])

