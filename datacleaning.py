import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.columns)

df.drop(['Luminosity', 'Unnamed: 0', 'Unnamed: 6','Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'], axis=1, inplace = True)

final_data=df.dropna()
final_data.reset_index(drop=True, inplace = True)
final_data.to_csv("cleaned_data.csv")
print(final_data.head(5))
