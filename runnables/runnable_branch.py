from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableBranch , RunnablePassthrough , RunnableSequence

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)
parser = StrOutputParser()
report_gen_chain = prompt1 | llm | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | llm | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain , branch_chain )


print(final_chain.invoke({'topic':'Russia vs Ukraine'}))