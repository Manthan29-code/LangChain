from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

chai_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('./chat_histroy.txt','r') as file:
    chat_history = file.readlines() 

print(chat_history)

prompt = chai_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)


