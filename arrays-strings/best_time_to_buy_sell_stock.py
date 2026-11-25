def max_profit(prices):
    min_price = float("inf")
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best

# Tests
print(max_profit([7, 1, 5, 3, 6, 4]))  # typical case, expect 5
print(max_profit([7, 6, 4, 3, 1]))     # edge case: prices only fall, expect 0