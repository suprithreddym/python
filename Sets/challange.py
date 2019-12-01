# text = input("please enter text")
# for i in text:
#     if i not in {'A', 'E', 'I', 'O', 'U'}:
#         print(i)

sampleText = "I LOVE YOU AMMA"

vowels = frozenset("aeiou")
finalset = set(sampleText).difference(vowels)
print(finalset)

finallist = sorted(finalset)

print(finallist)