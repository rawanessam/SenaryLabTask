### This script checkss for LLM reponse sanity
### All required fields are present, urgency score is between 1-5 and category is valid and one of the identified categories
import json
from typing import Any, Dict

def validate_llm_output(llm_output: str) -> Dict[str, Any]:
    
    valid_categories = ["Bug Report","Feature Request","Praise/Positive Feedback","General Inquiry"]
    parsed =llm_output
   
    if not isinstance(parsed, dict):
        raise ValueError("LLM output must be a JSON object.")

    required_keys = ["feedback_text", "category", "urgency_score"]
    for key in required_keys:
        if key not in parsed:
            raise ValueError(f"Missing required field in LLM output: {key}")

    if not isinstance(parsed["feedback_text"], str ):
        raise ValueError("feedback_text must be a string.")

    if not isinstance(parsed["category"], str) and parsed["category"] in valid_categories:
        raise ValueError("category must be a string.")

    if parsed["urgency_score"] is not None and not isinstance(parsed["urgency_score"], int) and 1<= parsed["urgency_score"]<=5 :
        raise ValueError("urgency_score must be an integer between 1 and 5 or null.")

    return llm_output

#validate_llm_output("")