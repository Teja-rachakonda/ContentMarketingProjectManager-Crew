# 🚀 AI Content Generator

An AI-powered content generation platform that creates high-quality content for **Blogs, LinkedIn, Instagram, and YouTube** using Azure OpenAI.

---

## 🌟 Features

- ✨ AI Content Generation (Blog, LinkedIn, Instagram, YouTube)
- 🎤 Voice Input Support
- 🧠 Chat Memory (Context-aware responses)
- ⚡ Streaming Output (real-time generation)
- 📄 Download as PDF
- 📋 Easy Copy Feature
- 📄 Download as TXT

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Azure OpenAI (GPT-4o)  
- **PDF Generation:** ReportLab  

---

## 📂 Project Structure


content_marketing_project_manager/
│
├── agents/ # Planner, Writer, Editor agents
├── backend/ # Orchestrator logic
├── llm/ # Azure OpenAI integration
├── memory/ # Chat memory
├── ui/ # Streamlit UI
├── utils/ # Voice + PDF utilities
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository


git clone https://github.com/YOUR_USERNAME/content_marketing_project_manager.git

cd content_marketing_project_manager


---

### 2️⃣ Create Virtual Environment


python -m venv venv
venv\Scripts\activate


---

### 3️⃣ Install Dependencies


pip install -r requirements.txt


---

### 4️⃣ Add Environment Variables

Create a `.env` file:


AZURE_OPENAI_API_KEY=your_api_key
AZURE_ENDPOINT=your_endpoint


---

### 5️⃣ Run the App


streamlit run ui/app.py


---

## 🚀 How to Use

1. Enter a topic or use voice input 🎤  
2. Select content type (Blog / LinkedIn / Instagram / YouTube)  
3. Click **Generate**  
4. Copy or download content (PDF / TXT)  

---

## 🔐 Security Note

- Never upload your `.env` file to GitHub  
- Always keep API keys secure  

---

## 📌 Future Improvements

- 🌐 Azure Deployment  
- 🔐 User Authentication  
- 💳 Payment Integration  
- 🎨 Advanced PDF Styling  
- 📊 Analytics Dashboard  

---

## 👨‍💻 Author

**Teja Rachakonda**  

- LinkedIn: https://www.linkedin.com/in/teja-rachakonda/  
- GitHub: https://github.com/Teja-rachakonda?tab=repositories

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
