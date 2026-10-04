# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yinny", color="#FFFFFF")
define st = Character("Stormy", color="#6FA8DC")
define tr = Character("Trendy", color="#E06666")
define sp = Character("Sparky", color="#FFD966")
define sd = Character("Spendy", color="#93C47D")



default machine_progress = 0
default correct_tools = 0
default wrong_tools = 0
default teamwork = 0
default safety = 0

# The game starts here.

label start:
    scene bg StormyScene1
    with fade

    "Stormy sobs loudly as he runs away from his completed experiment."
    st "As always, I'm all alone." 
    st "I just wanted to show everyone my talent."

    scene bg Scene2
    with fade
    "He hops on the couch and cuddles with a strange new plushie"

    scene bg Scene3
    with fade

    st "But of course no one actually cares."
    "Stormy continues to cry himself to sleep"

    "ding dong, ding dong"

    scene bg Scene4

    st "wait who's here?"

    scene bg Scene5
    with fade

    st "I'm coming!"
    "Stormy wipes his tears and rushes to the door."

    st "Sniff sniff who's here"


    
    # This ends the game.
    return
