from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

result = model.invoke("What is capital of India ?")

print(result)