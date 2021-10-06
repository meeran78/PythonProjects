#String concatenation
# suppose we want to create a string that says "subscribe to _______"
# youtuber = "Meeran Mohideen" # some string variable

## a few days to do this
# print("Subscriber to " + youtuber)
# print("Subscriber to {}".format(youtuber))
# print(f""subscriber to {youtuber"})

adj = input("Adjective : ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)