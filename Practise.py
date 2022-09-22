#Detailing start call
from re import L
from statistics import median


response = input("How are you Dr ?")
print(response)
def call():
    if response == "Good":
        print("Wonderful doc, I would like to interest you with in a few of our products")
    elif response == "Tired":
        print("That is perfectly fine doc, we try another day")
call()
fabutas = "Then Dr, Intas has the right product, that is Fabutas. Fabutas, our febixostat generic is well indicated for the treatment of hyperuricemia and also life-long therapy of gout"
need = input("How common is hyperuricemia in your practise? ")
losartas = "If that is the case,  then I will stick to a time tested sartan, losartan under the brand name losartas and for combined therapy we offer it losartas HT containg 12.5mg of hydrochlorothiazide for improved management of hypertension"
def detail():
    if need == "Commonly":
        print(fabutas)
    elif need == "Rarely":
        print(losartas)
detail()        
 #New year greetings
colleagues = ("Moses", "Erastus", "Dylan", "Gilbert", "Domminic")
def tidings(x):
    for a in x:
        print(a + " May this new season bring you nohing short of great growth")   
workforce = [input("List of all members of the human resource ")]
workforce = list(workforce)
tidings(workforce)
# hypertension detection
dp = input("bp read")
dp =  int(dp)
def diag (bp):
    if bp == 120:
        print("Prehyeprtensive")
    elif bp == range(121, 129)    :
        print("hypertensive")
    elif bp > 130:
        print("hypertensive crisis")    
diag(dp)   
num_1 = [19,29,18,37,1762]
r = (median(num_1))
print(r)
largest = -1
for i in [19,29,18,37,1762]:
    if i > largest:
        largest= i
        print(largest)   






     
