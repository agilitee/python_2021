import pandas as pd
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].set_title('Количество полетов')
axs[1].set_title('Общая перевезенная масса')
axs[2].set_title('Общая стоимость перевезенных товаров')
fig.set_figwidth(12)
plt.subplots_adjust(wspace=0.5)

df = pd.read_csv('flights.csv', index_col=0)

names = df['CARGO'].unique()
for name in names:
    select_flights = df[df['CARGO'] == name]
    number_of_flights = len(select_flights)
    weight, price = select_flights['WEIGHT'].sum(), select_flights['PRICE'].sum()
    axs[0].bar(name, number_of_flights, color='slateblue')
    axs[1].bar(name, weight, color='darkslateblue')
    axs[2].bar(name, price, color='mediumslateblue')

plt.savefig('flights.png')
