# Manajemen Data Pasien Instalasi Gizi  

## Preface  
This project was created as part of **Capstone Module 1** for the **Purwadhika Data Science & Machine Learning Program**.  
The goal is to apply fundamental Python programming concepts by developing a functional, real-world, terminal-based application.  
This system is designed to simulate the **management of patient nutrition data** in a hospital or clinic setting.

---

## Introduction  
The **Patient Nutrition Management System** is a simple Python-based application that allows users to manage patient records — including their physical measurements and nutritional status.  
The program runs on the terminal (CLI) and demonstrates the use of **lists, dictionaries, conditionals, loops, and functions** to create an interactive data management system.  

Each record contains patient information such as:
- Medical Record Number (No RM)  
- Name  
- Gender  
- Age  
- Height and Weight  
- Calculated BMI (IMT)  
- Nutritional Status  

The BMI (IMT) is automatically calculated using the standard WHO formula:  
> IMT = berat badan (kg) / (tinggi badan (m))²  

---

## Features  

### 1. Display All Patient Data  
**Function:** `data_seluruh()`  
**Purpose:** Displays all stored patient data in a well-formatted table with indexed rows.  
**Behavior:**  
- Checks if data exists before printing  
- Displays index, name, gender, IMT, and nutritional status  

---

### 2. Add New Patient Data  
**Function:** `tambah_Data()`  
**Purpose:** Allows users to add a new patient record.  
**Behavior:**  
- Prompts user input for No RM, Name, Gender, Age, Height, and Weight  
- Automatically calculates BMI (IMT) and determines nutritional status  
- Includes input validation for gender (`L/P` only) and numeric fields  
- Asks for confirmation before saving data  

---

### 3. Update Existing Patient Data  
**Function:** `perbarui_Data()`  
**Purpose:** Lets users update specific patient information.  
**Behavior:**  
- Displays the patient list with index references  
- Allows editing of specific fields (Name, Age, Gender, Height, Weight)  
- Automatically recalculates IMT and nutritional status if height or weight changes  

---

### 4. Delete Patient Data  
**Function:** `hapus_Data()`  
**Purpose:** Removes a patient record from the database.  
**Behavior:**  
- Displays all data for reference  
- Asks for the index number to delete  
- Confirms deletion before removing the record  

---

### 5. Read Specific Patient Data  
**Function:** `baca_Data()`  
**Purpose:** Displays either all patients or a specific patient’s data based on user choice.  

---

### 6. Exit Program  
**Option:** Menu 5  
**Purpose:** Terminates the program gracefully with a thank-you message.  

---

## Technology  
Python – The only technology used for this program.

## Conclusion
**Patient Nutrition Management System** serves as a foundational project for understanding how Python can be applied in real-world use cases related to **healthcare and data management**.  
