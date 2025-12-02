products = {"Fruits":[("Apple", 15, 60), ("Banana", 10, 80)],
        "Vegetables":[("Cucumber", 30, 10), ("Tomato", 10, 50)]}

for category, items in products.items():
    print(f"{category}:")

    for item in items:
        name, quantity, price = item
        print(f"{name}: Count:{quantity}, Unite price:{price}")

m_exp = max(
    (item for sublist in products.values() for item in sublist), 
    key=lambda item_details: item_details[2]
)

m_cat = max(products, key=lambda category_name: len(products[category_name]))

all_sum = sum(
    price * count 
    for sublist in products.values() 
    for _, count, price in sublist
)


print(m_exp,",",m_cat,",",all_sum)
