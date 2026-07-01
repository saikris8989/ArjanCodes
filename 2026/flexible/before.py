from typing import Any


def create_booking(data: dict[str, Any], **kwargs: Any) -> None:
    if data["status"] == "cancelled":
        raise ValueError("Flight cancelled")

    discount = 0.10 if data.get("loyalty") else 0
    total = data["price"] * (1 - discount)

    print(
        f"Booked {data['flight_number']} "
        f"for {data['passenger_name']} "
        f"at €{total} "
        f"in seat {kwargs.get('seat', 'standard')}"
    )


def main() -> None:

    booking = {
        "passenger_name": "Ada",
        "flight_number": "AC123",
        "price": 250,
        "status": "scheduled",
        "loyalty": True,
    }

    create_booking(
        booking,
        seat="extra_legroom",
    )


if __name__ == "__main__":
    main()
