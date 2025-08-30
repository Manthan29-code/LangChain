from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
import os


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_HUB_TOKEN")
)

model = ChatHuggingFace(llm = llm )

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} in\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(type(result))
list_facts = result['facts_about_black_holes']
print(type(list_facts))
for fact in list_facts:
    print(fact)