from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite") 
chat_history = [
    SystemMessage(content="You are a helpful AI assistant. and youer job is to give answer to user in text formate. ( don't give answer in markdown formate) you kan give emoj in your answer."),
]

while True: 
    user_input = input("Usser:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Exiting the chat. Goodbye!")
        break   
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}\n")