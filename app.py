import streamlit as st
import os
import pdfminer.high_level
import docx2txt
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def extract_text(file):
    if file.name.endswith('.pdf'):
        return pdfminer.high_level.extract_text(file)
    elif file.name.endswith('.docx'):
        return docx2txt.process(file)
    return None

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

def rank_resumes(job_desc, resumes):
    all_texts = [job_desc] + resumes
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked_resumes = sorted(zip(resumes, scores), key=lambda x: x[1], reverse=True)
    return ranked_resumes, vectorizer.get_feature_names_out()

def get_improvement_suggestions(job_desc, resume, feature_names):
    job_words = set(word_tokenize(job_desc))
    resume_words = set(word_tokenize(resume))
    missing_keywords = job_words - resume_words
    return missing_keywords

st.title("AI Resume Screening & Ranking System")

st.sidebar.header("Upload Files")
job_file = st.sidebar.file_uploader("Upload Job Description (PDF/DOCX)", type=['pdf', 'docx'])
resume_files = st.sidebar.file_uploader("Upload Resumes (PDF/DOCX)", type=['pdf', 'docx'], accept_multiple_files=True)

if job_file and resume_files:
    job_text = extract_text(job_file)
    job_text = preprocess_text(job_text)

    resume_texts = [preprocess_text(extract_text(file)) for file in resume_files]
    rankings, feature_names = rank_resumes(job_text, resume_texts)

    st.subheader("Ranked Resumes")
    for idx, (resume_text, score) in enumerate(rankings):
        st.write(f"**Rank {idx + 1}:** {resume_files[idx].name} (Score: {score:.2f})")

        suggestions = get_improvement_suggestions(job_text, resume_text, feature_names)
        if suggestions:
            st.markdown("**Suggestions to Improve Resume:**")
            st.write(", ".join(suggestions))
        st.markdown("---")

