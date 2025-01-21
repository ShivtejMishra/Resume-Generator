# ai_enhancement.py
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain import PromptTemplate, LLMChain

# Initialize the GoogleGenerativeAI LLM
llm = GoogleGenerativeAI(model="gemini-pro", api_key="AIzaSyDFK-Rw9JyG4yEejzqJWw0bTUmO1Vn3KaI")

def enhance_summary(summary):
    prompt = PromptTemplate(
        input_variables=["summary"],
        template="Enhance this professional summary: {summary}",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(summary)
    return result
