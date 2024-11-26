
def merge_sort(arr, lt):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], lt)
    right = merge_sort(arr[mid:], lt)
    return merge(left, right, lt)

def merge(arr1, arr2, lt):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if lt(arr1[i], arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < len(arr1):
        result.extend(arr1[i:])
    if j < len(arr2):
        result.extend(arr2[j:])
    return result

def calc_freq(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    return freq
    
items = [1,1,1,5,6,9,8,4,4,6]
items_with_freq = list(calc_freq(items).items())
sorted_items_with_freq = merge_sort(items_with_freq, lambda x, y: x[1] < y[1] or x[1] == y[1] and x[0] < y[0])
sorted_items = [item for item, freq in sorted_items_with_freq]
print(sorted_items)