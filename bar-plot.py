import matplotlib.pyplot as plt
import pandas as pd

# Sample data (you can replace this with your actual data)
data = {
    "year": [2014, 2014, 2014, 2016, 2016, 2016, 2018, 2018, 2018, 2020, 2020, 2020],
    "party": ["DEM", "REP", "Other", "DEM", "REP", "Other", "DEM", "REP", "Other", "DEM", "REP", "Write-in/Scattering/Blank"],
    "votes": [35355530, 781825, 0.994032714, 60319623, 50616149, 2.103300871, 60263478, 50654841, 2.105768014, 77122723, 72571042, 1053826],
}

df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(10, 6))
colors = {"DEM": 'blue', "REP": 'red', "Other": 'gray', "Write-in/Scattering/Blank": 'lightgray'}
party_order = ["DEM", "REP", "Other", "Write-in/Scattering/Blank"]

for party in party_order:
    party_data = df[df["party"] == party]
    plt.bar(party_data["year"], party_data["votes"], label=party, color=colors[party])

plt.xlabel('Year')
plt.ylabel('Total Votes')
plt.title('Total Votes by Party in U.S. House Elections (2014-2020)')
plt.xticks(df["year"].unique())
plt.legend()

plt.show()
