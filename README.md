# AI-Powered Translator (Flask & AJAX)
![python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![html](https://img.shields.io/badge/html-%23E34F26.svg?style=flat&logo=html5&logoColor=white)
![css](https://img.shields.io/badge/css-%231572B6.svg?style=flat&logo=css3&logoColor=white)
![javascript](https://img.shields.io/badge/javascript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E)
![gemini](https://img.shields.io/badge/gemini-886FBF?style=flat&logo=googlegemini&logoColor=white)
![dotenv](https://img.shields.io/badge/dotenv-ecd53f?style=flat&logo=python&logoColor=3776ab)

An AI-powered web-based translation application built using **Flask** and **AJAX**, following a clean **CS50-style project structure**.
The app allows users to translate words, phrases, or full sentences between multiple languages in real time without reloading the page.

The backend is powered by the **Google Gemini API**, while the frontend uses **vanilla JavaScript (Fetch API)** for asynchronous communication, providing a smooth and responsive user experience.

![](https://i.imgur.com/waxVImv.png)

## 🚀 Features

* Real-time translation using AI
* Asynchronous requests with AJAX (no page reload)
* Clean Flask backend with REST-style endpoints
* CS50-inspired project structure (`templates` & `static`)
* Secure API key management using environment variables
* Simple and user-friendly interface

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
> [!NOTE]
> Make sure your API key is kept private and **never committed to GitHub**.
> This project is intended for educational and experimental use.

---

⭐ If you like this project, feel free to star the repository!
