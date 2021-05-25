import matplotlib.pyplot as plt
import shelve
names = []
values = []
with shelve.open("data_base") as data:
    for keys, items in data.items():
        names.append(keys)
        values.append(items)

# print(names)
# print(values)
fig, ax = plt.subplots()
ax.plot(names, values)
ax.set_title('A single plot')
fig.show()