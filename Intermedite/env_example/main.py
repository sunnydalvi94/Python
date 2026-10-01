import os
from dotenv import load_dotenv

load_dotenv()

result = os.getenv("site_name")

print(result)