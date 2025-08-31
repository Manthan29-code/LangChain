from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()   

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

Prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = Prompt1 | llm | parser | prompt2 | llm | parser
chain2 = Prompt1 | llm | parser | prompt2 | llm
result = chain.invoke({'topic':'black hole'})
result2 = chain.invoke({'topic':'dark matter'})
print(type(result))
print(result)

print(type(result2))
print(result2)