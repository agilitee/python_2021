import matplotlib.pyplot as plt
import numpy as np

groups = {}
preps = {}

with open("students.csv") as f:
    data = f.read().split("\n")

for string in data:
    prep, group, note = string.split(',')[0], int(string.split(',')[1]), int(string.split(',')[2])
    if prep in preps:
        if note in preps[prep]:
            preps[prep][note] += 1
        else:
            preps[prep][note] = 1
    else:
        preps[prep] = {note: 1}
    if group in groups:
        if note in groups[group]:
            groups[group][note] += 1
        else:
            groups[group][note] = 1
    else:
        groups[group] = {note: 1}

names_of_preps = list(preps.keys())
numbers_of_groups = list(groups.keys())
colors = {3: 'slateblue', 4: 'darkslateblue', 5: 'mediumslateblue', 6: 'mediumpurple', 7: 'rebeccapurple',
          8: 'blueviolet', 9: 'indigo', 10: 'darkorchid'}

fig, ax = plt.subplots()


def plot_one_bar_prep(one_prep):
    dict_notes = preps[one_prep]
    dict_notes = dict(sorted(dict_notes.items()))
    notes = dict_notes.keys()
    values = dict_notes.values()
    bath_padding = 0
    for one_note, one_value in zip(notes, values):
        plt.bar(one_prep, one_value, bottom=bath_padding, color=colors[one_note])
        bath_padding = np.add(bath_padding, one_value).tolist()


for this_prep in names_of_preps:
    plot_one_bar_prep(this_prep)
plt.title("Marks per prep")
plt.legend(["3", "4", "5", "6", "7", "8", "9", "10"])
plt.show()
plt.savefig('preps.png')


def plot_one_bar_group(one_group):
    dict_notes = groups[one_group]
    dict_notes = dict(sorted(dict_notes.items()))
    notes = dict_notes.keys()
    values = dict_notes.values()
    bath_padding = 0
    for one_note, one_value in zip(notes, values):
        plt.bar(one_group, one_value, bottom=bath_padding, color=colors[one_note])
        bath_padding = np.add(bath_padding, one_value).tolist()


for this_group in numbers_of_groups:
    plot_one_bar_group(this_group)
plt.title("Marks per group")
plt.legend(["3", "4", "5", "6", "7", "8", "9", "10"])
plt.show()
plt.savefig('groups.png')
