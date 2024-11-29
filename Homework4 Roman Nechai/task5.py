lst = [
    ['English', 'Russian', 'Belarusian'],
    ['English', 'German', 'French', 'Belarusian'],
    ['English', 'Chinese', 'Hindi', 'Belarusian']
]


def show_langs(langs):
    lang1 = lst[0]
    lang2 = lst[0]
    for i in lst[1:]:
        lang1 = set(lang1) | set(i)
        lang2 = set(lang2) & set(i)
    return len(lang1), lang1, len(lang2), lang2


languages = show_langs(lst)

for lang in languages:
    print(lang)
