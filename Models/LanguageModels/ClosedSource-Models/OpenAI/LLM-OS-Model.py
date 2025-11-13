from dotenv import load_dotenv
from langchain_openai import OpenAI


load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

# You need to recharge your OpenAI account to access and interact with the mentioned models.
# Reference: OpenAI Billing Overview : https://platform.openai.com/settings/organization/billing/overview

result = llm.invoke("What is capital of India ?")

print(result)


