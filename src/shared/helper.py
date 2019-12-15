from datetime import datetime


def get_now_timestamp():
    return datetime.now()


def get_value_from_dict(adict, key, default):
    return adict.get(key, default)


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
