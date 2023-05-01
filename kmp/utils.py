def get_left(s: str, d: int):
    return s[0: d]


def get_right(s: str, d: int):
    return s[len(s) - d: len(s)]
