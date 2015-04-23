example = "A cool way to do this."


def truncate(text, limit):
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


print(truncate(example, 12))


def truncate_smart(text, limit):
    if len(text) <= limit:
        return text

    if example[limit].isalpha():
        i = limit

        while i > 0 and example[i].isalpha():
            i -= 1
    c = i

    while c > 0 and not example[c - 1].isalpha():
        c -= 1

    return text[:c] + "..."


print(truncate_smart(example, 12))

e = "one. two. three. nice thing to blah."
f = e.rfind(".", 0, 12)
print(e[:f + 1])


