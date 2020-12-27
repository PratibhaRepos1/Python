
emojifun = "🤪😘🙏"
#print(emojifun)

mystory = "He doesn't not like \"cheese\" in pizza.\nCan we go out for pizza?"
print(mystory)

#escape \n
filepath ="decuments\myfolder\\news"
print(filepath)

quote = "My friend doesn\'t like the word \"cheese\""
print(quote)

name = "Julie"

age = "42"

#sentence = ("Hi my name is {} and I am {} years old").format(name, age)
#sentence = "Hi my name is " + name + " and I am " + age + " years old"
sentence = "Hi my name is {} and I am {} years old".format(name, age)
print(sentence)

print(3 * "Apple")

print("Oranges" * 5)

tdfw = "turn down for what".replace("what","cheese").upper()
print(tdfw)

#index, characters and slicing
mystr = "Hello World"
#print(mystr[0])

lyric = """Can't stop, addicted to the shindig
Chop top, he says I'm gonna win big
Choose not a life of imitation
Distant cousin to the reservation
Defunct, the pistol that you pay for
This punk, the feeling that you stay for
In time, I want to be your best friend
Eastside love is living on the West End
Knock out, but boy you better come to
Don't die, you know the truth is some do
Go write your message on the pavement
Burn so bright, I wonder what the wave meant
White heat is screaming in the jungle
Complete the motion if you stumble
Go ask the dust for any answers
Come back strong with 50 belly dancers"""

print(lyric[-38:])

year = 1830 # When you check your solution, don't change this number
if year >= 2000 and year <= 2100:
    print("Welcome to the 21st century!")
else:
    print("You are before or after the 21st century")
