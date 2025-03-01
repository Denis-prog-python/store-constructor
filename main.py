class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин '{self.name}'.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

store1 = Store("Продуктовый рай", "ул. Ленина, 10")
store2 = Store("ТехноМир", "пр. Мира, 25")
store3 = Store("Модный стиль", "ул. Пушкина, 15")

store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("хлеб", 1.0)

store2.add_item("ноутбук", 50000)
store2.add_item("смартфон", 30000)
store2.add_item("наушники", 5000)

store3.add_item("футболка", 1500)
store3.add_item("джинсы", 3000)
store3.add_item("куртка", 7000)

print(store1)
print(store2)
print(store3)

print(f"Цена яблок в магазине '{store1.name}': {store1.get_item_price('яблоки')}")
print(f"Цена ноутбука в магазине '{store2.name}': {store2.get_item_price('ноутбук')}")
print(f"Цена футболки в магазине '{store3.name}': {store3.get_item_price('футболка')}")

store1.update_item_price("яблоки", 0.6)
store2.update_item_price("смартфон", 28000)

store3.remove_item("куртка")

print(store1)
print(store2)
print(store3)