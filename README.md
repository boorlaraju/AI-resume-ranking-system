# 🚀 AI Resume Screening and Ranking System

## 📌 Overview
The **AI Resume Screening and Ranking System** uses **NLP and ML** to rank resumes based on their relevance to the uploaded job description.  
It also provides **improvement suggestions** by identifying missing keywords.

---

## ⚙️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **Libraries:**  
    - `streamlit`: For the UI  
    - `pdfminer.six`: Extracts text from PDFs  
    - `docx2txt`: Extracts text from DOCX files  
    - `nltk`: Text preprocessing  
    - `scikit-learn`: For TF-IDF and cosine similarity  

---

## 📁 Folder Structure
📁 AI-Resume-Ranking-System  
 ┣ 📁 resumes               # Folder to store uploaded resumes  
 ┣ 📁 job_descriptions      # Folder to store job descriptions  
 ┣ 📁 models                # (Optional) Folder for saving ML models  
 ┣ 📄 app.py                # Main Streamlit application  
 ┣ 📄 requirements.txt      # Dependencies  
 ┣ 📄 README.md             # Project documentation  
 ┣ 📄 .gitignore            # Git ignore file  
 ┣ 📄 config.py             # Configuration settings (optional)  
 ┗ 📄 utils.py              # Utility functions  

