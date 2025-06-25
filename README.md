# 🔍 Voxa – Multimodal AI Assistant

**Voxa** is a smart, voice-enabled AI assistant that combines language models, web search, document analysis, translation, and text-to-speech into a unified conversational experience. Built with a modular design and a friendly Streamlit interface, Voxa dynamically understands what type of input it receives and routes it through the most appropriate processing path.

---

## 🧠 What Is Voxa?

Voxa is not just a chatbot — it’s a **multimodal assistant** that:

- 🎙️ Accepts **voice input** (English or Urdu)
- 📄 Answers questions from **uploaded PDF documents**
- 🌐 Performs **real-time web searches** and summarizes content
- 🧠 Responds to **general queries** using a large language model
- 🔊 **Speaks replies aloud** with audio playback in your selected language

---

## 🧩 How It Works

Voxa uses intelligent query classification to decide what a user is asking. The flow generally looks like this:

### 1. **Input**
- The user provides input via voice or text.
- The system supports both **English and Urdu**.

### 2. **Routing Logic**
The input is analyzed and classified into one of the following:
- `pdf_qa`: Questions based on uploaded documents
- `web_search`: Questions requiring external search
- `general`: Standard chat
- `reset`: Resets chat context

This is handled by a rule-based classifier using keyword matching (`model_router.py`).

### 3. **Processing Pathways**

| Mode | Processing Logic |
|------|------------------|
| **PDF QA** | The PDF is chunked and embedded using `sentence-transformers`, then queried using FAISS. The most relevant chunks are sent along with the user’s question to the LLM. |
| **Web Search** | Uses the Serper.dev API to simulate Google search, scrapes pages using BeautifulSoup, and summarizes results. |
| **General** | Sends the prompt directly to an LLM (DeepSeek model via OpenRouter). |
| **Translation** | If the user prefers Urdu, output text is translated using `deep-translator`. |
| **Text-to-Speech** | gTTS is used to convert responses to speech and play them back in-browser using HTML audio tags. |

---

## 🧰 Tools & Technologies Used

| Category | Tools |
|---------|-------|
| **Frontend/UI** | Streamlit |
| **Voice Input** | `speech_recognition`, `PyAudio` |
| **LLM Access** | OpenRouter (`deepseek/deepseek-r1`) |
| **Embeddings & Search** | `sentence-transformers`, `FAISS` |
| **PDF Parsing** | `PyMuPDF (fitz)` |
| **Web Search** | Serper API + `requests` + `BeautifulSoup4` |
| **Translation** | `deep-translator` |
| **Text-to-Speech** | `gTTS`, `base64`, Streamlit audio embedding |

---

## 🎯 Key Design Principles

- **Modularity**: All major components (LLM, PDF QA, web search, translation, TTS, voice) are separated for easier maintenance and testing.
- **Context Awareness**: The system remembers when it's in "PDF mode" or needs to switch modes based on user input.
- **Multilingual**: Native Urdu support for both input and output (translation + TTS).
- **Accessibility**: Designed for users who prefer voice interaction or local-language communication.

---

## 💬 Why Voxa?

This project demonstrates how modern AI tools can be composed into a **real-world intelligent assistant**, capable of handling diverse queries using multiple forms of input and output — from **legal document analysis** to **current event summaries**, **bilingual voice conversations**, and more.

It was built to explore how far we can stretch language models when paired with traditional software tools, creating a rich user experience that goes beyond simple text interaction.

---

## 🏁 Future Enhancements

- Support for multiple PDF documents at once
- Persistent chat memory across sessions
- Richer summarization (via fine-tuned models)
- Deployable as a web app (via Streamlit Community Cloud or Docker)

---

