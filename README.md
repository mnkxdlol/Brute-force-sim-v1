# **Brute Force Simulator**  

## **📌 What is this project about?**  
This project simulates different types of **Brute Force attacks** on passwords and hashes using **standard methods**. The graphical interface is developed with **Tkinter**. 

### **🔹 Available Attack Methods:**  
1. **Brute Force Attack:** Tries all possible character combinations to guess the password.  
2. **Dictionary Attack:** Uses a list of common passwords to find a match.  
3. **Attack on Hash:** Attempts to match a given hash (MD5, SHA-256, bcrypt) to its original password using a dictionary-based approach.  

 The program **automatically downloads** multiple password lists from **SecLists**, making the attack more effective! **ENJOY!** :P 

## **💻 How to Install and Run the Project?**  

### **1️⃣ Clone this project**  
```
git clone https://github.com/mnkxdlol/Brute-force-sim-v1.git
cd Brute-force-sim-v1
```

### **2️⃣ Install Python & Dependencies**  
Ensure you have **Python 3.x** installed. If not, download and install it from [Python.org](https://www.python.org/downloads/).  

Then, install the required Python libraries:  
```
pip install -r requirements.txt
```

## **🚀 How to Use the GUI?**  

### **1️⃣ Run the program**  
```
python bruteforce.py
```

### **2️⃣ Using the GUI**  
- **Enter a password or hash** (depending on the attack type).  
- **Select an attack method** from the dropdown menu:  
  - 🔹 **Brute Force:** Tests all possible character combinations.  
  - 🔹 **Dictionary Attack:** Uses a list of common passwords.  
  - 🔹 **Attack on Hash:** Tries to reverse a hash by matching it to known passwords.  
- **Start the attack** by clicking the `"Start the attack! :P"` button.  
- **Clear logs** anytime using the `"Clear Logs"` button.  

## **🛠 How It Works?**  

### **🔹 Brute Force Attack:**  
- The program generates **all possible combinations** of characters (letters, numbers, symbols).  
- It **tries every combination** until it finds the correct password.  
- 🚨 **Time-consuming for longer passwords!**  

### **🔹 Dictionary Attack:**  
- The program downloads **password lists from SecLists** (commonly used/leaked passwords).  
- It **checks each password** from the list until it finds a match.  

### **🔹 Attack on Hash:**  
- Enter a **hashed password** (MD5, SHA-256, bcrypt).  
- The program **tries matching it** to known passwords by hashing them and comparing the results.  

---

## **⚠️ Notes & Performance Considerations**  

- **Hybrid Attack Removed**: A hybrid attack feature was previously available, but it was removed for **optimization reasons**. Feel free to **reimplement it** if needed! :D 
- **Password Lists**: The program downloads multiple password lists from **SecLists** to increase success rates.  
- **Performance Warning**: Brute force attacks on **long passwords** can take a **VERY long time**. The dictionary attack is **much faster** for common passwords.  

---

## **🛠 Troubleshooting**  

- **"ModuleNotFoundError" (Missing dependencies)?**  
  - Run `pip install -r requirements.txt` to install missing libraries.  
- **GUI Freezing?**  
  - The attack process runs on a separate thread, but **Brute Force on long passwords** can be slow. Try using the **Dictionary Attack** for better speed.  
- **"Failed to load password list"?**  
  - Ensure you have **internet access** (password lists are downloaded automatically).  

---

## **📜 License**  
This project is licensed under the **MIT License**. Feel free to modify, share, or contribute!  

---
