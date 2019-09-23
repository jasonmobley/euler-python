def intFromList(l):
  n = 0
  m = 1
  for i in range(len(l)-1, -1, -1):
    n += m * l[i]
    m *= 10
  return n

digits = [1,2,3,4,5,6,7,8,9]

def next_permutation(digits):
  length = len(digits)
  i = length - 2
  j = length - 1

  while i >= 0:
    if digits[i] < digits[i+1]:
      break
    i -= 1
  
  if i < 0:
    return False

  while j > i:
    if digits[j] > digits[i]:
      tmp = digits[i]
      digits[i] = digits[j]
      digits[j] = tmp
      break
    j -= 1
  
  i += 1
  j = length - 1
  while j > i:
    tmp = digits[i]
    digits[i] = digits[j]
    digits[j] = tmp
    i += 1
    j -= 1

  return True

def digit_permutations(n):
  digits = list(range(1, n + 1))
  more_permutations = True
  while more_permutations:
    yield digits
    more_permutations = next_permutation(digits)

def is_pandig_product(digits, i, j):
  n = intFromList(digits[0:i])
  m = intFromList(digits[i:j])
  p = intFromList(digits[j:])
  if n == 1 or m == 1:
    return None
  if n * m == p:
    return (n, m, p)
  return None

pandigital_products = set()
for perm in digit_permutations(9):
  pandig_1_4 = is_pandig_product(perm, 1, 4)
  if pandig_1_4:
    pandigital_products.add(pandig_1_4[2])
  pandig_1_5 = is_pandig_product(perm, 1, 5)
  if pandig_1_5:
    pandigital_products.add(pandig_1_5[2])
  pandig_2_5 = is_pandig_product(perm, 2, 5)
  if pandig_2_5:
    pandigital_products.add(pandig_2_5[2])
  pandig_3_4 = is_pandig_product(perm, 3, 4)
  if pandig_3_4:
    pandigital_products.add(pandig_3_4[2])
  pandig_3_5 = is_pandig_product(perm, 3, 5)
  if pandig_3_5:
    pandigital_products.add(pandig_3_5[2])
  pandig_4_5 = is_pandig_product(perm, 4, 5)
  if pandig_4_5:
    pandigital_products.add(pandig_4_5[2])
print(pandigital_products)
print(sum(pandigital_products))

