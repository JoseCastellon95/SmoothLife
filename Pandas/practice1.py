import pandas as pd
from tabulate import tabulate

column = ['Naruto','Ichigo','Goku']

titles_columns = {'Name':column,
				'Skills':['Rasengan','Getsuga Tenshou','Kamehameha'],
				'Features':['Ninja','Shinigami','Super Sayayin']	}

data = pd.DataFrame(titles_columns)


print(tabulate(data, showindex=False, headers=data.columns))

select_column = data['Skills']

#print(select_column)

#select_row = data.iloc[2]
#print(select_row)


data.to_csv('anime.csv', sep="\t")