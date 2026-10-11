from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="i love llm"
)

vec = response.data[0].embedding
print(len(vec))
print(vec[:4])
# print(
#     json.dumps(
#         response.model_dump(),indent=2,default=str))