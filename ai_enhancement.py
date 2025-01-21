from langchain_google_genai.llms import GoogleGenerativeAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the GoogleGenerativeAI LLM
llm = GoogleGenerativeAI(model="gemini-pro", api_key=api_key)

def enhance_summary(summary):
    prompt = PromptTemplate(
        input_variables=["summary"],
        template="Enhance this professional summary: {summary}",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(summary)
    return result
