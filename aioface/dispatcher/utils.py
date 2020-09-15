def check_full_text(fb_message, filter_message) -> bool:
    if filter_message is None or fb_message == filter_message or \
            fb_message in filter_message:
        return True
    return False


def check_contains(fb_contains, filter_contains) -> bool:
    if filter_contains is None:
        return True
    intersection = list(fb_contains & filter_contains)
    if len(intersection) == 0:
        return False
    return True


def check_payload(fb_payload, filter_payload) -> bool:
    if filter_payload is None or fb_payload == filter_payload or \
            fb_payload in filter_payload:
        return True
    return False
