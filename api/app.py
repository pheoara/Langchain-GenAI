from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

# Load environment variables from .env file
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app= FastAPI (
    title="Langchain Server",
    version="1.8",
    description="A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
# OpenAI model
llm1= ChatOpenAI(model="gpt-3.5-turbo")
# Ollama Llama3
llm2= Ollama(model="llama3")

prompt1= ChatPromptTemplate.from_template("Write me an essay about {topic} of around 100 words")
prompt2= ChatPromptTemplate.from_template("Write me an poem about {topic} of around 100 words")

add_routes(
    app,
    prompt1 | llm1,
    path = "/essay"
)

add_routes(
    app,
    prompt2 | llm2,
    path = "/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host= "localhost",port=8080)

# when you run the app youll ad /docs in end of url and itll open swagger ui