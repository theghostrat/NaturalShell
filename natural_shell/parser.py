from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class Command(BaseModel):
    command: str = Field(None, description="The real command based on the input")

parser = JsonOutputParser(pydantic_object=Command)
