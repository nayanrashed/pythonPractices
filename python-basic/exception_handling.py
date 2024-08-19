def func(x):
    try:
        return 100/x
    except:
        return 'There is a zero correction error'
answer= func(1)
print(answer)