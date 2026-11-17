# 1. TUPLE: Raw data ko immutable list (tuple) me store kiya
raw_records = ("  sahil gupta , laptop , 55000 ", "rohan sharma, MOBILE , 20000",
               "  Sahil Gupta , mouse , 1500 ","priya singh , LAPTOP , 55000" ,
               "amit verma, mobile, 20000")

# 2. SET: Duplicate customers ko hatane ke liye empty set banaya
unique_customers = set()

# 3. INTEGER VARIABLE: Total kamai jodne ke liye counter variable
total_revenue = 0

# 4. DICTIONARY: Product-wise total sales (Key: Product, Value: Total Price) store karne ke liye
product_sales = {}

# 5. FOR LOOP: Har ek record ko ek-ek karke process karne ke liye
for record in raw_records:
    # STRING SPLIT: Comma (,) ke base par string ko tod kar list banayi
    parts = record.split(",")
    # STRING CLEANING (.strip() & .title()): Extra spaces hataye aur proper case me badla
    customer_name = parts[0].strip().title()
    product_name = parts[1].strip().title()
    # TYPE CASTING (int()): String price ko math calculation ke liye number me badla
    price = int(parts[2].strip())
    
    # SET METHOD (.add()): Customer ka naam set me dala (duplicates apne aap ignore honge)
    unique_customers.add(customer_name)
    # ASSIGNMENT OPERATOR (+=): Purane total_revenue me naya price joda
    total_revenue += price
    # 6. IF-ELSE CONDITION (Dictionary Update):
    # Check kiya ki product pehle se dictionary me hai ya nahi
    if product_name in product_sales:
        product_sales[product_name] += price    # Agar hai, toh purani sales me naya price joda
    else:
        product_sales[product_name] = price     # Agar nahi hai, toh nayi entry banayi
    # F-STRING PRINT: Har customer ka clean record print kiya
    print(f"Customer: {customer_name},\nProduct: {product_name},\nPrice: {price}")

# 7. FINAL REPORT (Loop ke bahar - sirf ek baar chalega):
# len() function se unique customers ki total ginti nikali
print(f"Unique Customers: {len(unique_customers)}")
print(f"Total Revenue: {total_revenue}")
# MAX() FUNCTION: Dictionary me sabse zyada sales (value) wale product ka naam nikala
top_product = max(product_sales, key=product_sales.get)
print(f"Product-wise Sales: {product_sales}")
print(f"Top Selling Product: {top_product} ({product_sales[top_product]})")