from collections import Counter
from operator import itemgetter
def string_letter_count(s):
    cnt = Counter()
    for word in s.lower():
        if word == ' ':
            pass
        else:
            cnt[word] += 1
    cnt = dict(cnt)
    sorted_cnt = sorted(cnt.items(), key=itemgetter(0))
    reordered = [x[::-1] for x in sorted_cnt]
    print(reordered)

string_letter_count("This is a test sentence")
