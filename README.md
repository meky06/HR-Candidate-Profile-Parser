# HR Candidate Profile Parser

An AI-powered HR application that automatically extracts structured candidate information from CVs, transforming unstructured PDF resumes into organized candidate profiles.

## 📌 Project Overview

Recruiters often need to review large numbers of CVs and manually identify key information such as candidate names, contact details, education, skills, and professional experience.

This project addresses this challenge by building an **AI-powered CV parsing system** that processes PDF resumes and extracts relevant candidate information into a structured format.

The project consists of two main components:

* **Kaggle Notebook** — development and experimentation of the CV parsing approach.
* **Streamlit Application** — an interactive GUI that allows users to upload a CV and receive a structured candidate profile.

---

## 🎯 Objectives

* Automate the extraction of information from CVs.
* Convert unstructured resume content into structured candidate data.
* Reduce manual CV screening effort.
* Provide an intuitive interface for HR users.

---

## ⚙️ System Workflow

```text
                    ┌─────────────────┐
                    │   PDF CV Upload │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  CV Processing  │
                    │   & Extraction  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   AI / LLM      │
                    │    Parsing      │
                    └────────┬────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │ Structured Candidate Data  │
              ├─────────────────────────────┤
              │ • Full Name                 │
              │ • Email                     │
              │ • Education                 │
              │ • Skills                    │
              │ • Experience                │
              └──────────────┬──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Streamlit GUI   │
                    └─────────────────┘
```

---

## 🧠 Technologies Used

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| Python           | Core development                             |
| NLP / LLM        | CV information extraction                    |
| Streamlit        | Interactive web application                  |
| REST API         | Communication between application and parser |
| PDF Processing   | Reading CV documents                         |
| JSON             | Structured candidate output                  |
| Jupyter / Kaggle | Development and experimentation              |
| VS Code          | Application development                      |
| Git & GitHub     | Version control                              |

---

## 📊 Information Extracted

The parser extracts the following candidate information:

### Candidate Information

* Full name
* Email address

### Education

* Degree
* Institution
* Graduation year

### Skills

* Technical and professional skills

### Experience

* Job role
* Company
* Years / duration

The extracted information is returned as structured JSON and displayed in a user-friendly candidate profile.

---

## 🖥️ Application

The Streamlit interface provides a simple workflow:

1. Upload a PDF CV.
2. Click **Parse Candidate Profile**.
3. The application sends the CV to the parsing API.
4. The AI system extracts the candidate information.
5. The structured profile is displayed in the interface.

The interface was designed with an HR-oriented workflow in mind, emphasizing readability and quick access to candidate information.

---

## 📓 Notebook

The Kaggle notebook documents the development and experimentation process behind the CV parser.

It includes the model / NLP workflow used to transform CV content into structured candidate information.

**Notebook:**
`notebook/HR_Candidate_Profile_Parser.ipynb`

---

## 🚀 Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/hr-candidate-profile-parser.git
cd hr-candidate-profile-parser
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
python -m streamlit run app/app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
hr-candidate-profile-parser/
│
├── README.md
│
├── app/
│   └── app.py
│
├── notebook/
│   └── HR_Candidate_Profile_Parser.ipynb
│
├── requirements.txt
│
└── .gitignore
```

---

## 🔒 Security & Privacy

CVs contain sensitive personal information. This repository does **not** contain real candidate CVs, personal information, API credentials, or private access tokens.

For demonstration purposes, any API endpoints or credentials should be configured locally rather than committed to the repository.

---

## 🔮 Future Improvements

Potential extensions include:

* Job description matching
* Candidate-job similarity scoring
* Automated skill-gap analysis
* Candidate ranking
* Experience summarization
* Multi-language CV support
* Database storage for candidate profiles
* Recruiter dashboard and analytics
* Bias and fairness monitoring

---

