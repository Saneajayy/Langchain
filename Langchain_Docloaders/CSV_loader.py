from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='filename.csv')
docs = loader.load()

print(len(docs))