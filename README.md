# 🌍 TravelWiz – Python Tkinter GUI Application

TravelWiz is a **desktop-based travel management system** developed using **Python and Tkinter**. This project is a GUI-based conversion of an original **C++ console application**, redesigned to follow modern software design practices while preserving the core functionality.

---

## 📌 Project Overview

TravelWiz allows users to:

* Create and manage user accounts
* Log in securely
* Search and book travel tours
* Select hotels and transportation
* Calculate trip costs automatically
* View profile details
* View booking history

The application is suitable for **academic projects**, especially for courses related to:

* Object-Oriented Programming (OOP)
* Software Engineering
* Human Computer Interaction (HCI)
* Python Programming

---

## 🧑‍💻 Technologies Used

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| Python 3   | Core programming language        |
| Tkinter    | GUI framework                    |
| OOP Design | Code structure & maintainability |

> Note: Tkinter comes **pre-installed** with Python.

---

## 🗂️ Project Structure

```
TravelWiz/
│
├── travelwiz.py        # Main application file
├── README.md           # Project documentation
```

---

## ⚙️ Features

### 🔐 Authentication

* User registration
* Secure login validation

### 🧾 Profile Management

* View user profile details

### 🔍 Tour Booking

* Search travel destination
* Choose hotel & transport
* Enter travel date and number of members
* Automatic cost calculation

### 📦 Booking History

* View all previous bookings per user

### 🎨 GUI Interface

* Clean, button-driven interface
* Multiple screens (Login, Home, Search, Profile, Bookings)

---

## 🧮 Cost Calculation Logic

The trip cost is calculated using the following logic:

```
Cost = (length of hotel name + length of transport name)
       × 500 × number of members
```

This logic was adapted from the original C++ project.

---

## ▶️ How to Run the Project

### Step 1: Install Python

Download Python from:

```
https://www.python.org/downloads/
```

✔ Make sure **"Add Python to PATH"** is checked during installation.

### Step 2: Run the Program

```bash
python travelwiz.py
```

---





---

✨ *Enjoy exploring TravelWiz!* ✨
