import pandas as pd

df = {
        'month':[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],
        'sales': [100, 150, 250, 175, 180, 300, 390, 200, 400, 278, 285, 350, 100, 150, 250, 175, 180, 300, 390, 200, 400, 278, 285, 350],
        'product': ['A', 'B', 'A', 'B','A', 'B','A', 'B','A', 'B','A', 'B','A', 'B','A', 'B','A', 'B','A', 'B','A', 'B','A', 'B']
        }

df = pd.DataFrame(df)

df['MoM'] = round((df.groupby('product')['sales'].shift(0) 
                   / df.groupby('product')['sales'].shift(1) - 1) * 100, 2)

print(df.head(10))