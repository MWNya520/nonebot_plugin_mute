from pydantic import BaseModel, Field

class Config(BaseModel):
    MUTE_TIMES: list[int] = Field(default=[1, 5, 10, 30])

