import pandas as pd
import random
from faker import Faker
import re
from datetime import timedelta
fake = Faker()
customer_registry  = {}

item_category_pairs = {
    # Phones
    "Samsung A7": "Phones",
    "iPhone 13": "Phones",
    "Xiaomi Redmi Note 12": "Phones",
    "Oppo A78": "Phones",
    "Vivo V27": "Phones",
    "Realme 11 Pro": "Phones",
    "iPhone SE 2022": "Phones",
    "Samsung Galaxy S23": "Phones",
    "Infinix Note 12": "Phones",
    "Asus ROG Phone 7": "Phones",

    # Laptops
    "MacBook Air M2": "Laptops",
    "Dell XPS 13 Plus": "Laptops",
    "Asus ROG Flow Z13": "Laptops",
    "Lenovo Yoga 7i": "Laptops",
    "HP Spectre x360": "Laptops",
    "MSI Stealth 15M": "Laptops",
    "Acer Swift 3": "Laptops",
    "Microsoft Surface Laptop 5": "Laptops",
    "Huawei MateBook D15": "Laptops",
    "Samsung Galaxy Book 3": "Laptops",

    # Books
    "Harry Potter and the Philosopher's Stone": "Books",
    "Atomic Habits": "Books",
    "Sapiens": "Books",
    "Deep Work": "Books",
    "Clean Architecture": "Books",
    "The Pragmatic Programmer": "Books",
    "Rich Dad Poor Dad": "Books",
    "The Lean Startup": "Books",
    "The Psychology of Money": "Books",
    "Start With Why": "Books",

    # Clothing
    "Nike Sports T-Shirt": "Clothing",
    "Levi's Denim Jacket": "Clothing",
    "Uniqlo Airism Shirt": "Clothing",
    "H&M Hoodie": "Clothing",
    "Zara Chinos": "Clothing",
    "Adidas Track Pants": "Clothing",
    "Polo Ralph Lauren Shirt": "Clothing",
    "Pull&Bear Jacket": "Clothing",
    "Cotton On Jeans": "Clothing",
    "Erigo Oversized Tee": "Clothing",

    # Shoes
    "Adidas Ultraboost": "Shoes",
    "New Balance 574": "Shoes",
    "Converse Chuck 70": "Shoes",
    "Puma RS-X": "Shoes",
    "Reebok Club C": "Shoes",
    "Nike Air Force 1": "Shoes",
    "Vans Old Skool": "Shoes",
    "Asics Gel Kayano": "Shoes",
    "Skechers D'Lites": "Shoes",
    "Fila Disruptor II": "Shoes",

    # Beauty
    "Maybelline Fit Me Foundation": "Beauty",
    "The Ordinary Niacinamide": "Beauty",
    "L'Oreal Revitalift Serum": "Beauty",
    "Wardah Intense Matte Lipstick": "Beauty",
    "Somethinc Niacinamide Moisture": "Beauty",
    "Emina Bright Stuff Moisturizer": "Beauty",
    "Avoskin Miraculous Toner": "Beauty",
    "Skintific Mugwort Clay Mask": "Beauty",
    "Scarlett Whitening Body Lotion": "Beauty",
    "Pixy UV Whitening BB Cream": "Beauty",

    # Toys
    "Lego Star Wars Set": "Toys",
    "Hot Wheels Twin Pack": "Toys",
    "Barbie Dreamtopia Doll": "Toys",
    "Nerf Elite 2.0 Blaster": "Toys",
    "Rubik's Cube 3x3": "Toys",
    "Play-Doh Kitchen Set": "Toys",
    "Monopoly Board Game": "Toys",
    "Beyblade Burst Turbo": "Toys",
    "Jenga Classic": "Toys",
    "RC Car Off-Road 4WD": "Toys",

    # Electronics
    "Samsung 55\" QLED TV": "Electronics",
    "Panasonic Rice Cooker 1.8L": "Electronics",
    "LG Smart TV 43\"": "Electronics",
    "Sharp Microwave 25L": "Electronics",
    "JBL Soundbar 2.1": "Electronics",
    "Philips Air Fryer XL": "Electronics",
    "Xiaomi Air Purifier 4": "Electronics",
    "Polytron Bluetooth Speaker": "Electronics",
    "Mito Blender 2 in 1": "Electronics",
    "Toshiba Water Dispenser": "Electronics",

    # Computer Accessories
    "Sony WH-1000XM6": "Computer Accessories",
    "Logitech MX Master 3S": "Computer Accessories",
    "Razer BlackWidow V4 Pro": "Computer Accessories",
    "HyperX Cloud II": "Computer Accessories",
    "SteelSeries Aerox 3": "Computer Accessories",
    "Logitech K380 Wireless": "Computer Accessories",
    "Corsair K95 RGB Platinum": "Computer Accessories",
    "Asus ROG Gladius III": "Computer Accessories",
    "Keychron K6 Wireless": "Computer Accessories",
    "Anker Soundcore Life Q35": "Computer Accessories"
}

payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash']
shipping_status_pool = ["shipped", "in transit", "delivered", "returned", "done"]

unique_phone_number = []
unique_email = []

def generate_phone_number():
    for i in range(20):
        prefix = "+62"
        number = "8" + "".join([str(random.randint(0, 9)) for _ in range(random.choice([9, 10]))])
        if number not in unique_phone_number:
            unique_phone_number.append(number)
            return f"{prefix}{number}"
        else:
            continue
    return ""

def generate_email(customer_name):
    name = " ".join(re.findall("[a-zA-Z]+", customer_name))
    name = name.lower()
    for i in range(20):
        prefix_email = name + "".join([str(random.randint(0, 9)) for _ in range(random.choice([1, 4]))])
        new_email = f"{prefix_email}@example.com"
        if new_email not in unique_email:
            unique_email.append(new_email)
            return new_email
        else:
            continue
    prefix_email = name + "".join([str(random.randint(0, 9)) for _ in range(random.choice([1, 4]))])
    new_email = f"{prefix_email}@trinity.com"
    if new_email not in unique_email:
        unique_email.append(new_email)
        return new_email
    else:
        new_email = f"{name}@example.com"
        if new_email not in unique_email:
            unique_email.append(new_email)
            return new_email
    return ""

def get_or_create_customer():
    key = random.randint(1, 3000)
    if key not in customer_registry:
        name = fake.name()
        customer_registry[key] = {
            "member_id": key,
            "customer": name,
            "email": generate_email(name),
            "phone": generate_phone_number()
        }
    else:
        name = customer_registry[key]['customer']
        if random.random() < 0.3:
            email = generate_email(name)
            customer_registry[key]['email'] = email
        if random.random() < 0.3:
            customer_registry[key]['phone'] = generate_phone_number()
    return customer_registry[key]

def generate_transaction(order_id):
    customer = get_or_create_customer()
    n_items = random.randint(1, 8)
    date = fake.date_time_between(start_date='-15d', end_date='now')
    payment = random.choice(payment_methods)
    address = fake.address().replace("\n", ", ")
    status_type = random.choices(["all_done", "done_and_returned", "mixed", "all_cancelled"], weights=[0.2, 0.2, 0.6, 0.1])[0]

    rows = []

    for _ in range(n_items):
        item = random.choice(list(item_category_pairs.keys()))
        category = item_category_pairs[item]
        quantity = random.randint(1, 5)
        price = round(random.uniform(10.0, 2000.0), 2)
        discount = random.choice([0, 0.05, 0.1, 0.15])
        net = round(price * quantity * (1 - discount), 2)
        shipping_cost = round(random.uniform(0, 20), 2)

        if status_type == "all_done":
            updated_at = fake.date_time_between(start_date=date + timedelta(days=7), end_date='now')
            shipping_status = "done"
        elif status_type == "done_and_returned":
            updated_at = fake.date_time_between(start_date=date + timedelta(days=7), end_date='now')
            shipping_status = random.choice(["done", "returned"])
        elif status_type == "all_cancelled":
            updated_at = fake.date_time_between(start_date=date, end_date=date + timedelta(hours=3))
            shipping_status = "cancelled"
        else:
            updated_at = fake.date_time_between(start_date=date + timedelta(days=1), end_date='now')
            shipping_status = random.choice(shipping_status_pool)

        row = {
            "order_id": order_id,
            "date": date,
            "customer": customer["customer"],
            "member_id": customer["member_id"],
            "items": item,
            "quantity": quantity,
            "price": price,
            "net": net,
            "email": customer["email"],
            "phone number": customer["phone"],
            "category": category,
            "payment method": payment,
            "shipping_address": address,
            "shipping cost": shipping_cost,
            "shipping status": shipping_status,
            "discount": discount,
            "updated_at": updated_at
        }

        rows.append(row)

    return rows

def generate_dataset(num_rows, output_path):
    all_rows = []
    for i in range(1, num_rows + 1):
        all_rows.extend(generate_transaction(i))

    df = pd.DataFrame(all_rows)
    df.to_csv(output_path, index=False)