import streamlit as st

st.set_page_config(
    page_title="House Price Prediction System",
    page_icon="🏠",
    layout="wide"
)

st.title("Welcome to the House Price Prediction App 🏠📈")
st.markdown("Use the left sidebar to navigate between pages.")

st.header("About This Project")
st.markdown("""
Welcome to the interactive platform for **Developing Predictive Models to Estimate Housing Prices with Macroeconomic Indicators**.

This project combines detailed property transaction data and macroeconomic factors to provide a comprehensive view of Denmark's housing market. The app integrates both **forecasting models** and **exploratory data dashboards**, giving users an end-to-end experience in analyzing and predicting house price trends.

---

### 🧰 What You Can Explore Here

- **Interactive Housing Market Dashboard**
  - Filter by year, region, and house type.
  - Examine price distributions, house age, size, and room breakdowns — all with regional insights.
  - Discover the top 10 cities by median price, visualized on an interactive map and bar chart.
  - Explore city-level price maps and compare prices across Denmark.

- **Forecasting with VAR Model**
  - View observed historical prices alongside model predictions.
  - Generate future forecasts interactively by selecting different forecast horizons.
  - Download forecast data for further analysis.

- **Macroeconomic Trends**
  - Compare median house prices against economic indicators like GDP growth, interest rates, inflation, and more.
  - All variables are scaled for intuitive trend comparison.

---

### 💡 Why This Matters

Understanding how house prices evolve over time — and how they relate to broader economic conditions — is crucial for:
- 🏘️ **Homebuyers and sellers**: Timing decisions and price expectations.
- 💼 **Investors and real estate professionals**: Strategic market analysis and investment planning.
- 📊 **Policymakers and economists**: Monitoring housing affordability and market stability.

---

### 🚀 How to Navigate

- Use the sidebar to switch between **Dashboard**, **Forecast**, and **Home** pages.
- Adjust filters and sliders to personalize your analysis.
- Explore interactive plots, download data, and gain insights at every step.

---

Enjoy exploring, and leverage this data-driven tool to understand and predict Denmark’s housing market more effectively!
""")
