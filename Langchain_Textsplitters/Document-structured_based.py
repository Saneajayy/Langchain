from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """ class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# example      
p1 = Person("Ajay", 22)
p1.introduce() """

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks[0])