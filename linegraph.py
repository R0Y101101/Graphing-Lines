import pandas as pd
import plotly.express as px

# Step 2: Read the CSV data into a DataFrame
df = pd.read_csv("covid_data.csv")

# Step 3: Create a scatter plot
fig = px.scatter(df, x="date", y="cases", color="country", title="COVID-19 Cases Over Time")

# Step 4: Show the graph
fig.show()

