from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt(r'ChatModels\template.json')


if st.button("Submit"): 
    chain = template | llm 
    output = chain.invoke({"paper_input": paper_input, "style_input": style_input, "length_input": length_input
    })
    if (not output):
        st.error("please wait ....")
    else:
        st.write(output.content)
