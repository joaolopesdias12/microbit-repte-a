def on_button_pressed_a():
    basic.show_leds("""
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        # # . . #
        # # . # .
        . . # . .
        # # . # .
        # # . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if randint(1, 3) == 1:
        basic.show_leds("""
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            """)
    elif randint(1, 3) == 2:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    else:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
