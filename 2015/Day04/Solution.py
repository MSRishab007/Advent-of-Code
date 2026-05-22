import hashlib
with open("2015/Day04/input.txt") as file:
    data = file.read().strip()
    for i in range(0,1000000):
        hash = hashlib.md5((data+str(i)).encode()).hexdigest()
        if hash.startswith("00000"):
            print("First Answer:", i)
            break
    for i in range(0,100000000):
        hash = hashlib.md5((data+str(i)).encode()).hexdigest()
        if hash.startswith("000000"):
            print("Second Answer:", i)
            break