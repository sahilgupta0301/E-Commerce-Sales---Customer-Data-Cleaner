# 1. TUPLE: Store raw sales data in an immutable sequence
raw_records = ("  sahil gupta , laptop , 55000 ", "rohan sharma, MOBILE , 20000",
               "  Sahil Gupta , mouse , 1500 ","priya singh , LAPTOP , 55000" ,
               "amit verma, mobile, 20000")

# 2. SET: Initialize an empty set to store unique customer names and avoid duplicates
unique_customers = set()

# 3. INTEGER VARIABLE: Counter variable to accumulate total revenue
total_revenue = 0

# 4. DICTIONARY: Store product-wise total sales (Key: Product, Value: Total Price)
product_sales = {}

# 5. FOR LOOP: Process each raw record one by one
for record in raw_records:
     # STRING SPLIT: Split the string by comma (,) into a list of fields
    parts = record.split(",")
    # STRING CLEANING (.strip() & .title()): Remove extra whitespace and standardize to title case
    customer_name = parts[0].strip().title()
    product_name = parts[1].strip().title()
    # TYPE CASTING (int()): Convert the string price into an integer for calculations
    price = int(parts[2].strip())
    
   # SET METHOD (.add()): Add customer name to the set (duplicates are automatically ignored)
    unique_customers.add(customer_name)
    # ASSIGNMENT OPERATOR (+=): Add the current item price to total_revenue
    total_revenue += price
    # 6. IF-ELSE CONDITION (Dictionary Update):
    # Check if the product already exists in the dictionary
    if product_name in product_sales:
        product_sales[product_name] += price    # Add price to existing product sales
    else:
        product_sales[product_name] = price      # Create a new entry for the product
     # F-STRING PRINT: Output the cleaned record for each transaction
    print(f"Customer: {customer_name},\nProduct: {product_name},\nPrice: {price}")

# 7. FINAL REPORT (Runs once after the loop completes):
# Use len() to count total unique customers
print(f"Unique Customers: {len(unique_customers)}")
print(f"Total Revenue: {total_revenue}")
# MAX() FUNCTION: Find the product with the highest total sales value in the dictionary
top_product = max(product_sales, key=product_sales.get)
print(f"Product-wise Sales: {product_sales}")
print(f"Top Selling Product: {top_product} ({product_sales[top_product]})")