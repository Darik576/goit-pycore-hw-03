import re


def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    if cleaned_number.startswith("+"):
        return cleaned_number

    if cleaned_number.startswith("380"):
        return "+" + cleaned_number

    return "+38" + cleaned_number


if __name__ == "__main__":
    phone_number = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
        "09546225564"
    ]

    sanitized_numbers = []

    for number in phone_number:
        sanitized_numbers.append(normalize_phone(number))

    print("Нормалізовані номери телефонів для SMS-розсилки:")
    print(sanitized_numbers)
