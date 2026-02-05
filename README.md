# AI-Powered Translator (Flask & AJAX)

An AI-powered web-based translation application built using **Flask** and **AJAX**, following a clean **CS50-style project structure**.
The app allows users to translate words, phrases, or full sentences between multiple languages in real time without reloading the page.

The backend is powered by the **Google Gemini API**, while the frontend uses **vanilla JavaScript (Fetch API)** for asynchronous communication, providing a smooth and responsive user experience.

---

## 🚀 Features

* Real-time translation using AI
* Asynchronous requests with AJAX (no page reload)
* Clean Flask backend with REST-style endpoints
* CS50-inspired project structure (`templates` & `static`)
* Secure API key management using environment variables
* Simple and user-friendly interface

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript (AJAX / Fetch API)
* **AI Model:** Google Gemini
* **Environment Management:** python-dotenv

---

## 📂 Project Structure

```
translator/
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── index.css
```

---

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd translator
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the Flask app**

   ```bash
   python app.py
   ```

6. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

---

## 🎯 Purpose

This project was built for learning purposes to demonstrate how to:

* Integrate AI APIs into a Flask application
* Use AJAX for client-server communication
* Organize a web project using best practices inspired by CS50

---

## 📌 Notes

* Make sure your API key is kept private and **never committed to GitHub**.
* This project is intended for educational and experimental use.

---

⭐ If you like this project, feel free to star the repository!
