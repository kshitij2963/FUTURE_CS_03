# 🔐 Secure File Sharing System — Future Interns (Cyber Security Task 3)

This project is made as part of **Future Interns Cyber Security Internship – Task 3**.

## 📌 Objective  
Create a secure file upload/download portal with **AES encryption** to protect files at rest and in transit.

---

## 🔥 Features
- AES-128 Encryption (EAX mode)  
- Secure File Upload  
- Secure File Download (Auto Decrypt)  
- Clean UI (HTML + CSS)  
- Python Flask Backend  
- Key stored separately for security  
- Safe file handling  

---

## 🛠️ Tech Stack
- **Python + Flask**
- **PyCryptodome (AES)**
- **HTML / CSS**
- **JavaScript**
- **Local Storage**

---

## 📁 Project Structure

```
secure-file-system/
│── app.py
│── key.key
│── templates/
│     └── index.html
│── uploads/
│── README.md
```

---

## 🚀 How to Run

```
pip install flask
pip install pycryptodome
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Testing
1. Upload any file → It gets encrypted  
2. Type filename and download → Auto decrypted

---

## 👨‍💻 Intern Details
**Track Code:** CS  
**Task:** 3 — Secure File Sharing System  
**Intern:** *Kshitij*  

---

## 📌 Notes
❗ Do NOT upload the `key.key` file publicly.  
❗ Use `.gitignore` to protect the key.

---

## ⭐ Output Preview  
- Encrypted file stored inside `/uploads`  
- Decrypted file downloaded as `decrypted_filename.ext`

---

## ✔ Completed for Future Interns Cyber Security Internship  
