def is_rhythmical(lst):
    if len(set(lst)) == 1:
        return "Парам пам-пам"
    return "Пам парам"

poem = input().split()

text = [sum(ch in 'аяуюоеёэ' for ch in phrase) for phrase in poem]

print(is_rhythmical(text))