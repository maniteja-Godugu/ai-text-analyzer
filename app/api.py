from fastapi import FastAPI,HTTPException
from pydantic import ValidationError,BaseModel,Field
from app.LLM import llm_api_call
from app.validation import TextAnalyzeRequest,HistoryItem
from app.logging_config import setup_logging
from app.operations import insert_data,get_history,get_history_by_id,delete_history_by_id

setup_logging()
app=FastAPI()


@app.post("/analyze",status_code=201)
def analyze(input: TextAnalyzeRequest):
    prompt = input.prompt

    try:
        data = llm_api_call(prompt)

        insert_data(
            prompt,
            data.summary,
            data.sentiment,
            data.difficulty
        )

        return data

    except ValidationError:
        raise HTTPException(
            status_code=502,
            detail="The AI returned data that could not be validated."
        )

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI service is currently unavailable."
        )


@app.get("/history", response_model=list[HistoryItem])
def history(Id: int):
    data = get_history()
    if data is None:
        raise HTTPException(
            status_code=404,
            detail="History not found"
        )
    data_list = []

    for row in data:
        data_dict = {
            "Id": row["Id"],
            "Prompt": row["Prompt"],
            "Summary": row["Summary"]
        }

        data_list.append(data_dict)

    return data_list


@app.get("/history/{id}")
def history_by_id(id: int):
    data = get_history_by_id(id)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="History not found"
        )

    return data


@app.delete("/history/{id}")
def delete_history(id: int):
    data=get_history_by_id(id)
    if data is None:
        raise HTTPException(
         status_code=404, 
        detail="History not found" 
        )
    delete_history_by_id(id)
    return {"message": "History deleted successfully"}

