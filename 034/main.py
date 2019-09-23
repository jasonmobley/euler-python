import functools

@functools.lru_cache()
def fact(n):
  if (n <= 1):
    return 1
  return n * fact(n - 1)

for i in range(3, 100000000):
  digits = str(i)
  fact_sum = 0
  for d in digits:
    k = int(d)
    fact_sum += fact(k)
  if (i == fact_sum):
    print(i)

'''
for i in range(0, 10):
  print('{0}! = {1}'.format(i, fact(i)))

0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
'''

