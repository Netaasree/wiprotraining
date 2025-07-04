# try:
#     print("Raising Exception")
#     raise ValueError
# finally:
#     print("performing clean-up")

try:
    print("Raising Exception")
    raise ValueError
except:
    print('Exception caught...')
finally:
    print("performing clean-up")
