try:
    num = int(input())
    print(num*4)
except (KeyboardInterrupt,ValueError,TypeError) as e:
    print("Number should be entered.....Program Terminated!!!")
#except ValueError:
#   print('Please check before you enter the datatype')
print("Bye raa")