import datetime
import random
import string


def make_bin(params):
    if params['zero_ones']:
        return random.choice([1, 0])
    return random.choice([True, False])


def make_str(params):
    length = params['len']
    has_lower = params['has_lower']
    has_upper = params['has_upper']
    has_digit = params['has_digit']
    return ''.join(
        random.choices(
            string.ascii_uppercase*has_upper + string.ascii_lowercase*has_lower
            + has_digit*string.digits, k=length,
        ),
    )


def make_int(params):
    length = params['len']
    return random.randint(10**(length-1), 10**length)


def make_datetime(params):
    start_date = datetime.datetime.strptime(
        params['start_date'], params['format'],
    )
    end_date = datetime.datetime.strptime(params['end_date'], params['format'])
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date
