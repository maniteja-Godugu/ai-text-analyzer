from google import genai
from pydantic import BaseModel,ValidationError
from google.genai import types
from dotenv import load_dotenv
import os
import json
import logging
from pathlib import Path
logger=logging.getLogger(__name__)
load_dotenv(Path(__file__).parent / ".env")
class TextAnalysis(BaseModel):
    summary:str
    sentiment:str
    topics:list[str]
    difficulty:str
    key_points:list[str]


def llm_api_call(prompt) -> TextAnalysis:
   
    
   api_key=os.getenv("GEMINI_API_KEY")
   try:
    client = genai.Client(api_key=api_key)

  
    logger.info("sending request to  LLM ")
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
            contents=f"""
You are a text analysis assistant.

Analyze the following text.

Your task is to:
1. Create a concise summary.
2. Determine the overall sentiment.
3. Identify the main topics.
4. Estimate the difficulty level.
5. Extract the most important key points.

Return only the requested structured result.

Text to analyze:
{prompt}
""",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=TextAnalysis,
        ),
    )
    logger.info("LLM returned response \n")
    data=json.loads(response.text)
    

    return  TextAnalysis.model_validate(data)
    
   except ValidationError as e:
      
      logger.error("AI response validation failed %s\n",e)
      raise
   except Exception as e:
      logger.error("LLM connection failed %s \n",e)
      raise

   