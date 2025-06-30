#random - generate numbers,random choices
import random
#from random import randint
print("Random number from 10 to 50 ",random.randint(10,50))
#random.random(dynamicall used)
print("Rnadom number from 0 to 1",random.random())
print("Random number from 1.5 to5.5 ", random.uniform(1.5,5.5))
#fruit
fruits = ['banana','apple','mango','pineapple']
print("Random choice from list", random.choice(fruits))
print("Random choice from list", random.choice(fruits))

num=[1,2,3,4,5]
print(num)
print("Shuffled list",random.shuffle(num))
print(num)


print(random.randint(1,100))
random.seed(16)
print(random.randint(1,100))