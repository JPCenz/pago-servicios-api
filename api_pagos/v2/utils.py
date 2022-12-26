import datetime

def is_payment_expired(expiration_date:str):
    delta = expiration_date - datetime.date.today()
    if delta.days < 0:
        return delta.days < 0

