from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('mypdf.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].metadata)

