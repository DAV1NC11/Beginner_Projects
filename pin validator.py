def validate_pin(pin):
    return bool(len(pin) in (4, 6) and pin.isdigit())
validate_pin("123456")