from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions = 300)

documents = [
    "Virat Kohli is a great Batsmen",
    "Ms-Dhoni is a great Wicket Keeper",
    "Jasprit Bumrah is the great Bowler"
]

documents_embedding = embedding.embed_documents(documents)

query_embedding = embedding.embed_query("Who is virat kohli?")

result = cosine_similarity([query_embedding], documents_embedding)[0]

index, score = sorted(list(enumerate(result)),key = lambda x : x[1])[-1]

print(documents[index])
