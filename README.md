# ✈️ Flight Analytics Dashboard

A simple interactive dashboard to explore and analyze flight data using Python, Streamlit, and MySQL.

---

## 📌 About the Project

This project was built as part of my learning journey in data analysis.
The goal was to work with real-world structured data and create a small analytics tool where users can explore flights and visualize patterns.

Instead of just writing SQL queries, I wanted to present the data in a more meaningful and interactive way.

---

## 🚀 What this app does

* Search flights between two cities
* Show airline distribution using a pie chart
* Identify busiest airports
* Visualize daily flight trends

---

## 🛠️ Tech Stack

* Python
* Streamlit
* MySQL
* Plotly

---

## 📊 Features

### 🔍 Flight Search

Select source and destination to view available flights.

### 🥧 Airline Distribution

Visual representation of how flights are distributed across airlines.

### 📍 Busy Airports

Bar chart showing airports with highest traffic.

### 📈 Daily Trends

Line chart to track number of flights over time.

---

## 📂 Project Structure

* `app.py` → Main Streamlit app 
* `dbhelper.py` → Database connection & queries 
* `crud.py` → Practice file for MySQL operations 

---

## ⚙️ How to Run

1. Clone the repository

```bash
git clone https://github.com/iqbal188/flight-analytics-dashboard.git
cd flight-analytics-dashboard
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Setup MySQL

* Create a database named `flights`
* Import your dataset into a table named `flights`

4. Run the app

```bash
streamlit run app.py
```

---

## 📸 Screenshots


<img width="1920" height="1080" alt="Screenshot 2026-04-18 171224" src="https://github.com/user-attachments/assets/5ae5c812-b2ef-4fbf-98f6-36b46cbbe8dd" />



<img width="1920" height="1080" alt="Screenshot 2026-04-18 171234" src="https://github.com/user-attachments/assets/5c291176-99a2-4f3c-998c-6c45ff39c934" />



<img width="1920" height="1080" alt="Screenshot 2026-04-18 170823" src="https://github.com/user-attachments/assets/9fb2b2a2-3156-46fe-9469-6e16f9a8ac92" />


---

## 💡 What I Learned

* Connecting Python with MySQL
* Writing SQL queries for analysis
* Building dashboards using Streamlit
* Creating visualizations using Plotly

---

## 🔮 Future Improvements

* Add filters (price, date, airline)
* Improve UI design
* Deploy the app online

---

## 👨‍💻 Author

Mohd Iqbal
Data Analyst

---
