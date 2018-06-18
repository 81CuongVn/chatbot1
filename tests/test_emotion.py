from engine.hoaian import HoaiAn

Bot = HoaiAn


def tests():
    ANGRY = [
        "mẹ",
        "im đi"
    ]
    VULGARITY = [
        "mẹ mày",
        "như cứt",
        "dm"
    ]
    CURSE = [
        "đồ ngu",
        "kém quá",
        "bot ngu",
        "con bot ngu này",
        "ngu thật",
        "ngu vậy"
    ]
    COMPLIMENT = [
        "giỏi thật",
    ]
    COLLECTION = [
        ANGRY,
        VULGARITY,
        CURSE,
        COMPLIMENT
    ]

    # COLLECTION = [
    #     VULGARITY
    # ]

    messages = []
    for collection in COLLECTION:
        messages.extend(collection)
    for message in messages:
        print("You>", message)
        reply = Bot.reply("localuser", message)
        print("Bot>", reply)


if __name__ == '__main__':
    tests()