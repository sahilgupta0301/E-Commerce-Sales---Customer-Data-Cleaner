# E-Commerce Sales & Customer Data Cleaner

A Python-based data cleaning and reporting script designed to standardize raw e-commerce transaction records and generate key business metrics.

## Key Features
- **Data Cleaning & Standardization:** Trims extra whitespace (`.strip()`) and formats customer and product names into consistent Title Case (`.title()`).
- **Deduplication:** Uses Python `set` to identify and count unique customers automatically.
- **Type Casting & Aggregation:** Converts string prices into integers to compute total revenue and product-wise sales breakdowns using dictionaries.
- **Automated Reporting:** Identifies the top-performing product by revenue and outputs a clean summary report.

## Tech Stack
- **Language:** Python 3
- **Core Concepts:** Tuples, Sets, Dictionaries, String Manipulation, Loops, and Conditional Logic

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/sahilgupta0301/E-Commerce-Sales---Customer-Data-Cleaner.git
   ```
2. Run the script:
   ```bash
   python main.py
   ```
