from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

model = ChatOpenAI(model = "gpt-4-0613") # will talk about temperature(0-2 )& max_completion_tokens parameter while creating a ChatOpenAI object

# You need to recharge your OpenAI account to access and interact with the mentioned models.
# Reference: OpenAI Billing Overview : https://platform.openai.com/settings/organization/billing/overview

result = model.invoke("What is capital of India ?")

print(result)