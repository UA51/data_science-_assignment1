import matplotlib.pyplot as plt
import pandas as pd

# Your data
data = {
    'congress': [82, 80, 81, 82, 83, 84, 85, 97, 98, 99, 83, 93, 94, 95],
    'start_date': ['1/3/1951', '1/3/1947', '1/3/1949', '1/3/1951', '1/3/1953', '1/3/1955', '1/3/1957', '1/3/1981', '1/3/1983', '1/3/1985', '1/3/1953', '1/3/1973', '1/3/1975', '1/3/1977'],
    'chamber': ['House', 'House', 'House', 'House', 'House', 'House', 'House', 'Senate', 'Senate', 'Senate', 'Senate', 'Senate', 'Senate', 'Senate'],
    'state_abbrev': ['ND', 'VA', 'VA', 'VA', 'VA', 'VA', 'VA', 'SD', 'SD', 'SD', 'NE', 'SD', 'SD', 'SD'],
    'party_code': [200, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 100, 100, 100],
    'bioname': ['AANDAHL, Fred George', 'ABBITT, Watkins Moorman', 'ABBITT, Watkins Moorman', 'ABBITT, Watkins Moorman', 'ABBITT, Watkins Moorman', 'ABBITT, Watkins Moorman', 'ABBITT, Watkins Moorman', 'ABDNOR, James', 'ABDNOR, James', 'ABDNOR, James', 'ABEL, Hazel Hempel', 'ABOUREZK, James George', 'ABOUREZK, James George', 'ABOUREZK, James George'],
    'bioguide_id': ['A000001', 'A000002', 'A000002', 'A000002', 'A000002', 'A000002', 'A000002', 'A000009', 'A000009', 'A000009', 'A000010', 'A000017', 'A000017', 'A000017'],
    'birthday': ['1897-04-09', '5/21/1908', '5/21/1908', '5/21/1908', '5/21/1908', '5/21/1908', '5/21/1908', '2/13/1923', '2/13/1923', '2/13/1923', '1888-07-10', '2/24/1931', '2/24/1931', '2/24/1931'],
    'cmltv_cong': [1, 1, 2, 3, 4, 5, 6, 5, 6, 7, 1, 2, 3, 4],
    'cmltv_chamber': [1, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 4],
    'age_days': [19626, 14106, 14837, 15567, 16298, 17028, 17759, 21144, 21874, 22605, 23552, 15289, 16019, 16750],
    'age_years': [53.73305955, 38.6201232, 40.62149213, 42.6201232, 44.62149213, 46.6201232, 48.62149213, 57.88911704, 59.88774812, 61.88911704, 64.48186174, 41.85900068, 43.85763176, 45.85900068],
    'generation': ['Lost', 'Greatest', 'Greatest', 'Greatest', 'Greatest', 'Greatest', 'Greatest', 'Greatest', 'Greatest', 'Greatest', 'Lost', 'Silent', 'Silent', 'Silent']
}

df = pd.DataFrame(data)

# Convert the 'start_date' column to datetime format
df['start_date'] = pd.to_datetime(df['start_date'])

# Group by 'start_date' and calculate average age
age_over_time = df.groupby('start_date')['age_years'].mean().reset_index()

# Plotting the line plot
plt.figure(figsize=(10, 6))
plt.plot(age_over_time['start_date'], age_over_time['age_years'], marker='o', linestyle='-', color='b')
plt.title('Average Age Over Time')
plt.xlabel('Start Date')
plt.ylabel('Average Age (Years)')
plt.grid(True)
plt.show()
