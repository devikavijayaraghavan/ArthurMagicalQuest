
# character names
define arthur = Character("Arthur")
define buster = Character("Buster")

# main menu first
screen main_menu():
    tag menu

    # main menu background image
    add "gui/MainMenu.jpg":
        fit "cover"
        xalign 0.5
        yalign 0.5

    # main menu "Arthur" text + alignment
    add "gui/ArthurTitle.png":
        xalign 0.5
        yalign 0.02

    # main menu "Magical Quest" subtext + alignment
    add "gui/MagicalQuestText.png":
        xalign 0.5
        yalign 0.25

    # main menu options all grouped together
    vbox:
        xalign 0.5
        yalign 0.7
        spacing 50

        # box button for "PLAY" button + alignment + hover sound
        button:
            action Start()
            hovered Play("sound", "audio/hover.mp3")
            activate_sound "audio/hover.mp3"
            background "#FF0000"
            hover_background "#000000"
            padding (4, 4)
            xalign 0.5

            # text button for "PLAY" button + alignment + hover sound
            textbutton "PLAY":
                action Start()
                #hovered Play("sound", "audio/hover.mp3")
                #activate_sound "audio/hover.mp3"
                text_size 50
                text_color "#FF0000"
                text_hover_color "#000000"
                xalign 0.5
                yalign 0.5
                background "#000000"
                hover_background "#FF0000"
                padding (135, 10)

        # box button for "HOW TO PLAY" button + alignment + hover sound
        button:
            action ShowMenu("how_to")
            hovered Play("sound", "audio/hover.mp3")
            activate_sound "audio/hover.mp3"
            background "#FF0000"
            hover_background "#000000"
            padding (4, 4)
            xalign 0.5

            # text button for "HOW TO PLAY" button + alignment + hover sound
            textbutton "HOW TO PLAY":
                action ShowMenu("how_to")
                #hovered Play("sound", "audio/hover.mp3")
                #activate_sound "audio/hover.mp3"
                text_size 50
                text_color "#FF0000"
                text_hover_color "#000000"
                xalign 0.5
                yalign 0.5
                background "#000000"
                hover_background "#FF0000"
                padding (20, 10)

        # box button for "QUIT" button + alignment + hover sound
        button:
            action Quit()
            hovered Play("sound", "audio/hover.mp3")
            activate_sound "audio/hover.mp3"
            background "#FF0000"
            hover_background "#000000"
            padding (4, 4)
            xalign 0.5

            # text button for "QUIT" button + alignment + hover sound
            textbutton "QUIT":
                action Quit()
                #hovered Play("sound", "audio/hover.mp3")
                #activate_sound "audio/hover.mp3"
                text_size 50
                text_color "#FF0000"
                text_hover_color "#000000"
                xalign 0.5
                yalign 0.5
                background "#000000"
                hover_background "#FF0000"
                padding (135, 10)

screen how_to():

    tag menu

    add "gui/HowTo.jpeg":
        fit "cover"
        xalign 0.5
        yalign 0.5

    textbutton "BACK":
        action ShowMenu("main_menu")
        hovered Play("sound", "audio/hover.mp3")
        activate_sound "audio/hover.mp3"
        text_bold True
        text_size 40
        text_color "#4e4157"
        text_hover_color "#FFFFFF"
        xalign 0.62
        yalign 0.85


# The game starts here.
label start:
    "Loading..."
    return



