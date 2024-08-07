def return_check(check):

    if x == y:
        check = 1
        print (x,"is equal to ",y)
        return check
        exit(0)
    elif x > y:
        check = 2
        print (x, "is greater than",y)
        return check
        exit(0)
    else:
        check = 3
        print(x,"is less than", y)
        return check
        exit(0)

while True:
    try:
        x = input("Enter a number for x:")
        x = int(x)

        y = input("Enter a number for y:")
        y = int(y)

        check = 0
    except ValueError:
        print("Entry can not be String, enter only Number")
        continue
    return_check(check)
    #print(check)
    exit(0)


docker build -t vikas24775/python:ver3.3 .

docker run -it --rm vikas24775/python:ver3.3
