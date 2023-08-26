from collections import OrderedDict
import re


def get_json_data(success: bool = True, error=None, message: str = None, result=None, *args, **kwargs):
    return OrderedDict([
        ('success', success),
        ('error', error),
        ('message', message),
        ('result', result)
    ])


def regex_phone(phone: str):
    return re.match("^\\+?998[012345789][0-9]{8}$", phone)
