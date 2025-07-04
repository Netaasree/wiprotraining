#raise [exception[,args[,traceback]]]
'''
try:
    num=11
    print(num)
    raise ValueError
except:
    print("Exception occured")
    
    #Traceback(Most recent calls)
'''    
    
    
try:
    raise NameError
except:
    print("Re-raising the exception")
    raise