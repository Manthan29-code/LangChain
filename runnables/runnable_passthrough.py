from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel , RunnablePassthrough , RunnableSequence

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)
joke_gen_chain = RunnableSequence(prompt1, llm, parser)


parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, llm, parser)
})


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))