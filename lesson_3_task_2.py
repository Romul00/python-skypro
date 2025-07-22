from smartphone import smartphone

catalog = [
    smartphone("Apple", "iPhone 13", "+79161234567"),
    smartphone("Samsung", "Galaxy S21", "+79261234567"),
    smartphone("Xiaomi", "Redmi Note 10", "+79361234567"),
    smartphone("Google", "Pixel 6", "+79461234567"),
    smartphone("OnePlus", "9 Pro", "+79561234567")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")