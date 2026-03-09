from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('mypdf.pdf')

text = """ Space exploration is the scientific study and discovery of outer space using telescopes, satellites, robotic probes, and human spaceflight. Over the past century, it has transformed our understanding of the universe and humanity’s place within it. The launch of the first artificial satellite, Sputnik 1 in 1957, marked the beginning of the space age and sparked rapid advancements in rocket technology and international competition during the Cold War.

One of the most significant milestones in space exploration occurred in 1969, when astronauts from NASA’s Apollo 11 mission successfully landed on the Moon. This historic event demonstrated that humans could travel beyond Earth and safely return, inspiring generations of scientists and engineers. """

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result1 = splitter.split_documents(docs)
result = splitter.split_text(text)
print(result)
print(result1[0])