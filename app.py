import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import col

# Initialize connection.
conn = st.experimental_connection("snowpark", type="snowpark")

# Load the table as a dataframe using the Snowpark Session.
@st.cache_data
def load_table():
    with conn.safe_session() as session:
        return session.table('mytable').to_pandas()

df = load_table()

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
