import math
from collections import defaultdict

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

# Margins for each category
margins = {"C1": "20%", "C2": "30%", "C3": "0.4", "C4": "50%", "C5": "0.6"}


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


# Function to calculate price with margin
def calculate_price(cost, margin):
    if "%" in margin:  # margin = "30%"
        margin_value = float(margin.removesuffix("%")) / 100
        return cost * (1 + margin_value)
    else:  # margin = "0.3"
        return cost * (1 + float(margin))


# Rounding function
def round_to_1_decimal(value):
    return math.floor(value * 10 + 0.5) / 10  # Same as Java's Math.round()


# Group products and calculate average price per group
group_prices = defaultdict(list)

for product in products:
    prod_name, group, cost = product  # [Product Name, Group, Cost]

    # Determine the category it falls into
    product_category = determine_category(cost, category)

    # Determine margin
    margin = margins[product_category]

    # Calculate the price using margin
    price = calculate_price(cost, margin)

    print(f"==> {cost} ; {product_category} ; {margin} ; {price}")

    group_prices[group].append(price)

# Calculate the final group averages
result = dict()
for group_name, prices in group_prices.items():
    # Apply mean formula
    average_price = sum(prices) / len(prices)

    # Apply 20% discount if more than 4 products in group
    if len(prices) > 4:
        average_price *= 0.8

    # Round to 1 decimal place
    result[group_name] = round_to_1_decimal(average_price)

# Print final results
print(result)
