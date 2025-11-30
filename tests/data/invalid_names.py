VALID_NAME = "Oleh"

INVALID_NAMES = [
    None, "", "   ", 123, 12.34, True, [], {}, ("Chan",),
    "A", "J"*300, "Oleh123", "@Oleh!", "😀",
    "<script>alert(1)</script>",
    "Chan'); DROP TABLE bookings; --",
    " Chan", "Chan ", "\tChan", "Chan\n",
]

TEST_MATRIX = []

for inv in INVALID_NAMES:
    TEST_MATRIX.append((inv, VALID_NAME, f"invalid_firstname_{str(inv)[:10].strip().replace(' ', '_')}"))

for inv in INVALID_NAMES:
    TEST_MATRIX.append((VALID_NAME, inv, f"invalid_lastname_{str(inv)[:10].strip().replace(' ', '_')}"))
