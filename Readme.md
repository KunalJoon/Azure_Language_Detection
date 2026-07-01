# 🌐 Azure AI Language Demo

A modern web application built with **Azure Static Web Apps**, **Azure Functions (Python)**, and **Azure AI Language Service** that demonstrates multiple Natural Language Processing (NLP) capabilities in one application.

## ✨ Features

- 🌍 **Language Detection**
  - Automatically detects the language of the input text.

- 🔒 **PII Redaction**
  - Identifies and redacts Personally Identifiable Information (PII) such as:
    - Names
    - Email Addresses
    - Phone Numbers
    - Credit Card Numbers
    - Other sensitive information

- 📝 **Abstractive Summarization**
  - Generates a human-like summary using Azure AI Language Service.

- ⚡ Fast and responsive user interface

- ☁️ Ready for deployment on Azure Static Web Apps

---

# 📸 Application Preview

## Input

```
Hello, my name is John Smith.

My email is johnsmith@gmail.com

My phone number is 9876543210.

I recently visited your store and had a wonderful experience.

The staff were polite, and the service was excellent.

Overall, I would highly recommend your business.
```

## Output

### Language

```
English
```

### PII Redacted

```
Hello, my name is ********.

My email is *******************

My phone number is **********

I recently visited your store and had a wonderful experience.
```

### Summary

```
The customer had a positive experience while visiting the store.
The staff provided excellent service and the customer highly recommends the business.
```

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
          Static Web App
          (HTML/CSS/JavaScript)
                  │
          HTTP POST Request
                  │
                  ▼
        Azure Function (Python)
                  │
                  ▼
      Azure AI Language Service
      ├── Language Detection
      ├── PII Recognition
      └── Abstractive Summarization
                  │
                  ▼
            JSON Response
                  │
                  ▼
             User Interface
```

---

# 📂 Project Structure

```
.
├── api/
│   └── analyze/
│       ├── __init__.py
│       └── function.json
│
├── src/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── host.json
├── requirements.txt
├── staticwebapp.config.json
└── README.md
```

---

# 🛠 Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- Python 3.x
- Azure Functions
- Azure Static Web Apps
- Azure AI Language Service
- Azure AI SDK

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/yourusername/azure-ai-language-demo.git
```

```
cd azure-ai-language-demo
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a file named:

```
local.settings.json
```

Example:

```json
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "LANGUAGE_ENDPOINT": "https://YOUR-RESOURCE.cognitiveservices.azure.com/",
        "LANGUAGE_KEY": "YOUR_API_KEY"
    }
}
```

---

## Run Locally

```bash
func start
```

Open:

```
http://localhost:4280
```

---

# 🌍 Deployment

Deploy using Azure Static Web Apps.

The project automatically deploys through GitHub Actions when connected to Azure Static Web Apps.

---

# 🔄 Workflow

```
User Input
      │
      ▼
Language Detection
      │
      ▼
PII Redaction
      │
      ▼
Abstractive Summarization
      │
      ▼
Display Results
```

---

# 📌 Example API Response

```json
{
    "language": "English",
    "redacted": "Hello, my name is ********.",
    "summary": "The customer had a positive experience and highly recommends the business."
}
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Azure AI Language Service
- Azure Functions
- REST API Development
- Python Backend Development
- JavaScript Fetch API
- Secure API Integration
- NLP using Cloud AI Services
- Azure Static Web Apps Deployment

---

# 📈 Future Enhancements

- 🌐 Multi-language Translation
- 😊 Sentiment Analysis
- 🔑 Key Phrase Extraction
- 🏷 Named Entity Recognition (NER)
- 📄 Document Classification
- 📊 Processing History
- 🌙 Dark Mode
- 📱 Mobile Responsive Improvements

---

# 👨‍💻 Author

**Kunal Joon**

Student • Sushant University

GitHub: https://github.com/KunalJoon

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
