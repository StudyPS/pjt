import sys

word = {}

total_count = 0

while 1:
    text = sys.stdin.readline().strip()
    if text == "":
        break
    prev_count = word.get(text, 0)
    word[text] = prev_count + 1
    total_count += 1

sorted_dict = sorted(word.items())
for x, y in sorted_dict:
    print(f"{x} {y/total_count*100:.4f}")
