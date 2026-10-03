# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define t = Character("Trendy", color="#c8ffc8")
default test = "hi my name is trendy!"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show trendy

    # These display lines of dialogue.

    t test

    e "I need you to help me pleaaaaase!"

    show eileen happy

    e "okay okay what is it? I'm tired"

    # This ends the game.

    return
