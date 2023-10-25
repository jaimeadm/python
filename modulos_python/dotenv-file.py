import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

# print(os.environ)

print(os.getenv('PASSWORD'))