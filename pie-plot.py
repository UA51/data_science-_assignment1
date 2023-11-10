import matplotlib.pyplot as plt
import pandas as pd

# Sample data for the year 2020 (you can replace this with your actual data)
data = {
    "party": ["DEM", "REP", "Write-in/Scattering/Blank"],
    "votes": [77122723, 72571042, 1053826],
}

df = pd.DataFrame(data)

# Create a pie chart for the year 2020
plt.figure(figsize=(8, 8))
colors = ['blue', 'red', 'lightgray']
explode = (0.1, 0, 0)  # Explode the first slice (DEM)

plt.pie(df["votes"], labels=df["party"], colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.title('Distribution of Votes by Party in U.S. House Election (2020)')

plt.show()
