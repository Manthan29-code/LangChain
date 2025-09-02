from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='document_loader\social_network.csv')

docs = loader.load()
print("Types of file --> " , type(docs))
print("Lenght of file --> " , len(docs))

print(type(docs[1]))
print("First 5 rows of file --> ")
for i in range(5):
    print(docs[i])
