from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel
from langchain_core.runnables import RunnableSequence
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt1 = PromptTemplate(
    template='Generate one tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate one Linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain  = RunnableParallel(
    {
        'tweet_chain' : RunnableSequence(prompt1, llm, parser) ,
        'linkedin_chain' :  RunnableSequence(prompt2, llm, parser)
    }
)


result = parallel_chain.invoke({'topic': 'AI'})
print(result['tweet_chain'])
print(result['linkedin_chain'])

