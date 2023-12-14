def clean_phone_number(phone_number):
    return phone_number.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
