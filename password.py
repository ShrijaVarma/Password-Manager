import tkinter as tk
from tkinter import messagebox

passwords = {}

def add_password():
    service = service_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if service and username and password:
        passwords[service] = {'username': username, 'password': password}
        messagebox.showinfo("Success", "Password added successfully!")
        service_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")


window = tk.Tk()
window.title("Password Manager")
window.configure(bg="#2e3b4e")  # Set window background to a dark color
window.resizable(False, False)
window.geometry("400x300")

center_frame = tk.Frame(window, bg="#f1f1f1")  # Light background for the center frame
center_frame.pack(padx=20, pady=20, fill="both", expand=True)

instructions = '''To add a password, fill all fields and press "Add Password".\nTo view it, enter Account Name and press "Get Password".'''
tk.Label(center_frame, text=instructions, bg="#f1f1f1", wraplength=350, justify="left", fg="#333333").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(center_frame, text="Account:", bg="#f1f1f1", fg="#333333").grid(row=1, column=0, sticky="e", padx=5, pady=5)
service_entry = tk.Entry(center_frame, bg="#ffffff", fg="#333333", bd=2)
service_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(center_frame, text="Username:", bg="#f1f1f1", fg="#333333").grid(row=2, column=0, sticky="e", padx=5, pady=5)
username_entry = tk.Entry(center_frame, bg="#ffffff", fg="#333333", bd=2)
username_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(center_frame, text="Password:", bg="#f1f1f1", fg="#333333").grid(row=3, column=0, sticky="e", padx=5, pady=5)
password_entry = tk.Entry(center_frame, show="*", bg="#ffffff", fg="#333333", bd=2)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons with customized colors
add_button = tk.Button(center_frame, text="Add Password", command=add_password, width=15, bg="#4CAF50", fg="white", bd=2, relief="solid")
add_button.grid(row=4, column=0, padx=5, pady=10)

get_button = tk.Button(center_frame, text="Get Password", command=get_password, width=15, bg="#2196F3", fg="white", bd=2, relief="solid")
get_button.grid(row=4, column=1, padx=5, pady=10)

# Signature with different font color
signature = "Developed by Shrija Varma"
tk.Label(center_frame, text=signature, bg="#f1f1f1", font=("Arial", 8, "italic"), fg="#777777").grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
