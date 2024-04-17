salesData = {}

with open("icecream.txt", "r") as data:
    total_sales_stores = {}
    for line in data:
        if ":" in line:
            parts = line.strip().split(":")
            flavor = parts[0]
            sales = [float(part) for part in parts[1:]]
            total_sales = sum(sales)
            
            # Menyimpan sales data dan total sales utk masing-masing flavor ice cream
            salesData[flavor] = {'sales': sales, 'total_sales': total_sales}
            
            # Menambahkan sales utk setiap store
            for index, sale in enumerate(sales):
                store = f"store{index+1}"
                if store in total_sales_stores:
                    total_sales_stores[store] += sale
                else:
                    total_sales_stores[store] = sale

# Menjumlahkan total sales utk masing-masing store di salesData
for store, total_sales in total_sales_stores.items():
    salesData[store] = {'total_sales': total_sales}

print(salesData)