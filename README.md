<h1 align="center" id="title">📸 OrionSearch 📸</h1>

<p align="center">
  <i>“A simple, AI-powered local photo search engine — where Python meets Computer Vision.”</i>
</p>

<p align="center">
  <img src="https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt6814c99ef8071ed9/682dffd211a651b72ba9d96d/illustration-search-ai-with-logo-white.png" alt="AI Search Visual" style="max-width:100%;height:auto;border-radius:12px;box-shadow:0 0 15px rgba(0,150,255,0.3);">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-purple" alt="ChromaDB Badge">
  <img src="https://img.shields.io/badge/Model-CLIP-yellowgreen" alt="Model Badge">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="License Badge">
</p>

---

<div align="center">
  <img src="https://img.shields.io/badge/🖼️_Search_Your_Photos_with_Words_-blue?style=for-the-badge" alt="Search with Words">
</div>

---

## ⚙️ About The Project

**OrionSearch** is a lightweight **AI-powered photo search engine** written entirely in Python.
It was built as a portfolio project to demonstrate modern AI/ML integration, vector databases, and app development.

> 🧩 *It’s not Google Photos — but it thinks like it.*

OrionSearch operates on a simple principle: **semantic search**. Instead of searching by filenames, it searches by the *meaning* of your photos.
It includes two primary modules:
- 🔍 **The Indexer:** Scans your image folders, analyzes each photo with the **CLIP** AI model, and stores its "meaning" as a vector in a **ChromaDB** database.
- 🧠 **The Search App:** A **Streamlit** web app that lets you type a text query (like "a red car" or "dog on a beach"), which it converts into a vector to find the most similar images in your database.

---

## 🚨 Features

OrionSearch uses a **modern AI stack** to let you search your local images:

✅ **Semantic Search:** Understands natural language queries. You can search for "pink flower" and it will find your `lotus.jpg`.  
✅ **Local-First Database:** All image "memories" (vectors) are stored 100% locally in a `chromadb` database.  
✅ **Duplicate Prevention:** The indexer is smart and won't re-process images that are already in the database.  
✅ **Simple Web UI:** A clean and fast web app built with `Streamlit` to display search results visually.  
✅ **AI-Powered:** Uses the powerful, pre-trained **CLIP** model from `sentence-transformers` to understand both images and text.  

---

## 🚀 Getting Started

### 🧩 Prerequisites
- Python 3.x
- All libraries from `requirements.txt`

Install all dependencies using:
```bash
pip install -r requirements.txt
```
---

## 💻 Installation
- Clone this repository and enter the project directory:

```Bash

git clone [https://github.com/D-Majumder/OrionSearch.git](https://github.com/D-Majumder/OrionSearch.git)
cd OrionSearch
(Note: You may need to rename your repository on GitHub to OrionSearch for this link to be perfect.)
```

---

## ⚡ Usage
Using OrionSearch is a two-step process:

1. Index Your Photos
-Add your .jpg, .png, or .jpeg images to the test_images folder.

- Run the indexer script to build the AI database. This only needs to be done once per batch of new photos.

```Bash

python indexer.py
(Note: You will see a new folder named orion_db appear.)
```

2. Launch the Search App
-Once your database is built, launch the Streamlit web app:

```Bash

streamlit run app.py
(Note: A browser window will open automatically. Start searching!)
```

## 🧩 Project Philosophy
### 🧠 Learn by building modern, end-to-end AI applications.
OrionSearch helps beginners understand:

- How "semantic search" and "vector embeddings" work.
- How to integrate a large AI model (CLIP) into a Python app.
- How to use a vector database (ChromaDB) to store and query data.
- How to build a simple web UI for an AI tool with Streamlit.

---

## 📜 Disclaimer
This project is for educational and portfolio purposes only. It is a demonstration of AI integration and is not intended as a replacement for professional media management software.

---

## 🛠️ Built With
- Python 🐍 
- Streamlit 🎈 
- ChromaDB 🧠
- sentence-transformers (CLIP) 🤖

---

## 🤝 Connect With Me
<p align="center">
  <a href="mailto:dhrubamajumder@proton.me" target="_blank">
    <img src="https://img.shields.io/badge/Email-Dhruba%20Majumder-blue?logo=gmail" alt="Email Badge">
  </a>
  <a href="https://www.linkedin.com/in/iamdhrubamajumder/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Dhruba%20Majumder-blue?logo=linkedin" alt="LinkedIn Badge">
  </a>
  <a href="https://github.com/D-Majumder" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-D--Majumder-black?logo=github" alt="GitHub Badge">
  </a>
</p>

<div align="center"> 
  <img src="https://img.shields.io/badge/🚀_Built_for_Portfolio_-Learn_AI_Integration-green?style=for-the-badge" alt="Portfolio Project Badge"> 
</div> 
<p align="center"> 
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1E90FF&height=100&section=footer&text=Search+your,+gallery+offline.&fontSize=22&fontColor=111111&animation=fadeIn" /> </p>
