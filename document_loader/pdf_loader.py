from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('document_loader\dl-curriculum.pdf')

documents = loader.load()

print(type(documents))

print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)