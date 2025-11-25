# Food-Delivery-Surge-Pricing-Analyzer
This is a basic snowflake project i built to learn snowflake.
# Real-Time Food Delivery Surge Pricing Analytics
### Snowflake • Snowpark Python • Streamlit • SQL Analytics

## 📌 Project Summary
This project simulates a real-time surge pricing model for a food delivery platform using the Snowflake Data Cloud. It demonstrates how dynamic demand patterns can be analyzed to calculate surge multipliers and price adjustments across delivery zones.

The solution combines:
- **Snowpark Python Worksheets** for data generation
- **Snowflake tables and views** for storage & analytics
- **SQL-based surge pricing logic**
- **Streamlit in Snowflake** for interactive visualization

This showcases end-to-end data engineering and analytical capability entirely within Snowflake.

---

## ✅ Key Features
### 🔹 Synthetic Real-Time Order Generation
- Built using Snowpark Python
- Generates timestamped order events
- Writes directly into a Snowflake table (`orders_snowpark`)

### 🔹 Surge Pricing Calculation
Implemented using SQL, including:
- Order volumes in the last 30 minutes
- Average order value
- Business-rule surge tiers
- Surge-adjusted pricing output

Delivered through view:
surge_pricing

### 🔹 Interactive Streamlit Dashboard (Inside Snowflake)
Visual insights include:
✅ Surge multipliers by zone  
✅ Surge-adjusted pricing  
✅ Highest demand zone indicator  
✅ Live query integration  

---

## 🧠 Surge Pricing Logic
Demand-based tiers used:

| Orders in last 30 min | Surge Multiplier |
|-----------------------|-----------------|
| 50+                   | 1.6             |
| 30–49                 | 1.3             |
| 15–29                 | 1.15            |
| < 15                  | 1.0             |

Formula:
surge_price = avg_base_price * surge_multiplier

---

## 🏗 Architecture Overview
**Data Generation Layer**
✅ Snowpark Python  
✅ Randomized volume & pricing  
✅ Realistic distribution of surge zones  

**Data Storage Layer**
✅ Snowflake Table: `orders_snowpark`  
✅ Time-based query filtering  

**Analytics Layer**
✅ SQL aggregations  
✅ CASE-based surge logic  
✅ Time window evaluation  

**Presentation Layer**
✅ Streamlit in Snowflake  
✅ No external deployment required  

---

