from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response =client.chat.completions.create(
    model = "gpt-6-luna",
    messages=[
        {
            "role":"user",
            "content":"what emi in bank"
        }
    ]
)

print(response.choices[0].message.content)

# response = client.responses.create(
#     model="gpt-6-luna",
#     reasoning={"effort": "none"},
#     input="Explain EMI in one line.",
# )

# python -m uvicorn Backend.fast_API.Crud_operation:app --reload