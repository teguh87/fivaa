def fivaa(rows):
    result = []
    temp = rows
    for i in range (temp, 0,-1):
        arr = []
        for j in range(0, i + 2):
            if j >= 2:
                arr.append(str(temp + 1))
            else:
                arr.append(str(temp - 1))
        temp = temp - 1
        result.append(''.join(arr))
    return '\n'.join(result)

if __name__=='__main__':
    rows = input("Enter number of rows ")
    rows = int (rows)
    print(fivaa(rows))

