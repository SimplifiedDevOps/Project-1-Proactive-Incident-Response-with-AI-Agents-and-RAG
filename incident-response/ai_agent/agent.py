# ai_agent/agent.py

from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.embeddings import PineconeEmbeddings
from langchain.retrievers import PineconeRetriever
from langchain.llms import OpenAI  # Use the LLM of your choice

from pinecone_integration.store_and_query import initialize_pinecone
from config.config import PINECONE_INDEX_NAME

# Initialize Pinecone
initialize_pinecone()

# Set up conversation memory to retain context
memory = ConversationBufferMemory(memory_key="chat_history")

# Define a prompt template to guide data collection
prompt_template = PromptTemplate(
    template="""
    You are an AI Incident Response Agent. Given an incident description and retrieved similar incidents,
    suggest potential resolutions based on historical data.

    Incident description: {incident_description}

    Additional context from chat history:
    {chat_history}

    Operator's response:
    {operator_response}

    Please suggest the next steps or request further information as needed, such as logs, cluster status, or previous attempts at resolution.
    """
)

# Set up LangChain embeddings and retriever
pinecone_embeddings = PineconeEmbeddings(index_name=PINECONE_INDEX_NAME)
retriever = PineconeRetriever(embeddings=pinecone_embeddings, top_k=5)

# Define the Retrieval-Augmented Generation (RAG) agent
def create_agent():
    return RetrievalQA(
        retriever=retriever,
        memory=memory,
        prompt=prompt_template,
        llm=OpenAI(model="gpt-3.5-turbo")  # Substitute with your preferred model
    )

def handle_incident_with_agent(incident_description, operator_response=""):
    # Retain conversation context and generate resolution suggestions
    agent = create_agent()
    response = agent({
        "incident_description": incident_description,
        "operator_response": operator_response
    })
    return response
