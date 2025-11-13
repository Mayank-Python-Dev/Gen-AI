from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

#gives error for now because it is not deployed by an Inference Provider ..
#reference : https://www.google.com/search?q=when+i+use+tinylama+from+hugging+face+it+says+provider+%3D+next(iter(provider_mapping)).prov&oq=when+i+use+tinylama+from+hugging+face+it+says+provider+%3D+next(iter(provider_mapping)).prov&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRiPAjIHCAIQIRiPAjIHCAMQIRiPAtIBCDk5OTlqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is capital of India ?")

print(result)