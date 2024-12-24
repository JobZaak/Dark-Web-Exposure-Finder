import tkinter as tk
from tkinter import messagebox, scrolledtext
import hashlib

# Function to hash email inputs
def hash_email(email):
    return hashlib.sha1(email.encode()).hexdigest()

# Function to check email exposure in a local breach dataset
def check_email():
    email = email_entry.get().strip()
    if not email:
        messagebox.showwarning("Input Error", "Please enter an email address.")
        return

    hashed_email = hash_email(email)
    try:
        with open("breach_dataset.txt", "r", encoding="utf-8") as file:
            breaches = file.readlines()

        
        output_text.insert(tk.END, f"Checking breaches for {email} (hashed: {hashed_email})...\n")
        
        # Search for the hashed email in the breach dataset
        found = False
        for line in breaches:
            breach_info = line.strip().split(",")  # Format: hashed_email,source,date
            if breach_info[0] == hashed_email:
                output_text.insert(
                    tk.END,
                    f"⚠️ ALERT: {email} was found in a breach!\n"
                    f"Source: {breach_info[1]}\nDate: {breach_info[2]}\n\n"
                )
                found = True
                break

        if not found:
            output_text.insert(tk.END, f"No breaches found for {email}. ✅\n\n")

    except FileNotFoundError:
        output_text.insert(tk.END, "Error: Breach dataset file not found.\n")
    except Exception as e:
        output_text.insert(tk.END, f"Unexpected error: {e}\n\n")

# Function to clear the output
def clear_output():
    output_text.delete(1.0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Dark Web Exposure Finder by Job Zaak")
root.geometry("800x600")

# Email Input
email_label = tk.Label(root, text="Enter Email Address:")
email_label.pack(pady=10)

email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=10)

# Buttons
check_button = tk.Button(root, text="Check Breach", command=check_email, bg="green", fg="white", width=15)
check_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear Output", command=clear_output, bg="red", fg="white", width=15)
clear_button.pack(pady=10)

# Output Text Area
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=95, height=25, bg="black", fg="white")
output_text.pack(pady=10)

# Run the application
root.mainloop()
