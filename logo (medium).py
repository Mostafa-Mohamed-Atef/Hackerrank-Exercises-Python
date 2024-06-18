import collections
string = [i for i in input()]
counter = collections.Counter(string)
sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
[print(f"{x[0]} {x[1]}") for x in sorted_counter[:3]]