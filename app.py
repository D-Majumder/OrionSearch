import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
import os

# --- 1. Page Setup ---
st.set_page_config(
    page_title="Orion Search",
    layout="wide"
)

# --- 2. Add GitHub Link to Sidebar ---
st.sidebar.title("About")
st.sidebar.markdown(
    "A local, AI-powered photo search engine built by Dhruba Majumder."
)
st.sidebar.markdown(
    "[![GitHub](https://img.shields.io/badge/GitHub-D--Majumder-blue?style=flat&logo=github)]"
    "(https://github.com/D-Majumder)"
)

# --- 3. Main App ---
st.title("Orion: Your Local AI Photo Search")

# Cache the model and db connection
@st.cache_resource
def get_model_and_db():
    # print statements removed to clean up terminal
    model = SentenceTransformer('clip-ViT-B-32')
    db_client = chromadb.PersistentClient(path="./orion_db")
    collection = db_client.get_collection(name="photos")
    return model, collection

model, collection = get_model_and_db()

# --- 4. Search UI ---
query_text = st.text_input("Search your photos:", placeholder="A photo of a...")

if query_text:
    
    # --- 5. Search Logic ---
    query_embedding = model.encode(query_text).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=4 
    )

    # --- 6. Display Results ---
    st.subheader("Search Results")
    
    if not results['ids'][0]:
        st.write("No matching photos found.")
    else:
        cols = st.columns(4) 
        
        for i, (path, metadata) in enumerate(zip(results['ids'][0], results['metadatas'][0])):
            
            if os.path.exists(path):
                with cols[i]:
                    # Fix: use_container_width (removes yellow warning)
                    st.image(path, use_container_width=True) 
                    st.write(f"**{metadata['filename']}**")