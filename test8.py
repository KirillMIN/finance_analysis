import matplotlib.pyplot as pl
import shelve
with shelve.open("data_base") as data:
    pl.bar(data.keys(), data.values(), label='year')
    pl.show()