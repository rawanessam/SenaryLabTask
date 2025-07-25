from openai import OpenAI
from dotenv import load_dotenv
import os
import json 

### This script runs the OPEN AI backend it prompts Open AI API and returns response

load_dotenv()
#prompt_path = json.loads()
config = os.getenv("CONFIG_FILE")
src_path = os.getcwd()
config_dict = json.loads(open(f"{config}").read())
prompt_path = config_dict["promt_file"]
#os.chdir("..")

    # Get the new current working directory

client = OpenAI(
  api_key = os.getenv("OPENAI_API_KEY"),
  organization = os.getenv("OPENAI_ORG_ID"),
  project = os.getenv("OPENAI_PROJECT_ID"),
  timeout= 30,
)
model = "gpt-4.1"


role = open(f"{prompt_path}",'r').read() ## read prompt text file

## Function that takes prompt and user input and prompts the model
def prompt_llm(prompt=role,user_input="",model=model):  
  res = client.chat.completions.create(
      model=model,
      messages=[{'role':'system','content':prompt},
                  {"role": "user", "content":user_input}]
      )

  result = res.choices[0].message.content

  return(result)
