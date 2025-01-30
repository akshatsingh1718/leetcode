"""
Product price: cost * (1 + margin)

If group size > 4 then reduce total products price by 20%

Var Product structure: [Product Name, Group, Cost]
And we want to decide

Var Category structure: [Cat name, cost start, cost end] 

Var Margin (dict) structure: {cat name: margin( in % or in range of 0-1) }
"""

# Data: List of products with [Product, Group, Cost]
products = [
    ["A", "G1", 20.1],
    ["B", "G2", 98.4],
    ["C", "G1", 49.7],
    ["D", "G3", 35.8],
    ["E", "G3", 105.5],
    ["F", "G1", 55.2],
    ["G", "G1", 12.7],
    ["H", "G3", 88.6],
    ["I", "G1", 5.2],
    ["J", "G2", 72.4],
]

# Category classification: [Category, Cost range from (inclusive), Cost range to (exclusive)]
category = [
    ["C3", 50, 75],
    ["C4", 75, 100],
    ["C2", 25, 50],
    ["C5", 100, None],
    ["C1", 0, 25],
]

# Margins for each category
margins = {"C1": "20%", "C2": "30%", "C3": "0.4", "C4": "50%", "C5": "0.6"}

"""
something * 20%

something * 20
--------------
100

something * 0.2
"""


# Function to determine category based on cost
def determine_category(cost: int, category: list) -> str:
    """
    category: [Cat name, cost start, cost end]
    Traverse over all the key val pairs in category to check
    that the cost falls in which category
    """
    result = ""
    for cat, start, end in category:
        if start <= cost and end is None:
            result = cat
            break

        if start <= cost < end:
            result = cat
            break

    return result


# Calculate average product price per group
from collections import defaultdict

group_prices = defaultdict(list)


# iterate over all the products
for product in products:
    pname, group, cost = product  # [Product Name, Group, Cost]

    # determine the catergory it falls in using category
    # example: C3, C4, ect
    product_category = determine_category(cost, category)

    # determine margin
    margin = margins[product_category]

    if "%" in margin:  # margin = "30%"
        margin_p = margin
        margin = margin.removesuffix("%")  # "30%" -> "30"
        margin = float(margin)  # "30" -> 30.0
        # print(f"{margin=} {margin/100}")
        margin /= 100  # 30.0 -> 0.3

    else:  # margin = "0.3"
        margin = float(margin)  # "0.3" -> 0.3
        margin_p = margin

    # Product price using given formula
    price = cost * (margin + 1)

    # group_prices["G1"].append(123)
    group_prices[group].append(price)

"""
Now till here
group_prices = {
"G1" : [price1, price2],
"G2" : [price2, price3, price4, price5, price6],
"G3" : [price7],
}
"""

# Calculate final group averages
result = dict()
for group_name, prices in group_prices.items():
    # apply mean formula to prices
    total_price = sum(prices)
    average_price = total_price / len(prices)

    # if the total prices are more than 4 reduce the avg price by 20%
    if len(prices) > 4:
        average_price *= 0.8  # Apply 20% discount
    print(
        f"{group_name=} ; {total_price=} {round(average_price, 1)=}  len={len(prices)}"
    )
    # round the prices to 1 decimal place
    result[group_name] = round(average_price, 1)


# Assertion
print(result)
assert result == {"G1": 37.5, "G2": 124.5, "G3": 116.1}, "It doesn't work"

print("It works!")
