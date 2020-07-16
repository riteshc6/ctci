from collections import defaultdict

def group_angrams(anagrams: list):
    grouped_anagrams  = []
    anagram_groups = defaultdict(list)

    for anagram in anagrams:
        key = sort_chars(anagram)
        anagram_groups[key].append(anagram)

    for anagram_group in anagram_groups.values():
        grouped_anagrams.extend(anagram_group)

    return grouped_anagrams

def sort_chars(string: str):
    return "".join(sorted(string))


anagrams = ["apple", "banana", "carrot", "ele", "duck", "papel", "tarroc", "cudk", "eel", "lee"]
print(anagrams)
print(group_angrams(anagrams))
