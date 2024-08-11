import streamlit as st
import google.generativeai as genai
import faiss
import voyageai
import numpy as np
import pickle

if "embedding_model" not in st.session_state:
    voyageai.api_key = 'pa-fc9fffse4_-OfOP7wue323wrlQoeDWBw5yG34o61VsY'    # get your api key from  https://dash.voyageai.com/
    st.session_state.embedding_model = voyageai.Client()
if "LLM_model" not in st.session_state:
    genai.configure(api_key='AIpaSyCTP1iN0Ifp1KCVcjAc_4yPjC_7BhlFA6Q')     # get your api key from https://aistudio.google.com/app/apikey
    st.session_state.LLM_model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def embed_query(query):
    query_embedding = st.session_state.embedding_model.embed([query.lower()], model="voyage-large-2-instruct")
    return np.array(query_embedding.embeddings)

def get_response(query,embeddings,chunks):
    prompt = "Given the context : \n"
  # Function to embed user query
    embedded_query = embed_query(query)
  # Create a FAISS index
    embedding_dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(embedding_dimension)
    index.add(embeddings)

    k = 10  # Number of nearest neighbors to search for
    D, I = index.search(embedded_query, k)
    for i in range(k):
        nearest_index = I[0][i]
        nearest_text = chunks[nearest_index]
        prompt = prompt + nearest_text
    prompt = prompt + "\n\nAnswer this Question in an intelligent, concise way and a better format based on the above provided FAST School of     Computing data : "+query

    response = st.session_state.LLM_model.generate_content(prompt)
    return response.text

# Function to load embeddings and text chunks from files
def load_data():
    embeddings = np.load('embeddings.npy')
    with open('chunks.pkl', 'rb') as f:
        chunks = pickle.load(f)
    return {"embeddings": embeddings,"chunks" : chunks}


st.title("FAST NUCES CHATBOT")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "data" not in st.session_state:
    st.session_state.data = load_data()
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response =  get_response(prompt,st.session_state.data["embeddings"],st.session_state.data["chunks"])
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})