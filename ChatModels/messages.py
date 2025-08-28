from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

message = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content='Tell me about LangChain in 5 lines ')
]

result = model.invoke(message)

message.append(AIMessage(content=result.content))

for msg in message:
    print(f"{msg.type}: {msg.content}\n")