import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

"""Loading the dataset provided in the assignment folder"""

df=pd.read_csv("/content/drive/MyDrive/Churn_Modelling.csv")

df.info()

df.describe()

"""1. UNIVARIATE ANALYSIS
The term univariate analysis refers to the analysis of one variable. You can remember this because the prefix “uni” means “one.” There are three common ways to perform univariate analysis on one variable: 1. Summary statistics – Measures the center and spread of values.

#
Histogram
"""

sns.displot(df["Age"], color='darkorange')

"""In Histogram, we can do it vertically too, by just changing the axis"""

sns.histplot(y="Age",data=df,color='darkorange')

"""Now, we can also use Histogram for categorical variables"""

sns.histplot(x='Age',data=df,hue=df['Tenure'])

"""Distplot"""

sns.distplot(df["Age"],color='purple')

"""This is visualising displot alone"""

sns.distplot(df["Age"],hist=False,color='blue')

"""Boxplot"""

sns.boxplot(df["Age"],color='pink')

"""Countplot"""

sns.countplot(df['Age'])

"""2. BIVARIATE ANALYSIS
#
Image result for bivariate analysis in python It is a methodical statistical technique applied to a pair of variables (features/ attributes) of data to determine the empirical relationship between them. In order words, it is meant to determine any concurrent relations (usually over and above a simple correlation analysis).

#
Barplot
"""

sns.barplot(df["NumOfProducts"],df["Age"])

"""Linearplot"""

sns.lineplot(df["Age"],df["NumOfProducts"], color='purple')

"""Scatterplot"""

sns.scatterplot(x=df.Age,y=df.RowNumber,color='green')

"""Pointplot"""

sns.pointplot(x='Age',y='Tenure',data=df,color='pink')

"""Regplot"""

sns.regplot(df['Age'],df['Tenure'],color='orange')

"""3. MULTI - VARIATE ANALYSIS
#
Multivariate analysis is based in observation and analysis of more than one statistical outcome variable at a time. In design and analysis, the technique is used to perform trade studies across multiple dimensions while taking into account the effects of all variables on the responses of interest.

#
Pairplot
"""

sns.pairplot(data=df[["RowNumber","Age","Tenure","Balance","NumOfProducts"]],kind="kde")

sns.pairplot(data=df[["RowNumber","Age","Tenure","Balance","NumOfProducts"]], hue="Age", diag_kind="hist")

sns.pairplot(data=df[["RowNumber","Age","Tenure","Balance","NumOfProducts"]], hue="Age")

"""4. Perform descriptive statistics on the dataset
#
Image result for descriptive statistics in python Python Descriptive Statistics process describes the basic features of data in a study. It delivers summaries on the sample and the measures and does not use the data to learn about the population it represents. Under descriptive statistics, fall two sets of properties- central tendency and dispersion.

#
"""

df.describe()

"""5. Handle the Missing values."""

data=pd.DataFrame({"a":[1,2,np.nan],"b":[1,np.nan,np.nan],"c":[1,2,4]})
data

data.isnull().any()

data.isnull().sum()

data.fillna(value = "S")

data["a"].mean()

data["a"].median()

"""6. Find the outliers and replace the outliers
#
For data that follows a normal distribution, the values that fall more than three standard deviations from the mean are typically considered outliers. Outliers can find their way into a dataset naturally through variability, or they can be the result of issues like human error, faulty equipment, or poor sampling.

#
"""

outlierss=df.quantile(q=(0.25,0.75))

outlierss

sns.boxplot(df["Age"],color='purple')

df["Age"]=np.where(df["Age"]<25,50,df["Age"])

sns.boxplot(df["Age"],color='pink')

"""7. Check for Categorical columns and perform encoding.
#
Categorical Columns : Categorical are a Pandas data type. A string variable consisting of only a few different values.

#
Encoding : For efficient storage of these strings, the sequence of code points is converted into a set of bytes. The process is known as encoding.

#
"""

df.head(4)

df["Gender"].replace({"Female":0,"Male":1},inplace = True)
df["Geography"].replace({"France":1,"Spain":2,"Germany":3},inplace = True)
df["Gender"].replace({"Female":0,"Male":1},inplace = True)
df["Geography"].replace({"France":1,"Spain":2,"Germany":3},inplace = True)

df.head(4)

"""8. Split the data into dependent and independent variables.
#
Dependent Variable : A dependent variable is a variable whose value depends on another variable.

#
Independent Variable : An Independent variable is a variable whose value never depends on another variable but the researcher.

#
"""

y = df["Surname"]

x=df.drop(columns=["Surname"],axis=1)

x.head()

"""9. Scale the independent variables"""

names=x.columns
names

from sklearn.preprocessing import scale

X=scale(x)

X

x = pd.DataFrame(X,columns = names )
x

"""10. Split the data into training and testing

#
Train/Test is a method to measure the accuracy of your model. It is called Train/Test because you split the the data set into two sets: a training set and a testing set. 80% for training, and 20% for testing. You train the model using the training set.

#
"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

x_train.head()

x_train.shape,y_train.shape,x_test.shape,y_test.shape

