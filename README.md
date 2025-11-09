# 🔐 Password Complexity Checker  
### Internship Project — Prodigi Info Tech (Task 02)

---

## 🧠 Overview
This project is a **Password Complexity Checker** built using **Python** and **Tkinter** GUI.  
It helps users analyze how strong their passwords are based on real-world security criteria and checks whether the password has appeared in any **known data breaches** — safely and anonymously using the **Have I Been Pwned API**.

---

## ⚙️ Features
✅ Real-time password strength analysis (Weak → Very Strong)  
✅ Evaluates based on:
- Length  
- Uppercase & lowercase letters  
- Numbers  
- Special characters  

✅ Color-coded feedback and clear text-based strength level  
✅ Detailed improvement suggestions  
✅ Toggle password visibility (Show/Hide)  
✅ **Breach Check** via Have I Been Pwned API (k-anonymity method — no full password ever sent)  
✅ Lightweight GUI using Tkinter  

---

## 🧭 How to Use

### 1️⃣ Install Python
Make sure you have **Python 3.8+** installed.  
👉 [Download Python](https://www.python.org/downloads/)  
Check “Add Python to PATH” during installation.

### 2️⃣ Clone or Download the Repository
git clone https://github.com/yourusername/Password-Complexity-Checker-ProdigiInfoTech.git


Or "download the ZIP and extract it."

3️⃣ Install Dependencies

Open the terminal in the project folder and run:
> pip install requests

4️⃣ Run the Application
python password_checker.py

5️⃣ Test Your Password

• Enter any password in the text field.

• Instantly view its strength and suggestions.

• Click “Check Breach” to see if it was found in any public data leaks (done securely).

### 🧩 Requirements

• Python 3.8 or higher <br>
• requests (install via pip) <br>
• tkinter (included in most Python installations) <br>

### 🔐 How the Breach Check Works

This app uses the Have I Been Pwned API safely:
• Only the first 5 characters of your password’s SHA-1 hash are sent to the API. <br>
• The full hash is compared locally, ensuring your full password never leaves your computer. <br>
• If your hash appears in the database results, your password is considered compromised. <br>

### 🧠 Security Notes

✅ Even strong passwords can eventually be cracked through brute force, but such attacks are rare in real-world scenarios. <br>
✅ Use unique passwords for each site, enable 2FA, and consider using a password manager. <br>
✅ The breach lookup requires an internet connection; strength checks work offline. <br>

### 🧰 Tech Stack

-- Language: Python <br>
-- GUI: Tkinter <br>
-- API: Have I Been Pwned <br>
-- Libraries: requests, hashlib, re <br>

### 🧾 License
This project is open-source and free to use for educational purposes.
