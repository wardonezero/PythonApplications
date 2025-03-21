def book_ticket(destination, price, discount=0, *extras, **details):
    print(f"Booking to {destination} for ${price - discount}")
    if extras:
        print(f"Extras: {', '.join(extras)}")
    if details:
        print(f"Details: {details}")


# book_ticket("Paris", extras=["window seat", "meal"], discount=10, price=100)
book_ticket("Paris", 100, 10, "window seat", "meal")
book_ticket("Paris", 100, 10, "window seat", "meal", **{"name": "John"})
