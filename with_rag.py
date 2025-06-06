from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

loader = PyMuPDFLoader("SQL Revision Notes.pdf")
docs = loader.lazy_load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
chunks = text_splitter.split_documents(docs)
embedd = HuggingFaceEmbeddings()
db = FAISS.from_documents(chunks,embedd)
retriver = db.as_retriever(search_type="similarity",kwargs={"k":3})
query = "What is sql"
retriver_docs = retriver.invoke(query)
print(retriver_docs[0].metadata)