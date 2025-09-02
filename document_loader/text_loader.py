from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('document_loader\cricket.txt', encoding='utf8')

documents = loader.load()

print(type(documents))
print(len(documents))
# print(documents[0].page_content)
print(documents[0].metadata)

chain = prompt | llm | parser

print(chain.invoke({'poem':documents[0].page_content}))



## add on 
# study about text splitter
'''
from langchain.text_splitter import CharacterTextSplitter

# Step 1: Load text file (single Document object)
loader = TextLoader("document_loader/cricket.txt", encoding="utf8")
documents = loader.load()

# Step 2: Use a text splitter
text_splitter = CharacterTextSplitter(
    separator="\n",      # split by newline (you can also use " " for spaces)
    chunk_size=200,      # max characters per chunk
    chunk_overlap=20,    # overlap between chunks to preserve context
)
'''