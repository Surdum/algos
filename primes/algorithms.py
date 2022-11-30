from base import AlgoBase


class PrimeNumbersCount(AlgoBase):
    description = 'Prime numbers count'

    def prepare_args(self, n: str):
        return [int(n)]

    def run(self, n: int):
        if n == 1:
            return 0
        if n == 2:
            return 1
        primes = [2]
        sqrt_n = n**0.5
        for i in range(3, n+1, 2):
            is_prime = True
            j = 0
            while j < len(primes) and primes[j] < sqrt_n:
                if i % primes[j] == 0:
                    is_prime = False
                    break
                j += 1
            if is_prime:
                primes.append(i)
        return len(primes)


class SieveOfEratosthenes(AlgoBase):
    description = 'Sieve of Eratosthenes'

    def prepare_args(self, n: str):
        return [int(n)]

    def run(self, n: int):
        if n == 1:
            return 0
        numbers = list(range(n+1))
        numbers[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if numbers[i] != 0:
                j = i * i
                for k in range(j, n+1, i):
                    numbers[k] = 0
        c = 0
        for elem in numbers:
            if elem != 0:
                c += 1
        return c


if __name__ == '__main__':
    prime_counter = PrimeNumbersCount()
    print(prime_counter.run(10))
    print(prime_counter.run(50))
    print(prime_counter.run(100))

    erat = SieveOfEratosthenes()
    print(erat.run(10))
    print(erat.run(50))
    print(erat.run(100))

