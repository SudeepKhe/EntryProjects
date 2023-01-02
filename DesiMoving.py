welcome = "Welcome to Desi Moving and Labor"
print(welcome)
name = input('May I ask your name ')
nice= "Nice to meet you " + name 
print (nice)
movingdate= (input ("When is your expected moving date in DD/MM? "))
print (movingdate)
housing= int(input("Great " + name + ", now can you tell me how many guys you will require for your move? "))
print (housing)
if housing == 1: 
    print("For one guy it will be $50/hr with a two hour minimum \nWhen you are ready to book please call us directly at 732-200-2885, thanks")
elif housing == 2:
    print("For two guys it will be $80/hr with a two hour minimum \nWhen you are ready to book please call us directly at 732-200-2885, thanks")
else:
    print("Sorry we are only offering up to two men at this time\nThanks for inquiring and keep us in mind for future moving/labor assitance!")
   


   
    