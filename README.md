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
birhan_energies_oil_analysis/
├── 📂 data/
│   ├── 📄 compiled/
│   │   └── events.csv         # Compiled list of major geopolitical/economic events
│   └── 📄 raw/
│       └── brent_prices.csv   # Raw Brent oil price time series data
│
├── 📂 notebooks/
│   ├── 📓 01_data_preparation_and_eda.ipynb
│   └── 📓 02_bayesian_changepoint_model.ipynb
│
├── 📂 src/
│   └── # Python source code for models or utilities (if any)
│
├── 📜 .gitignore
├── 📜 README.md              # You are here!
├── 📜 requirements.txt        # Project dependencies
└── 🧪 venv/                    # Virtual environment directory
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