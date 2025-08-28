from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_HUB_TOKEN")
)

model = ChatHuggingFace(llm = llm )
result = model.invoke("Explain the theory of relativity in simple terms.")

with open("output.md", "w") as f:
    f.write(result.content)