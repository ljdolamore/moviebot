# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup", "yuh", "Yippee", "Yuh Huh"]:
            return True
        elif answer in ["n", "no", "nope", "Nah Dude"]:
            return False
   
def has_keyword(statement, keywords):
    statement = statement.lower()
    
    for word in keywords:
        word = word.lower()
        
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "You have an awful taste in film",
                 "Do you really think so?"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()

    questioning_words = ("Why", "Seriously?", "Are you sure about that?")
    movie_words = ["Good Will Hunting"]
    

    if has_keyword(statement, movie_words):
        response = "Good Choice"
    else:
        response = "That movie sucks"

    return response

def play():
    talking = True

    print("""  /     \
              vvvvvvv  /|__/|
                 I   /O,O   |
                 I /_____   |      /|/|
                J|/^ ^ ^ \  |    /00  |    _//|
                 |^ ^ ^ ^ |W|   |/^^\ |   /oo |
                  \m___m__|_|    \m_m_|   \mm_|
    Hello. I'm Movie Question Bot. I only ask what your favorite movie is.""")
    print("what is your favorite movie?")
    movie=input()
    
    
    while talking:
        statement = input(">> ")

        if statement == "Bai Doggy":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
