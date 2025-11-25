import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get Snowflake session
session = get_active_session()

# Query surge pricing data using fully qualified name
df = session.sql("""
    SELECT * 
    FROM food_delivery.surge_demo.surge_pricing
""").to_pandas()

st.title("🚀Surge Pricing Dashboard")
st.write("Live surge analytics powered by Snowflake + Streamlit")

# Show raw data
st.subheader("📋 Surge Pricing Data")
st.dataframe(df)

# Chart 1 — Surge Multiplier by Zone
st.subheader("🔥 Surge Multiplier by Zone")
st.bar_chart(df.set_index("ZONE")["SURGE_MULTIPLIER"])

# Chart 2 — Surge Price by Zone
st.subheader("💰 Surge Price by Zone")
st.bar_chart(df.set_index("ZONE")["SURGE_PRICE"])

# Insight
highest_zone = df.sort_values("SURGE_MULTIPLIER", ascending=False).iloc[0]["ZONE"]
st.success(f"Highest surge zone right now: **{highest_zone}**")
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get Snowflake session
session = get_active_session()

# Query surge pricing data using fully qualified name
df = session.sql("""
    SELECT * 
    FROM food_delivery.surge_demo.surge_pricing
""").to_pandas()

st.title("🚀 Surge Pricing Dashboard")
st.write("Live surge analytics powered by Snowflake + Streamlit")

# Show raw data
st.subheader("📋 Surge Pricing Data")
st.dataframe(df)

# Chart 1 — Surge Multiplier by Zone
st.subheader("🔥 Surge Multiplier by Zone")
st.bar_chart(df.set_index("ZONE")["SURGE_MULTIPLIER"])

# Chart 2 — Surge Price by Zone
st.subheader("💰 Surge Price by Zone")
st.bar_chart(df.set_index("ZONE")["SURGE_PRICE"])

# Insight
highest_zone = df.sort_values("SURGE_MULTIPLIER", ascending=False).iloc[0]["ZONE"]
st.success(f"Highest surge zone right now: **{highest_zone}**")
