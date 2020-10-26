#Bella McCarter
#The Decade Quiz (A quiz that figures out which decade you'd thrive in)

username=input("What is your name? ")
def greeting(name):
    #greets and welcomes the quiz taker
    print("Hey, " + name + "! Welcome to the Decade Quiz!", sep= "")
greeting(username)

if input("Type Enter to start the quiz or type Cancel: ")==("Cancel"):
    print("Cancelling quiz...", end="")
else:
    print("How would you describe your fashion?\n")
    print("a. Tight fitting clothes are not your thing. You care less\n"
          "about fashion and instead what is comfortable and efficient to wear.\n")
    print("b. Bell bottom jeans, intricate patterns, and flower crowns.\n"
          "Any type of clothing that screams 'free spirit' is for you.\n")
    print("c. Minimalistic clothes, grunge outfits, or a hip hop vibe is\n"
          "how people would describe your style.\n")
    print("d. You like to wear something that draws attention while still\n"
          "being comfortable enough to party in. You'd find a patterned suit\n"
          "with a hat or a loose, sparkling dress with jewlery enticing.\n")
    print("e. You love the look of luxery. Something that draws attention in a \n"
          "way of having money. Whether you spring more towards a ball-gown and\n"
          "a fur coat, or a subtle but empowering suit; you spring nonetheless.\n")
    print("f. Leather jackets, band tees, and anything considered punk style is\n"
          "what you like.\n")
    print("g. You love the preppy vibe. Whether it be sweaters, vests, or mini skirts.\n")
    print("h. You want to make a bold statement but still look professional. You \n"
          "believe that what you wear indicates who you are and how you want people \n"
          "to percieve you.\n")
    answer_1 = input("Answer: ")
                        #https://vintagedancer.com/1940s/1940s-mens-fashion/
                        #https://www.crfashionbook.com/fashion/g27033975/
                        #fashion-staples-throughout-decade/?slide=6
if input("Type 'Go' to continue: ") == ("Go") or ("go"):
    print("Which artisits are you most likely to listen to?\n")
    print("a. Frank Sinatra or Rosemary Clooney\n")
    print("b. Queen or Billy Joel\n")
    print("c. Nirvana, Brittany Spears, or Backstreet Boys.\n")
    print("d. Louis Armstrong or Eddie Lang\n")
    print("e. Glen Miller or Billy Holiday\n")
    print("f. Bon Jovi or Michael Jackson\n")
    print("g. Beatles or Rolling Stones\n")
    print("h. Elvis Presley or Little Richard.\n")
    answer_2 = input("Answer: ")

                                #https://grammar.yourdictionary.com/slang/
                                #1970-s-slang.html

if input("Type 'Go' to continue: ") == ("Go") or ("go"):
    print("Which event would you most like to attend?\n")
    print("a. Doing something outdoors like hiking or\n"
          "playing sports.\n")
    print("b. Going to the disco.\n")
    print("c. Going clubbing in a somewhat modern bar.\n")
    print("d. Gambling and drinking at a vinatge speakeasy.\n")
    print("e. Going to see a musical at the theatre.\n")
    print("f. Spending the night rollerskating and dancing\n"
          "with friends.\n")
    print("g. Going to the drive in.\n")
    print("h. Going to a diner and dancing in a group to the\n"
          "jukebox.\n")
    answer_3 = input("Answer: ")

                                #https://medium.com/@Rifftime_Music/
                                #music-trends-through-the-decades-b8c5cbbae08b

if input("Type 'Go' to continue: ") == ("Go") or ("go"):
    print("Which slang phrase/word do you like the most?\n")
    print("a. 'Eager Beaver' - meaning 'enthusiastic'\n")
    print("b. 'Peace out, home fry' - meaning 'Goodbye'\n")
    print("c. 'Booyah' - meaning excitment\n")
    print("d. 'Meat Wagon' - meaning 'Ambulance'\n")
    print("e. 'Blow your wig' - meaning 'Get Excited'\n")
    print("f. 'Gnarly' - meaning 'Exciting'\n")
    print("g. 'Groovy' - meaning 'Cool'\n")
    print("h. 'Ankle-Biter' - mmeaning 'small child'\n")
    answer_4 = input("Answer: ")


answers = (answer_1, answer_2, answer_3, answer_4)

a =int(5)
b =int(10)
c =int(15)
d =int(20)
e =int(25)
f =int(30)
g =int(35)
h =int(40)

if answers == a:
    print(int(a))
elif answers == b:
    print(int(b))
elif answers == c:
    print(int(c))
elif answers == d:
    print(int(d))
elif answers == e:
    print(int(e))
elif answers == f:
    print(int(f))
elif answers == g:
    print(int(g))
elif answers == h:
    print(int(h))
else:
    print(" ")


total= ((answer_1)+(answer_2)+(answer_3)+(answer_4))

print("Total: ", (total * 1))

if (input("Type 'Go' to show the grading scale: ")) == ("Go") or ("go"):
    print("Grading Scale\n a = 5 \n b = 20 \n c = 35\n"
      " d = 50\n e = 65\n f = 80\n g = 95\n h = 110\n")

# A = 40's
# B = 70's
# C = 90's
# D = 20's
# E = 30's
# F = 80's
# G = 60's
# H = 50's

score = input("Please add up and enter score: ")

if score >= "20" and score <= "55":
    print("You would thrive in the 40s!")
    
if score >= "60" and score <= "100":
    print("You would thrive in the 70's!")
    
if score >= "105" and score <= "145":
    print("You would thrive in the 90's!")
    
if score >= "150" and score <= "190":
    print("You would thrive in the 20's!")
    
if score >= "195" and score <= "235":
    print("You would thrive in the 30's!")
    
if score >= "240" and score <= "280":
    print("You would thrive in the 80's!")
    
if score >= "285" and score <= "325":
    print("You would thrive in the 60's!")
    
if score in range(3) >= "330" and score <= "440":
    print("You would thrive in the 50's!")
    
if score < "20":
    print("Error")
