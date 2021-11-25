import pandas as pd

df = pd.read_csv('transactions.csv')

print("3 самых крупных платежа из реально проведённых:")
target_1 = df.loc[df['STATUS'] == 'OK'].SUM.sort_values()
print(target_1[-3:])

print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc:")
target_2 = df.loc[df['STATUS'] == 'OK'].loc[df['CONTRACTOR'] == 'Umbrella, Inc', 'SUM']
print(target_2.sum())
