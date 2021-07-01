with open('data.txt', 'r+') as f:
    data = 'some data to be written to the file'
    f.write(data)
    s = f.readlines()
    print(s)

