def my_function(*args):
    print(args)
    print(type(args))
    print(args[0])
    print(args[1])

'''my_function(10)
my_function()'''
my_function(1,2,3)
my_function([1,2,3,5],4,5,8)