def join_array_remove_duplicate(arrayA, arrayB):
    def remove_duplicate(array):
        hasil = []
        for i in array:
            if i not in hasil:
                hasil.append(i)
        return hasil
    
    arrayA = remove_duplicate(arrayA)
    arrayB = remove_duplicate(arrayB)
    
    for i in arrayA:
        if i in arrayB:
            arrayB.remove(i)
    hasil  = arrayA + arrayB
    return hasil
    
    
        

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
