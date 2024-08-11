## FAST School of Computing Chatbot 🤖

This repository contains a chatbot for FAST School of Computing built using web scraping, embedding, Retrieval-Augmented Generation (RAG) and Streamlit. This chatbot is designed to provide quick and helpful information about the school, its programs, and other relevant resources.

**Features:**

* **Information Retrieval:** The chatbot can answer questions about FAST School of Computing, including its programs and more.
* **Personalized Responses:** Using a Retrieval Augmented Generation (RAG) approach, the chatbot provides accurate and relevant information based on the scraped website data.
* **User-Friendly Interface:** Built with Streamlit, the chatbot offers a seamless and interactive experience for users.

**Technology Stack:**

* **Python:** The core programming language.
* **Scraping:** The website data is scraped using Python libraries like BeautifulSoup.
* **RAG (Retrieval Augmented Generation):**  Combines information retrieval with language generation to provide accurate and relevant responses.
* **LLMs (Large Language Models):** The chatbot uses an LLM (like Gemini) to generate human-like text responses.
* **Streamlit:** Provides the front-end interface for the chatbot.

**How to Use:**

1. **Clone the repository:**
   ```bash
   https://github.com/MuhammadAhmadBajwa/FAST-NUCES-Chatbot.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **GET your API:**
   Get your voyageai API from https://dash.voyageai.com/ and replace it with existing API KEY app.py #line 9
   Get your gemini API from https://aistudio.google.com/app/apikey and replace it with existing API KEY app.py #line 12 
   Signup on these websites , then create an API Key and paste the API KEYS in the app.py.
   
4. **Run the chatbot:**
   ```bash
   streamlit run app.py
   ```

**Screenshot:**

<img alt="Chatbot ScreenShot" src="https://raw.githubusercontent.com/MuhammadAhmadBajwa/FAST-NUCES-Chatbot/main/images/Screeshoot.png">
