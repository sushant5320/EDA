from collections import Counter
nums= [1,1,1,2,2,3]
k=2
# result = [x[0] for x in Counter(nums).most_common(k)]
# print(result)


print(Counter(nums).most_common(k))