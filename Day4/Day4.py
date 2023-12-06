import hashlib

done=False

i=0
while not done:
    i+=1
    inputToHash="bgvyzdsv"+str(i)
    print(inputToHash,end=" = ")
    result = hashlib.md5(inputToHash.encode())
    print(result.hexdigest())

    if result.hexdigest()[0:6] == "000000":
        done=True
