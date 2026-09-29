# PART A


# PART B
def reserve_stock(stock, order):
    remaining = stock.copy()

    for item, quantity in order:
        if item not in stock:
            raise ValueError(f"Unknown item: {item}")
        if quantity <= 0:
            raise ValueError(f"Quantity must be positive, got {quantity}")
        if quantity > remaining[item]:
            raise ValueError(f"Insufficient stock for {item}")
        remaining[item] = remaining[item] - quantity

    return remaining
    print()

# PART C
# 1. Successful reservation with repeated items
stock = {"pen": 5, "pencil": 10}
order = [("pen", 2), ("pen", 1)]
result = reserve_stock(stock, order)
assert result == {"pen": 2, "pencil": 10}
assert stock == {"pen": 5, "pencil": 10}          # original untouched

# 2. Repeated items exceeding stock (overselling)
stock = {"pen": 5}
order = [("pen", 3), ("pen", 3)]  # first line valid alone, combined total (6) exceeds 5
try:
    reserve_stock(stock, order)
    assert False, "Expected ValueError for overselling"
except ValueError:
    pass
assert stock == {"pen": 5}                        # original unchanged after failure

# 3. Unknown item
stock = {"pen": 5}
order = [("stapler", 1)]
try:
    reserve_stock(stock, order)
    assert False, "Expected ValueError for unknown item"
except ValueError:
    pass
assert stock == {"pen": 5}

# 4. Zero quantity
stock = {"pen": 5}
order = [("pen", 0)]
try:
    reserve_stock(stock, order)
    assert False, "Expected ValueError for zero quantity"
except ValueError:
    pass
assert stock == {"pen": 5}