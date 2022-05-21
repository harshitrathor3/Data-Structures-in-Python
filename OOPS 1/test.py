def scope_test():

    def local_():
        spam = 'local'
    
    def nonlocal_():
        nonlocal spam
        spam = 'nonlocal'
    def global_():
        global spam
        spam = 'global'
    
    spam = 'test spam'
    
    local_()
    print('Local : ', spam)
    nonlocal_()
    print('nonlocal : ', spam)
    global_()
    print('global : ', spam)

scope_test()
print(spam)