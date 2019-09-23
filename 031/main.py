coins = [1, 2, 5, 10, 20, 50, 100, 200]

def combinations(coins, max_coin_idx, target_val):
  if max_coin_idx < 0 or max_coin_idx > len(coins):
    return 0
  if target_val == 0:
    return 1
  if target_val < 0:
    return 0
  if max_coin_idx <= 0 and target_val > 0:
    return 0
  return combinations(coins, max_coin_idx - 1, target_val) + combinations(coins, max_coin_idx, target_val - coins[max_coin_idx - 1])

print(combinations(sorted(coins), len(coins), 200))
