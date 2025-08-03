# 📈 Analysis of Brent Oil Prices: Identifying Structural Breaks with Bayesian Change Point Models

**🏢 Project for:** Birhan Energies
**📌 Status:** Phase 1 - Data Exploration and Analysis Planning *(In Progress)*

---

## 1️⃣ Business Objective

This project aims to analyze the historical prices of Brent crude oil to identify statistically significant **structural breaks** in the time series.

🎯 The primary goal is to associate these **change points** with major:

* 🌍 Geopolitical events
* 🛢️ OPEC policy decisions
* 🌐 Global economic shocks

📊 Insights from this analysis will provide **Birhan Energies** with **data-driven intelligence** to support strategic advice for investors, policymakers, and other energy stakeholders.

---

## 2️⃣ Project Structure

🗂️ The repository is organized to keep data, notebooks, source code, and reports modular and easy to manage:

```
.
├── data/
│   ├── brent_oil_prices.csv       # Raw daily prices (1987–2022)
│   └── events.csv                 # Curated list of major global events
├── notebooks/
│   └── 01_data_exploration.ipynb  # Initial EDA and stationarity analysis
├── reports/
│   └── (Upcoming)                 # For interim and final reports
├── src/
│   └── (Upcoming)                 # For dashboard backend (Flask) and frontend (React)
├── .gitignore
├── README.md                      # You are here
└── requirements.txt               # Project dependencies
```

---

## 3️⃣ Data Sources

📁 **`brent_oil_prices.csv`**
→ Historical daily Brent oil prices from **May 20, 1987** to **September 30, 2022**.

📁 **`events.csv`**
→ A hand-curated list of **major global events**, including:

* Date
* Name
* Type (e.g., geopolitical, economic shock)
* Short description of impact on the oil market

---

## 4️⃣ Setup and Installation

🧪 This project uses **Python** with a **virtual environment** for managing dependencies.

### ✅ Step 1: Create and Activate the Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### ✅ Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

📝 If `requirements.txt` doesn’t exist yet, create it using:

```bash
pip freeze > requirements.txt
```

---

## 5️⃣ How to Run the Analysis

💡 The initial exploration is done in a **Jupyter Notebook**.

🔧 Ensure your virtual environment is activated, and all libraries are installed.

### 📓 Launch Jupyter:

```bash
jupyter lab
```

Then:

* Navigate to the `notebooks/` directory.
* Open `01_data_exploration.ipynb`
* Run the notebook to load data, visualize trends, and perform stationarity tests.

---

## 6️⃣ Project Roadmap

This project will be completed in **three main phases**:

### 📌 Task 1: Foundational Analysis *(In Progress)*

* Define the data analysis workflow ✅
* Research and compile event data into `events.csv` ✅
* Perform initial EDA on the oil price time series
* Finalize interim report for Phase 1

### 📌 Task 2: Change Point Modeling

* Implement Bayesian Change Point models using **PyMC**
* Detect statistically significant change points in the series
* Match these to known events from `events.csv`
* Quantify effects on **price level**, **volatility**, etc.

### 📌 Task 3: Interactive Dashboard

* Build a **Flask** backend to serve the results
* Develop a **React** frontend dashboard
* Create visual tools for exploring:

  * Prices
  * Events
  * Change points
* 🎯 Enable stakeholder-driven insight discovery