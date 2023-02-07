def normalize_time(t):
    if int(t) > 0:
        return f"{int(t)}s"
    units = [(1, 's'), (1000, 'ms'), (10**6, 'µs'), (10**9, 'ns')]
    i = 0
    while int((t - int(t)) * units[i][0]) <= 0 and i < len(units):
        i += 1
    return f"{int((t - int(t)) * units[i][0])}{units[i][1]}"


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ColorPrint:
    def print(self, text, color='', **kwargs):
        print(f"{color}{text}{Colors.ENDC}", **kwargs)
