import streamlit as st


# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM users;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has ")