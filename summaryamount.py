#  PART A
1. Negative amounts are not rejected
2. rejected is hardcoded to 0
3. the except is bare






# PART B
def summarise_amounts(raw_values):
    total = 0
    rejected = 0
    for raw in raw_values:
        try:
            amount = int(raw)
        except ValueError:
            rejected += 1
            continue
        if amount < 0:
            rejected += 1
        else:
            total += amount
    return{"total": total, "rejected": rejected}



#  PART C
0 . assert summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]) == {"total": 15, "rejected": 3}

1.  assert summarise_amounts([]) == {"total": 0, "rejected": 0}
2.  assert summarise_amounts(["bad", "x", "-1", "1.5"]) == {"total": 0, "rejected": 4}
3.  assert summarise_amounts(["0"]) == {"total": 0, "rejected": 0}


explain:
1. Empty input
2. All rejected (unconvertible and negative)
3. alid zero must count toward total, not rejected