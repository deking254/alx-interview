#!/usr/bin/python3
"""utf-8 encoding validation"""


def validUTF8(data):
    """
    returns true or false depending on the validity
    of the data utf8 encoding
    """
    try:
        b = bytes(data)
        try:
            b.decode('utf-8')
            return True
        except Exception
            return False
    except Exception:
        return False