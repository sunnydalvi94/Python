from openai import OpenAI

import json

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    reasoning={"effort":"none"},
    # temperature=0,
    # max_output_tokens=20,
    input=[
        {"role":'user',"content":"what is electonic device?"  },
        {"role":"system","content":"you are good assistant"}
    ]
)

# print(
# json.dumps(
#     response.model_dump(),
#     indent=2,
#     default=str
# )
# )
print(response.output_text)

