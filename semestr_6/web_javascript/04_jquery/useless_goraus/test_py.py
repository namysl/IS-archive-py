
class test():
    __L = [0]
    __i = 0
    def __init__(self):
        print(test.__L)
        print(test.__i)
        test.__L[0] = test.__L[0]+1
        test.__i = test.__i + 1
        
