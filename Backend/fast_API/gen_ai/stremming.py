from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    reasoning={"effort": "none"},
    input="similar of happy",
    stream=True,
    temperature=1
)

for event in response:
    if event.type == "response.output_text.delta":
      print(event.delta,end="",flush=True)
      time.sleep(0.1)  # Slow down printing

# print(response.output_text)