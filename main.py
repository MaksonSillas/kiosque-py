from management import product_handler
from management import tab_handler
from menu import products

if __name__ == "__main__":
    # print(product_handler.get_product_by_id("28"))
    # print(product_handler.get_products_by_type("drink"))
    product_handler.menu_report()
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    
    # print(product_handler.add_product(products, **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    # print(tab_handler.calculate_tab(table_2))
    ...
