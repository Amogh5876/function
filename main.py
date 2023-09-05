def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}' .format(args[0],kwargs['food']))
myfunc(10,20,30,food ='eggs', animals='dog', sports= 'ricket')

