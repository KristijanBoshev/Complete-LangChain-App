from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI(
    title="LangChain",
    version="1.0",
    description="API server for LangChain"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()

llm = Ollama(model="phi3")

prompt_openai = ChatPromptTemplate.from_template("Write me instructions on how to {topic}, with 100words")

prompt_ollama = ChatPromptTemplate.from_template("Write me an essay about {topic}, with 100words")

add_routes(
    app,
    prompt_openai|model,
    path="/instructions"
)

add_routes(
    app,
    prompt_ollama|llm,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port="8000")


