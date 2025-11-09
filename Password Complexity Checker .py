# Task-02: Password Complexity Checker with Breach Detection
# Developed using Python Tkinter GUI

import tkinter as tk
from tkinter import ttk, messagebox
import string
import hashlib
import requests

# ------------------- Password Strength Logic -------------------
def check_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(c.islower() for c in password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        strength += 1
    else:
        suggestions.append("Add numbers")

    if any(c in string.punctuation for c in password):
        strength += 1
    else:
        suggestions.append("Add special characters")

    return strength, suggestions


# ------------------- Data Breach Checker -------------------
def check_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return "⚠️ Could not check breach (network error)"
        hashes = (line.split(':') for line in res.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return f"⚠️ This password appeared in {count} data breaches!"
        return "✅ No known breaches found!"
    except:
        return "⚠️ Network error — unable to check breach."


# ------------------- GUI Feedback Update -------------------
def update_feedback(*args):
    password = entry.get()
    strength, suggestions = check_strength(password)

    progress['value'] = strength * 20
    if strength <= 2:
        feedback.set("Weak Password 😟")
        progress_style.configure("green.Horizontal.TProgressbar", background='red')
    elif strength == 3:
        feedback.set("Moderate Password 😐")
        progress_style.configure("green.Horizontal.TProgressbar", background='orange')
    elif strength == 4:
        feedback.set("Strong Password 🙂")
        progress_style.configure("green.Horizontal.TProgressbar", background='blue')
    else:
        feedback.set("Very Strong Password 💪")
        progress_style.configure("green.Horizontal.TProgressbar", background='green')

    suggestion_box.config(state='normal')
    suggestion_box.delete(1.0, tk.END)
    if password:
        if suggestions:
            suggestion_box.insert(tk.END, "Suggestions:\n" + "\n".join("- " + s for s in suggestions))
        else:
            suggestion_box.insert(tk.END, "Perfect! Your password is strong.")
    suggestion_box.config(state='disabled')


# ------------------- Check Breach Button -------------------
def on_breach_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Empty Field", "Please enter a password first.")
        return
    result = check_breach(password)
    breach_status.set(result)


# ------------------- Toggle Visibility -------------------
def toggle_visibility():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text="Show")
    else:
        entry.config(show='')
        toggle_btn.config(text="Hide")


# ------------------- GUI SETUP -------------------
root = tk.Tk()
root.title("Password Complexity Checker - Prodigi Info Tech")
root.geometry("520x480")
root.resizable(False, False)
root.config(bg="#f4f6f8")

tk.Label(root, text="🔐 Password Complexity Checker", font=("Segoe UI", 16, "bold"), bg="#f4f6f8", fg="#222").pack(pady=15)

frame = tk.Frame(root, bg="#f4f6f8")
frame.pack(pady=5)

tk.Label(frame, text="Enter Password:", font=("Segoe UI", 12), bg="#f4f6f8").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(frame, width=30, font=("Segoe UI", 12), show='*')
entry.grid(row=0, column=1, padx=5, pady=5)

toggle_btn = tk.Button(frame, text="Show", command=toggle_visibility, font=("Segoe UI", 10))
toggle_btn.grid(row=0, column=2, padx=5)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, font=("Segoe UI", 12, "bold"), bg="#f4f6f8").pack(pady=10)

progress_style = ttk.Style()
progress_style.theme_use('default')
progress_style.configure("green.Horizontal.TProgressbar", thickness=20, background='red')

progress = ttk.Progressbar(root, style="green.Horizontal.TProgressbar", orient="horizontal", length=350, mode='determinate')
progress.pack(pady=5)

suggestion_box = tk.Text(root, height=6, width=55, font=("Segoe UI", 10))
suggestion_box.pack(pady=10)
suggestion_box.config(state='disabled')

# Breach check section
breach_status = tk.StringVar(value="")
tk.Button(root, text="Check if Password is Breached", command=on_breach_check, font=("Segoe UI", 10, "bold"), bg="#0078D7", fg="white").pack(pady=8)
tk.Label(root, textvariable=breach_status, font=("Segoe UI", 10, "bold"), bg="#f4f6f8", fg="#333").pack(pady=5)

entry.bind("<KeyRelease>", update_feedback)

root.mainloop()
