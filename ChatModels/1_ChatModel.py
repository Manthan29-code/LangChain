from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = llm.invoke("list all the state with their capitals in India in table format.")
fs = open("result.md", "w", encoding="utf-8")
fs.write(result.content)
fs.close()