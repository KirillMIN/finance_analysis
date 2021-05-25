import shelve
mini_data_structure = {}


def check_and_update_dict(category, money):
    if category not in mini_data_structure.keys():
        mini_data_structure.update({category: money})
    else:
        mini_data_structure[category] += money

