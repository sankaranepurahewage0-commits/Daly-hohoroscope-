from datetime import date

ZODIAC_SIGNS = {
    "1": "මේෂ",
    "2": "වෘෂභ",
    "3": "මිථුන",
    "4": "කටක",
    "5": "සිංහ",
    "6": "කන්‍යා",
    "7": "තුලා",
    "8": "වෘශ්චික",
    "9": "ධනු",
    "10": "මකර",
    "11": "කුම්භ",
    "12": "මීන"
}

MESSAGES = [
    "අද ඔබේ සැලසුම් පිළිබඳ නැවත සිතා බලන්න.",
    "වැදගත් තීරණ ගැනීමට පෙර හොඳින් විමසා බලන්න.",
    "පවුලේ අය සමඟ කාලය ගත කිරීමට සුදුසු දිනයකි.",
    "මුදල් වියදම් කිරීමේදී සැලකිලිමත් වන්න.",
    "අලුත් දෙයක් ඉගෙන ගැනීමට කාලය වෙන් කරන්න.",
    "අද ඔබේ සෞඛ්‍යය හා විවේකය ගැන සිතන්න."
]

def get_horoscope(sign, day=None):
    if day is None:
        day = date.today()
    sign = str(sign)
    if sign not in ZODIAC_SIGNS:
        return None
    index = (day.toordinal() + int(sign)) % len(MESSAGES)
    return f"{ZODIAC_SIGNS[sign]} ලග්නය: {MESSAGES[index]}"
