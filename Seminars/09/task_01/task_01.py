"""
df.query("housing_median_age > 51")
df.query("housing_median_age > 51 and total_rooms < 1000")
df [ df['population'] < 20 ] [['total_bedrooms', 'total_rooms']]
df.query("population < 20") [ ['total_bedrooms', 'total_rooms']]

df.loc[     df['population'] < 20,   ['total_bedrooms', 'total_rooms']    ]
df.loc[     df['median_income'] < 2,   [ 'median_house_value']    ]
df.loc[     df['median_income'] < 2,   [ 'median_house_value']    ]

print(df['median_house_value'].max())
print(df['median_house_value'].min())
df.query('median_income == 3.1250') [['median_house_value']].max()
apr = df['median_house_value'].min() * 1.45
df.query(f'median_house_value < {apr}') [['population']].max()
"""