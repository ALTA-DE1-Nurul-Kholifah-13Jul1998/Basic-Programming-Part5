def pair_sum(arr, target):
    awal = 0
    akhir = len(arr) -1
    
    while awal <akhir:
        sum_target = arr[awal] + arr[akhir]
        if sum_target == target:
            return [awal, akhir]
        elif sum_target < target:
            awal+=1
        else:
            akhir-=1
    return None

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]