from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

url= 'https://www.apple.com/in/macbook-neo/?afid=p240%7Cgo~cmp-23617594767~adg-196369366000~ad-799078594206_kwd-2468200336486~dev-c~ext-~prd-~mca-~nt-search&cid=wwa-in-kwgo-mac-noncore_macbookneo-macbookneo-macbookneo_hero_announce_030426-MacBookNeo-MacBookNeo-apple+macbook+neo'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)