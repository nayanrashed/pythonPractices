def func(x):
    try:
        return 100/x
    except:
        return 'There is zero division error'
answer= func(0)
print(answer)

