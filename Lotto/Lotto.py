import random as rdm

class Lotto:
    ATTEMPTS: int = 6
    RANGE: int = 45

    def __init__(self) -> None:
        self.attempts = Lotto.ATTEMPTS
        self.range = Lotto.RANGE

    def lotto_generation(self) -> list[int]:
        lottoZahlen: list[int] = []
        while len(lottoZahlen) < self.attempts:
            num: int = rdm.randint(1, self.range)
            if num not in lottoZahlen:
                lottoZahlen.append(num)
        return lottoZahlen
    
    def lotto_statistik(self, lotto: list[int], previos: dict) -> dict:
        stats: dict = previos.copy()
        for num in lotto:
            if num in stats:
                stats[num] += 1
        return stats