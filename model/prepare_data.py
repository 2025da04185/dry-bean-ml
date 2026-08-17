import pandas as pd

# read the excel file
bean_data = pd.read_excel('DryBeanDataset/Dry_Bean_Dataset.xlsx')

bean_data.to_csv('DryBeanDataset/Dry_Bean_Dataset.csv', index=False)

print("Shape: ", bean_data.shape)
print("Columns: ", bean_data.columns)