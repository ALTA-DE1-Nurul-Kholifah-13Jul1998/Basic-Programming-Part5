def muncul_sekali(angka):
    count_angka = {}
    hasil = []
    # print(con_angka)
    for i in angka:
        if i in count_angka:
            count_angka[i]+=1
        else:
            count_angka[i] = 1
    
    for j, count in count_angka.items():
        if count == 1:
            hasil.append(int(j))
    
    return hasil
        # if i not in list_hasil:
        #     # con_angka.remove(i)
        #     # print(con_angka)
        #     list_hasil.append(i) 


if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]