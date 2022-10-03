import pandas as pd

df = pd.DataFrame(
    {
        'country': ['UK', 'UK', 'UK', 'Spain', 'Spain', 'Ukraine', 'Ukraine', 'Spain'],
        'city': ['London', 'Oxford', 'Cardiff', 'Madrid', 'Barcelona', 'Kyiv', 'Kharkiv', 'Valencia'],
        'population': [9_002_488, 151_584, 362_400, 2_824_000, 1_454_000, 2_797_553, 1_430_885, 736_000]
    }
)

# view starting data
print(df)

df['total'] = df.groupby('country')['population'].transform('sum')
df = df.drop(['population', 'city'], axis='columns').drop_duplicates()

# view summarised data
print(df)
