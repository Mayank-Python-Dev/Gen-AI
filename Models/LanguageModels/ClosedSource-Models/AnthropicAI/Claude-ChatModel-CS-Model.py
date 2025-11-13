from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

#visit : https://console.anthropic.com/ to create APIKEY

model = ChatAnthropic(model = "claude-3.5-sonnet-20241022")

result = model.invoke("What is capital of India ?")

print(result)