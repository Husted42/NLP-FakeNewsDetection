import csv
import pandas as pd

df = pd.read_csv(('sample.csv'))
 
# Creating a dataframe with 80% of the data
part_80 = df.sample(frac = 0.8)
part_80.to_csv('split80.csv', index=False)

# Creating a dataframe with the rest (20%)
rest_part = df.drop(part_80.index) 
rest_part.to_csv('split20.csv', index=False)

# Creating a new dataframe to split the 20 % for test and validation
df10 = pd.read_csv('split20.csv')

# Creating a dataframe with 50% of the data / 10% of the whole dataset 
part_50 = df10.sample(frac=0.5)
part_50.to_csv('split10_1.csv', index=False)

# Creating a dataframe with 50% of the data / 10% of the whole dataset 
part_50_2 = df10.drop(part_50.index)
part_50_2.to_csv('split10_2.csv', index=False)

print("\n80% of DataFrame:")
print(part_80)

print("\n10% of DataFrame:")
print(part_50)

print("\nrest of the 10% of DataFrame:")
print(part_50_2)