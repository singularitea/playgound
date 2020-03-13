import datetime as dt
import random

# generate reading data for sensor_data table
def generate_data(sensor_id,lower_limit,upper_limit,reading_amount):
    # time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time = dt.datetime.now() - dt.timedelta(seconds=reading_amount)
    data = random_float_between_range_rounded(lower_limit,upper_limit,2)
    return((time, sensor_id, data, "",))


# create a floting point number between two limits and round to input decimal places
def random_float_between_range_rounded(lower_limit,upper_limit,decimal_places):
    return round(random.uniform(lower_limit,upper_limit), decimal_places)
