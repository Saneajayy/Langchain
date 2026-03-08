from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf', #this means to load all the pdf files in the root folder. (many other patters for other cases)
    loader_cls=PyPDFLoader
)

docs = loader.load() #lazy_load() -- this loads one doc at a time, used when we have very large content to load. (for e.g. 100 pdfs in a folder).

print(len(docs)) 

