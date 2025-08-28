from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-2.5-flash')

result = llm.invoke("list the first 10 presidents of the USA")

print(result)