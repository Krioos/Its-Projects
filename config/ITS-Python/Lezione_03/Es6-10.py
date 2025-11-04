numbers = {"jhon": [1,2,3,4,5],
            "Bob": [6,7,8,9,10]
}
for k,v in numbers.items():
    print(f"{k}:", end = " ")
    for i in range(len(v)):
        if i == len(v)-1:
            print(f"{v[i]}")
        else:
            print(f"{v[i]}", end = " ")