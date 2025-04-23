# 🧠 AI Chat Extension

This Chrome Extension allows users to interact with a custom AI-powered chatbot that retrieves answers based on URL content. The chatbot is powered by a FastAPI backend using HuggingFace embeddings, Qdrant for similarity search, and MongoDB for logging.

---

## 🌟 Features

- 🔗 Extracts and processes webpage content using a backend API
- 🧠 Asks intelligent questions based on context from the current tab
- 💬 Displays chatbot answers in a popup
- 🛠️ Uses Chrome's tab and cookie APIs
- ⚙️ Built with Manifest V3 and background service workers

---
## 🧩 Installation (For Development)

1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
```

**Open Chrome and go to:

```bash
chrome://extensions/
```bash

- `Enable Developer mode (top right).`

- `Click` Load unpacked and select the project folder.

## 📸 UI
- Minimal popup interface (popup/index.html)

- `Button` to load current tab's content

- Input box to ask questions

- Display area for chatbot answers




