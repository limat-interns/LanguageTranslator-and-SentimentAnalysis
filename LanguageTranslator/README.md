
# 🌐 Advanced Language Translator

A Flask-based web application that allows users to translate text between multiple languages. It includes advanced **RTL (Right-To-Left)** formatting support for languages like Arabic, Hebrew, and Urdu, and also supports optional **reversing of input** before translation.

---

## 🚀 Features

- 🌍 Translate text between various languages using **Google Translate API**.
- 🔁 Optionally reverse input (word-wise and character-wise) before translation.
- 🔠 Auto-detects if the target language is an RTL language and updates the display direction accordingly.
- 📋 One-click **copy** functionality for the translated output.
- 🎨 Clean and responsive UI with RTL support.

---

## 📂 Project Structure

```
LanguageTranslator/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 🛠️ Requirements

Install all dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```txt
Flask>=2.0
googletrans==4.0.0-rc1
langdetect
requests
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🌐 Supported Languages

| Language             | Code |
| -------------------- | ---- |
| English              | `en` |
| French               | `fr` |
| Spanish              | `es` |
| German               | `de` |
| Italian              | `it` |
| Portuguese           | `pt` |
| Russian              | `ru` |
| Chinese (Simplified) | `zh` |
| Japanese             | `ja` |
| Korean               | `ko` |
| Hindi                | `hi` |
| Tamil                | `ta` |
| Telugu               | `te` |
| Bengali              | `bn` |
| Gujarati             | `gu` |
| Kannada              | `kn` |
| Malayalam            | `ml` |
| Marathi              | `mr` |
| Punjabi              | `pa` |
| Urdu                 | `ur` |
| Arabic               | `ar` |
| Turkish              | `tr` |
| Vietnamese           | `vi` |
| Thai                 | `th` |
| Dutch                | `nl` |
| Greek                | `el` |
| Hebrew               | `iw` |
| Polish               | `pl` |
| Ukrainian            | `uk` |
| Romanian             | `ro` |


---

## ✅ TODO

- [ ] Language auto-detection toggle
- [ ] Voice input and output
- [ ] Language history & recent translations
- [ ] Better RTL font styling

---

## 👨‍💻 Author

**Ganesh Arihanth**

> Open to collaboration and feedback! 🌟

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute.
