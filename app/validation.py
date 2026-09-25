from pydantic import BaseModel,Field


class TextAnalyzeRequest(BaseModel):
    prompt:str = Field(alias="text",min_length=1,max_length=1000)

class HistoryItem(BaseModel):
    Id:int
    Prompt:str
    Summary:str
    