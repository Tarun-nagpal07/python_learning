'''Read a CSV file of sales (date, product, quantity, price). Calculate total revenue per product
and find the best-selling product. Write a summary report CSV.'''

import csv

totals = {}  


with open("sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity * price

        if product not in totals:
            totals[product] = {"qty": 0, "revenue": 0.0}

        totals[product]["qty"] += quantity
        totals[product]["revenue"] += revenue

best_product = max(totals.items(), key=lambda x: x[1]["qty"])

print("Best Selling Product:", best_product[0])
print("Total Quantity Sold:", best_product[1]["qty"])

with open("summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Product", "TotalQty", "TotalRevenue"])

    for product, data in totals.items():
        writer.writerow([
            product,
            data["qty"],
            f"{data['revenue']:.2f}"
        ])

print("Summary report created successfully!")
