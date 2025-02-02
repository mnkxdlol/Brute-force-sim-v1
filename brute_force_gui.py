import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
import requests
import itertools
import time
import threading
import bcrypt
import queue

# This is the dictionary urls lists, you can change/add if you want
PASSWORD_LIST_URLS = [
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Top1000/Top1000.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-100.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Top1000/Top1000-duplicates.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/500-worst-passwords.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-2009.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/1000-2019.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/wordlist-2019.txt",
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/common-1-billion.txt"
]

class BruteForceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Brute Force Sim")
        self.root.geometry("600x500")
        self.root.configure(bg="#2b2b2b")
        self.logs = []
        self.queue = queue.Queue()

        # this is the title and input, welp you can change it too 
        self.title_label = tk.Label(root, text="Brute Force Sim", font=("Helvetica", 20), fg="white", bg="#2b2b2b")
        self.title_label.pack(pady=10)

        self.password_label = tk.Label(root, text="Enter your password or hash:", font=("Helvetica", 12), fg="white", bg="#2b2b2b")
        self.password_label.pack(pady=5)
        self.password_input = tk.Entry(root, font=("Helvetica", 12))
        self.password_input.pack(pady=5)

        self.method_label = tk.Label(root, text="Select the method:", font=("Helvetica", 12), fg="white", bg="#2b2b2b")
        self.method_label.pack(pady=5)
        self.method_select = ttk.Combobox(root, values=["Brute Force", "Dictionary", "Hash attack"], font=("Helvetica", 12), state="readonly")
        self.method_select.set("Brute Force")
        self.method_select.pack(pady=5)

        # Start and clear buttons
        self.start_button = tk.Button(root, text="Start the attack! :p", font=("Helvetica", 14), bg="red", fg="white", command=self.start_attack)
        self.start_button.pack(pady=10)

        self.clear_logs_button = tk.Button(root, text="Clear Logs", font=("Helvetica", 12), bg="gray", fg="white", command=self.clear_logs)
        self.clear_logs_button.pack(pady=5)

        # Log area and progress bar
        self.log_area = tk.Text(root, height=10, width=60, font=("Courier", 10), bg="#1e1e1e", fg="white", wrap="word")
        self.log_area.pack(pady=10)
        self.log_area.insert(tk.END, "Attack logs...\n")

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="indeterminate")
        self.progress_bar.pack(pady=10)

        # About and warning sentence
        self.about_button = tk.Button(root, text="About me", font=("Helvetica", 12), bg="gray", fg="white", command=self.show_about)
        self.about_button.pack(pady=5)

        self.warning_label = tk.Label(root, text="Everything is not secured, even your password.", font=("Helvetica", 10), fg="red", bg="#2b2b2b")
        self.warning_label.pack(pady=5)

        # Start the log update loop
        self.update_log()

    def show_about(self):
        about_message = (
            "This project is open source and created by mnkxdlol.\n"
            "Read the GitHub repository if you want to contribute.\n"
            "Feel free to suggest improvements or report bugs!"
        )
        messagebox.showinfo("About me", about_message)

    def log(self, message):
        self.logs.append(message)
        self.queue.put(message)

    def update_log(self):
        try:
            while True:
                message = self.queue.get_nowait()
                self.log_area.insert(tk.END, message + "\n")
                self.log_area.yview(tk.END)
        except queue.Empty:
            pass

        self.root.after(100, self.update_log)

    def brute_force(self, correct_password, max_length=4):
        self.logs = []
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        attempts = 0
        start_time = time.time()

        for length in range(1, max_length + 1):
            for guess in itertools.product(chars, repeat=length):
                attempt = ''.join(guess)
                attempts += 1
                self.log(f"🔍 Attempt {attempts}: {attempt}")
                if attempt == correct_password:
                    duration = time.time() - start_time
                    self.log(f"✅ Found your password: {attempt} in {attempts} attempts! ({duration:.2f}s)")
                    self.progress_bar.stop()
                    self.password_input.delete(0, tk.END)  # To clear the input after the attack
                    return attempt
        self.log("❌ Failed to find the password.")
        self.progress_bar.stop()
        self.password_input.delete(0, tk.END)
        return None

    def load_password_list(self):
        
        passwords = []
        for url in PASSWORD_LIST_URLS:
            try:
                self.log(f"🔍 Attempting to load password list from: {url}")
                response = requests.get(url)
                response.raise_for_status()  
                passwords.extend(response.text.splitlines()) 
            except requests.RequestException as e:
                self.log(f"❌ Failed to load password list from {url}: {e}")
        return passwords

    def dictionary_attack(self, correct_password):
        self.logs = []
        
        passwords = self.load_password_list()
        attempts = 0

        start_time = time.time()

        if not passwords:
            self.log("❌ Password list is empty or could not be loaded.")
            self.progress_bar.stop()
            self.password_input.delete(0, tk.END)  # To clear the input after the attack
            return None

        for password in passwords:
            password = password.strip()
            attempts += 1
            self.log(f"🔍 Attempt {attempts}: {password}")
            if password == correct_password:
                duration = time.time() - start_time
                self.log(f"✅ Found your password: {password} in {attempts} attempts! ({duration:.2f}s)")
                self.progress_bar.stop()

                self.password_input.delete(0, tk.END)
                return password

        self.log("❌ Failed to find the password.")
        self.progress_bar.stop()
        self.password_input.delete(0, tk.END)
        return None

    def hash_attack(self, hash_value, hash_type):
        self.logs = []
        passwords = self.load_password_list()
        attempts = 0
        start_time = time.time()

        for password in passwords:
            attempts += 1
            if hash_type == "MD5":
                hashed = hashlib.md5(password.encode()).hexdigest()
            elif hash_type == "SHA-256":

                hashed = hashlib.sha256(password.encode()).hexdigest()
            elif hash_type == "bcrypt":
                hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            self.log(f"🔍 Attempts {attempts}: {password} -> {hashed}")
            if hashed == hash_value:
                duration = time.time() - start_time
                self.log(f"✅ Found the hash: {password} in {attempts} attempts! ({duration:.2f}s)")
                self.progress_bar.stop()

                self.password_input.delete(0, tk.END)
                return password

        self.log("❌ Failed to find the hash.")
        self.progress_bar.stop()
        self.password_input.delete(0, tk.END)
        return None

    def start_attack(self):
        input_password = self.password_input.get()
        method = self.method_select.get()

        if not input_password:
            messagebox.showerror("Error", "Enter a password or hash.")
            return

        # Start the progress bar
        self.progress_bar.start()

        # Start the attack in a new thread
        attack_thread = threading.Thread(target=self.run_attack, args=(input_password, method))
        attack_thread.start()


    def run_attack(self, input_password, method):
        self.log("🔍 Starting attack...")

        if method == "Brute Force":
            self.brute_force(input_password, 4)
        elif method == "Dictionary":
            
            self.dictionary_attack(input_password)
        elif method == "Hash attack":

            self.hash_attack(input_password, "MD5")

    def clear_logs(self):
        self.log_area.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceApp(root)
    root.mainloop()