import pandas as pd
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].set_title('Ср. кол-во решенных задач по факульт. группам')
axs[1].set_title('Ср. кол-во решенных задач по группам по инф-ке')
fig.set_figwidth(11)
plt.subplots_adjust(wspace=0.2)

students_info = pd.read_excel('students_info.xlsx')
results_ejudge = pd.read_html("results_ejudge.html")

students_info = students_info[students_info['login'].notna()]
students_info.rename(columns={'login': 'User'}, inplace=True)
results_ejudge = results_ejudge[0]

group_faculty_names = students_info['group_faculty'].unique()
group_out_names = students_info['group_out'].unique()

all_data = pd.merge(students_info, results_ejudge, on='User')
faculty_data = all_data.groupby('group_faculty').mean()
group_data = all_data.groupby('group_out').mean()

for fac_name, group_name in zip(group_faculty_names, group_out_names):
    axs[0].bar(fac_name, faculty_data.loc[fac_name, 'Solved'], color='slateblue')
    axs[1].bar(group_name, group_data.loc[group_name, 'Solved'], color='darkslateblue')

plt.savefig('students.png')
required_data = all_data.loc[(all_data['G'] >= 10) | (all_data['H'] >= 10)]
print(required_data['group_faculty'].unique())
print(required_data['group_out'].unique())
