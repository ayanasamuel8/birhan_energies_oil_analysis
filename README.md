# 📈 **Analysis of Brent Oil Prices: Identifying Structural Breaks with Bayesian Change Point Models**

**🏢 Project for:** Birhan Energies
**📌 Status:** Phase 1 (Foundational Analysis) ✅ *Complete*

---

## 1️⃣ **Business Objective**

This project analyzes the historical prices of Brent crude oil to identify statistically significant structural breaks in the time series.

🎯 The primary goal is to associate these change points with major:

* 🌍 **Geopolitical events**
* 🛢️ **OPEC policy decisions**
* 🌐 **Global economic shocks**

📊 The resulting insights will provide **Birhan Energies** with data-driven intelligence to support strategic advice for investors, policymakers, and other stakeholders in the energy sector.

---

## 2️⃣ **Setup and Installation**

This project uses **Python 🐍** with a virtual environment 🧪 for managing dependencies.

### ✅ Step 1: Create and Activate the Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it (on macOS/Linux) 🐧
source venv/bin/activate

# Or on Windows 🪟
venv\Scripts\activate
```

### ✅ Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

📦 Note: The `requirements.txt` file contains all necessary packages like `pandas`, `pymc`, `arviz`, `matplotlib`, and `jupyter`.

---

## 3️⃣ **Project Structure**

The repository is organized to separate data, notebooks, and source code for clarity.

```
```
birhan_energies_oil_analysis/
├── 📂 data/
│   ├── 📂 compiled/
│   │   └── 📄 events.csv         # Compiled list of major geopolitical/economic events
│   └── 📂 raw/
│       └── 📄 brent_prices.csv   # Raw Brent oil price time series data
│
├── 📂 frontend/
│   └── 📂 src/
│       └── 🖼️ App.tsx            # React component for the interactive UI
│
├── 📂 notebooks/
│   ├── 📓 01_eda_exploration.ipynb          # Exploratory Data Analysis and visualization
│   └── 📓 02_bayesian_changepoint_model.ipynb # Bayesian modeling implementation
│
├── 📂 src/
│   ├── 🐍 app.py               # Flask API for serving data to the frontend
│   └── 🐍 utils.py             # Utility functions for data loading and cleaning
│
├── 📜 .gitignore
├── 📜 README.md              # You are here!
├── 📜 requirements.txt        # Project dependencies
└── 🧪 venv/                    # Virtual environment directory
```
```

---

## 4️⃣ **Project Status & Roadmap**

The project is divided into three main phases. The **initial foundational work** (Task 1) is complete, and we are moving toward modeling. 🚀

* \[✅] **Task 1:** Foundational Analysis & Planning
    → Defined workflow, researched events, documented assumptions
* \[⏳] **Task 2:** Change Point Modeling (Next Step)
    → Implement Bayesian models using PyMC to detect breaks
* \[⬜] **Task 3:** Interactive Dashboard (Future Work)
    → Build a Flask + React interface to explore results

---

## 5️⃣ **Task 1 Deliverable: The Analytical Framework**

This section covers the major outputs from the foundational analysis phase.

---

### 5.1 📅 **Compiled Event Data**

A core part of this task was researching major events relevant to the oil market.

* **📂 Action:** A structured dataset (`data/compiled/events.csv`) contains **20+ key events** from 1987 to 2022.
* **📌 Purpose:** Provides real-world context for interpreting change points, and supports forming analytical hypotheses. 🧠

---


### 5.2 🗺️ **Defined Data Analysis Workflow**

A step-by-step plan from raw data to insights:

1. **🧹 Data Preparation and EDA:**
     Load, clean, visualize, and transform the data (e.g., log returns); test for stationarity.
2. **🤔 Event Hypothesis Formulation:**
     Use `events.csv` to hypothesize structural breaks around known impactful events (e.g., 2008 Crisis).
3. **⚙️ Bayesian Change Point Modeling:**
     Implement a PyMC model to infer structural changes in mean/variance of oil prices.
4. **💡 Insight Generation & Impact Quantification:**
     Compare detected breaks with known events. Quantify "before vs. after" shifts.
5. **📤 Communication and Delivery:**
     Consolidate findings in a report + dashboard for stakeholder insights.

---

### 5.3 ⚠️ **Identified Assumptions and Limitations**

Acknowledging the boundaries of the analysis is essential.

#### 🔑 Key Assumptions:

* **📅 Event Proximity:** Market reacts near the public date of an event.
* **📉 Model Simplicity:** Initial model assumes discrete, instant changes.
* **🧾 Data Coverage:** Events dataset captures the most critical events.
* **📊 Parameter Stability:** Statistical properties remain consistent between change points.

#### 🔍 Limitations: Correlation ≠ Causation ❗️

* **✅ What the model gives:**
    Probabilities of structural breaks. If aligned with events, it shows strong **temporal correlation** 🔗.
* **🚫 What it doesn't give:**
    Proof that an event **caused** the price shift. Correlation may be spurious or influenced by unseen variables.

🔬 *Proving causality is outside this project’s scope.*
Our goal: provide **data-driven evidence** to **support or challenge hypotheses** about event impacts. 🎯
## 6️⃣ **Data Exploration & EDA**

This phase involved a thorough exploration and cleaning of the Brent Oil Prices dataset, leveraging custom utility functions from `src/utils.py` and detailed analysis in the notebook `notebooks/01_eda_exploration.ipynb`.

### 6.1 **Data Loading & Inspection**

- Data is loaded using the `load_data` function from `src/utils.py`.
- The dataset contains 9,011 rows with two columns: `Date` and `Price`, with no missing values.

### 6.2 **Date Format Analysis**

- Two date formats identified in the `Date` column:
    - `ddmmyy` (e.g., `20-May-87`): 8,360 entries
    - `mmddyy` (e.g., `Nov 08, 2022`): 651 entries
- No entries in other formats, ensuring consistency.

### 6.3 **Data Cleaning & Preparation**

- The `Date` column is cleaned and converted to datetime objects, then set as the DataFrame index.
- Data is sorted chronologically for time series analysis.

### 6.4 **Visualization & Stationarity Testing**

- The raw price series is plotted, showing clear trends and volatility.
- Daily log returns are calculated and visualized, appearing stationary and centered around zero.
- Augmented Dickey-Fuller (ADF) tests:
    - **Raw Price Series:** Non-stationary (p-value > 0.05)
    - **Log Return Series:** Stationary (p-value << 0.05)

### 6.5 **Key Insights**

- The dataset is clean and well-structured for time series analysis.
- The price series is non-stationary, while log returns are stationary, which is typical for financial time series.
- This EDA sets the stage for further modeling and forecasting tasks.

---

---

## 7️⃣ **Bayesian Change Point Analysis**

This phase applies Bayesian modeling (using PyMC) to detect structural breaks in the Brent Oil Price time series. The approach allows for probabilistic inference of change points, quantifying uncertainty and providing interpretable results.

### 7.1 **Modeling Approach**

- A Bayesian change point model is implemented to identify points in time where the statistical properties (mean, variance) of the price or log return series shift.
- The model uses Markov Chain Monte Carlo (MCMC) sampling to estimate the posterior distribution of change points.
- Prior information from the compiled events dataset is used to inform hypotheses about likely break dates.

### 7.2 **Key Results & Insights**

- Several statistically significant change points are detected, many of which align closely with major geopolitical or economic events (e.g., 2008 financial crisis, OPEC decisions).
- The model quantifies the magnitude of shifts in mean and volatility before and after each change point.
- Posterior probability plots provide a visual summary of uncertainty around break dates.
- These results support the hypothesis that external events have a measurable impact on oil price dynamics.

### 7.3 **Implications for Stakeholders**

- The Bayesian approach provides a robust framework for understanding market regime shifts.
- Insights can inform risk management, investment strategy, and policy decisions for energy sector stakeholders.
- The methodology is extensible to other time series and event-driven analyses.

### 7.4 **Summary & Recommendations**

- The Bayesian analysis confirms that Brent oil prices experience distinct structural breaks, often coinciding with major global events.
- Quantitative results from the model highlight periods of increased volatility and regime shifts, which are critical for forecasting and scenario planning.
- Stakeholders should monitor identified change points and associated events to better anticipate market movements and adjust strategies accordingly.

---

## 🖥️ Interactive Dashboard & API Integration

This project includes a full-stack solution for exploring Brent oil price data and market events:

### 🌐 API (Flask, `src/app.py`)

- **Endpoints:**
  - `/api/price-data`: Returns daily price and log return data for Brent oil.
  - `/api/events`: Returns a list of major market events with dates and descriptions.
  - `/api/changepoint`: Returns the results of Bayesian changepoint analysis (e.g., volatility shifts).
- **Data Processing:**
  - Loads cleaned price and event data from CSV files.
  - Calculates log returns for volatility analysis.
  - Serves all data in JSON format for easy frontend consumption.

### 🖼️ UI (React, `frontend/src/App.tsx`)

- **Features:**
  - Date range selection for filtering displayed data.
  - Interactive line chart showing price and volatility, with:
    - Key events marked by vertical lines and labels.
    - Bayesian changepoint periods highlighted with shaded regions.
  - Summary card displaying key findings (e.g., volatility increase during the 2008 GFC).
- **Integration:**
  - Fetches all data from the Flask API endpoints.
  - Responsive and user-friendly interface for data exploration.

---