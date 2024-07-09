from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Ensure the environment variables are loaded
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Set environment variables
os.environ["OPENAI_API_KEY"] = openai_api_key

# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)
# st.write("Prompt template created successfully.")

# Ollama LLM opensource no charges
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
# st.write("LangChain components initialized successfully.")

# Streamlit framework
st.title('Langchain Demo With llama3 API')
input_text = st.text_input("Search the topic you want")

# Display the input for debugging
st.write("User Input:", input_text)

# Execute the chain if input_text is provided
if input_text:
    result = chain.invoke({'question': input_text})
    st.write("Result:", result)
