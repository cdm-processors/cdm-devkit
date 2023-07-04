label_counter = 0


def get_label() -> str:
    global label_counter

    label = f"L{label_counter}"
    label_counter += 1
    return label
