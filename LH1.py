import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats


path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
#print(df[['bore','stroke' ,'compression-ratio','horsepower']].corr())
#print (df[["stroke","price"]] .corr)
#sns.regplot(x="stroke", y="price", data=df)
sns.boxplot(x="body-style", y="price", data=df)
sns.boxplot(x="engine-location", y="price", data=df)
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.ylim(0,)
plt.show()

#print (df['drive-wheels'].value_counts().to_frame())
df_new_grp=df[['body-style','price']]
print ([df_new_grp.groupby('body-style').mean()])
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot = grouped_pivot.fillna(0)
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)