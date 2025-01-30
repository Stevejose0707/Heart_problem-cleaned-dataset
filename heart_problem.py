import pandas as pd
df=pd.read_csv("C:/Users/Steve Jose/Downloads/heart.csv")
print(df)
print(df.dtypes)
print('*'*100)
#1.no of rows
print(df.shape)
print('*'*100)
#2.column name
df2=df.iloc[:0]
print(df2)
#3.miising value
print(df.isna().sum())
#5
df5=df.groupby('target') ['target'].count().sort_values(ascending=False)
print(df5)
#6
df6=df.groupby('age') ['age'].count().sort_values(ascending=False)
print(df6)
#7
df7=df.loc[df['age']>50].groupby('target') ['target'].count()
print(df7)
#8
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
print(x)
print(y)
#9
k=df['trestbps'].unique()
e=df['restecg'].unique()
print(k)
print(e)
z=df['trestbps'].mean()
df['trestbps'].fillna(z,inplace=True)
h=df['restecg'].mode()[0]
df['restecg'].fillna(h,inplace=True)
l=df['thalach'].mode()[0]
df['thalach'].fillna(l,inplace=True)
xv=df['ca'].mode()[0]
df['ca'].fillna(xv,inplace=True)
d=df['thal'].mode()[0]
df['thal'].fillna(d,inplace=True)


#10
for i in df.index:
    if df.loc[i,'thalach']>180:
        df.loc[i,'thalach']==l
print(df)
print(df.isna().sum())
df.to_csv('C:/Users/Steve Jose/Downloads/Heart_cleaned.csv',index=False)
