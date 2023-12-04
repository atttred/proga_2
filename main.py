import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("titanic.csv")

print(data.head())
print(data.info())

survived = data['Survived'].value_counts()
print(survived)

clas = data[data['Survived'] == 0]['Pclass'].value_counts()
total = data['Pclass'].value_counts()
print(clas)
print(clas/total)


data['AgeCategory'] = pd.cut(data['Age'], bins = [0, 30, 60, float('inf')], labels = ['young', 'seredni', 'old'])
survived_age = data[data['Survived'] == 1]['AgeCategory'].value_counts()

survived_age.plot(kind='bar', rot=0)
plt.title('Survived by age categories')
plt.xlabel('Category')
plt.ylabel('Survived')
plt.show()

sex = data[data['Survived'] == 1]['Sex'].value_counts()
sex.plot(kind='pie')
plt.title('Rozpodil by sex')
plt.show()


embarked = data['Embarked'].value_counts()
print(embarked.idxmax())

average_fare = data['Fare'].mean()
print(f"{average_fare:.2f}")

fare_by_class = data.groupby('Fare')['Pclass'].mean()
fare_by_class.plot(kind='bar', xlabel='Pclass', ylabel='Av. Fare', title='Negr')
plt.show()


print(data[data['Sex'] == 'male']['Fare'].mean())

fare_by_sex = data.groupby('Sex')['Fare'].mean()
fare_by_sex.plot(kind='bar', xlabel='Sex', ylabel='Av. Fare', title='Negr')
plt.show()