from Lotto import Lotto

first = Lotto()
print(first.lotto_generation())


stats = {i: 0 for i in range(46)}


for i in range(1000):

    lotto_numbers = first.lotto_generation()
    stats = first.lotto_statistik(lotto_numbers, stats)

print(stats)