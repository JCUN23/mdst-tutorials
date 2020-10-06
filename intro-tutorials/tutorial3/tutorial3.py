import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

filepath_train = "C:/Users/atcun/Desktop/mdst/intro-tutorials/tutorial3/exploratory data analysis/train.csv";
filepath_test = "C:/Users/atcun/Desktop/mdst/intro-tutorials/tutorial3/exploratory data analysis/test.csv";
filepath_gender = "C:/Users/atcun/Desktop/mdst/intro-tutorials/tutorial3/exploratory data analysis/gender_submission.csv";
train = pd.read_csv(filepath_train)
test = pd.read_csv(filepath_test)
gender = pd.read_csv(filepath_gender)

# print(train.columns)
# print(train.head())
# print(train.tail())
# print(train.info())
# print(train.shape)
# print(train.describe())
# print(train.describe(include='object'))

train.hist(figsize=(7,8), layout=(2,4));
plt.tight_layout() 

train.hist(column='Pclass', by=train.Survived, sharex=True, label=True)
plt.title('Histogram of Pclass by Survival')
plt.xlabel('Pclass')
fig, axes = plt.subplots(1,2, sharex=True, sharey=True)

train.hist(column='Pclass', by=train.Survived, ax=axes)

fig.text(0.5, 1, 'Histogram of Pclass by Survival', ha='center')
fig.text(0.5, 0.04, 'Pclass', ha='center')


train.boxplot(column='Age', by='Survived')
plt.suptitle('') # removed default subtitle, it overlaps with title
plt.title('Boxplot of Age by Survival Status')
plt.xlabel('Survived (1 = Yes)')
plt.ylabel('Age (years)')
plt.tight_layout()

train.boxplot(column='Fare', by='Embarked')
plt.suptitle('') # removed default subtitle, it overlaps with title
plt.title('Boxplot of Fare by Port of Embarkment')
plt.xlabel('Port of Embarkment')
plt.ylabel('Fare')
plt.tight_layout()

train.plot(kind='scatter', x='Age', y='Fare')
plt.title('Scatterplot of Fare vs Age')

train[['Age','Fare']].corr()

trainbar = train.groupby('Survived').mean()

trainbar.plot.bar(y=['Age','Fare'])
plt.title('Average Age and Fare by Survival Status')
plt.ylabel('Average Age or Fare')
plt.xlabel('Survival Status (1 = Survived)')

train.groupby(['Survived', 'Pclass', 'Sex', 'Embarked']).count().head()

trainSurvivedPclass = pd.crosstab(train.Survived, train.Pclass)
print(trainSurvivedPclass)

trainSurvivedPclass.info()
trainSurvivedPclass.plot.bar()
plt.ylabel('Counts in each Pclass')

Pclassratio = train['Survived'].value_counts('Survived')
print(Pclassratio)

chi= stats.chi2_contingency(trainSurvivedPclass)
print(chi)