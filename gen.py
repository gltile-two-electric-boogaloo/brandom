import random

beginning = ["you're such a "] * 10 \
            + ["you're a "] * 10 \
            + ["you're my "] * 1 \
            + ["who's a "] * 10 \
            + ["who's my "] * 1 \
            + [""] * 50

end = [lambda: " " + ":" + ("3" * random.randint(1, 5))] \
    + [lambda: " " + "🥺" * random.randint(1, 20)] \
    + [lambda: "," * random.randint(1, 5)] \
    + [lambda: (" \\*pets you\\*" * random.randint(1, 5))[:-random.randint(4, 5)]]


def gen():
    return random.choice(beginning) + "good girl" + random.choice(end)()
