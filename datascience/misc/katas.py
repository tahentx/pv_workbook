def string_letter_count(s):
    from collections import Counter
    from operator import itemgetter
    cnt = Counter()
    for word in s.lower():
        if word == ' ':
            pass
        else:
            cnt[word] += 1
    cnt = dict(cnt)
    sorted_cnt = sorted(cnt.items(), key=itemgetter(0))
    reordered = [x[::-1] for x in sorted_cnt]
    t = []
    for x in reordered:
        f = str(x[0])
        t.append(f)
        t.append(x[1])
    answer = ''.join(t)
    return answer

string_letter_count("This is a test sentence")
