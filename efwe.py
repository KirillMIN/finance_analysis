import datetime


def clear_data_values():
    current_time = datetime.datetime.today().strftime("%m")
    return current_time

print(clear_data_values())