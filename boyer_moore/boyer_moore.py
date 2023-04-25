class Search:
    @staticmethod
    def full_scan(string: str, substring: str) -> int:
        t = 0
        while t <= (len(string) - len(substring)):
            m = 0
            while (m < len(substring)) and (string[t + m] == substring[m]):
                m += 1
            if m == len(substring):
                return t
            t += 1
        return -1

    @staticmethod
    def bmh(string: str, substring: str) -> int:
        shift = Search.create_shift(substring)
        t = 0
        while t <= (len(string) - len(substring)):
            m = len(substring) - 1
            while (m >= 0) and (string[t + m] == substring[m]):
                m -= 1
            if m < 0:
                return t
            t += shift[ord(string[t + len(substring) - 1])]
        return -1

    @staticmethod
    def create_shift(mask: str) -> list:
        shift = [len(mask)] * 128
        for m in range(len(mask) - 1):
            shift[ord(mask[m])] = len(mask) - m - 1
        return shift


if __name__ == '__main__':
    source_text = '000000000001010000000'
    search_text = '101'
    print('Полный перебор:', Search.full_scan(source_text, search_text))
    print('БМХ:', Search.bmh(source_text, search_text))
