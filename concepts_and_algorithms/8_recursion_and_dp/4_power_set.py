from typing import List

def get_subsets(sets: List[set], index: int):
    if index == len(sets):
        return [set()]
    
    subsets = get_subsets(sets, index + 1)
    all_subsets = []
    item = sets[index]
    for subset in subsets:
        new_subset = set()
        [new_subset.add(elem) for elem in subset]
        new_subset.add(item)
        all_subsets.append(new_subset)
    all_subsets.extend(subsets)
    return all_subsets

print(get_subsets(['a1', 'a2', 'a3'], 0))
