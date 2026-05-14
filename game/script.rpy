
# character names
define arthur = Character("Arthur")
define buster = Character("Buster")

# main menu first
screen main_menu():
    tag menu

    add "gui/MainMenu.jpg":
        fit "cover"
        xalign 0.5
        yalign 0.5

    add "gui/ArthurTitle.png":
        xalign 0.5
        yalign 0.02

    add "gui/MagicalQuestText.png":
        xalign 0.5
        yalign 0.25

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.55

        frame:
            background "#FF0000"
            padding (4, 4)
            xalign 0.5

            frame:
                background "#000000"
                padding (100, 10)

                textbutton "PLAY":
                    action Start()
                    text_size 50
                    text_color "#FF0000"
                    xalign 0.5
                    yalign 0.5
        
        frame:
            background "#FF0000"
            padding (4, 4)
            xalign 0.5

            frame:
                background "#000000"
                padding (10, 10)

                textbutton "HOW TO PLAY":
                    action ShowMenu("how_to")
                    text_size 50
                    text_color "#FF0000"
                    xalign 0.5
                    yalign 0.5

        frame:
            background "#FF0000"
            padding (4, 4)
            xalign 0.5

            frame:
                background "#000000"
                padding (100, 10)
            
                textbutton "QUIT":
                    action Quit()
                    text_size 50
                    text_color "#FF0000"
                    xalign 0.5
                    yalign 0.5

screen how_to():

    add "gui/HowTo.jpeg" 
    textbutton "Back" action MainMenu()


# The game starts here.
label start:
    "Loading..."
    return



