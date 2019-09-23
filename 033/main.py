from math import gcd

def intFromList(l):
  n = 0
  m = 1
  for i in range(len(l)-1, -1, -1):
    n += m * l[i]
    m *= 10
  return n

fractions = list()

for numerator in range(10, 100):
  for denominator in range(numerator+1, 100):
    actual = numerator / denominator
    a = numerator // 10
    b = numerator % 10
    c = denominator // 10
    d = denominator % 10
    if (b == 0 and d == 0) or (a == b and c == d) or (a != d and b != c):
      continue
    if (a == d and c != 0 and  actual == b/c):
      fractions.append((numerator, denominator))
      print('{0}/{1} == {2}/{3}'.format(numerator, denominator, a, c))
    if (b == c and d != 0 and actual == a/d):
      fractions.append((numerator, denominator))
      print('{0}/{1} == {2}/{3}'.format(numerator, denominator, a, c))

n_product = 1
d_product = 1
for f in fractions:
  print(f)
  n_product *= f[0]
  d_product *= f[1]

greatest_divisor = gcd(n_product, d_product)
final_denominator = d_product // greatest_divisor

print(final_denominator)

