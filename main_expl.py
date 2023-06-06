import pandas as pd
import matplotlib

og_data = pd.read_csv(r'data/Historical Product Demand.csv')
#imbalance = og_data['price_range'].value_counts()
correl = og_data.corr()
describr = og_data.describe()
print(og_data.head(10))
og_data.info()

og_data.dropna(inplace= True)

print(og_data['Order_Demand'].where(og_data['Order_Demand']== '(1)'))

#check if you can make an assumption and gues the null dates
og_data['Order_Demand']= og_data['Order_Demand'].astype(int)
where(df['Rating_Score'] < 50))


filtered_df = og_data[og_data['Order_Demand'].str.contains((', case=False)]