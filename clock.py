from neopixel import Neopixel
    
#     F
#    ---
# A |   | E
#    -G-
# B |   | D
#    ---
#     C

SEGMENTS_BY_DIGIT = 7
LEDS_BY_SEGMENT = 4
DIGITS = 4
DOTS = 2

colors = [
  (0x00, 0x00, 0x00), #00 - off
  (0xff, 0x00, 0x00), #01 - 00h red
  (0xff, 0x00, 0x40), #02 - 01h crimson
  (0xff, 0x00, 0x80), #03 - 02h rose
  (0xff, 0x00, 0xc0), #04 - 03h cerise
  (0xff, 0x00, 0xff), #05 - 04h magenta
  (0xc0, 0x00, 0xff), #06 - 05h purple
  (0x80, 0x00, 0xff), #07 - 06h violet
  (0x40, 0x00, 0xff), #08 - 07h indigo
  (0x00, 0x00, 0xff), #09 - 08h blue
  (0x00, 0x40, 0xff), #10 - 09h cerulean
  (0x00, 0x80, 0xff), #11 - 10h azure
  (0x00, 0xc0, 0xff), #12 - 11h capri
  (0x00, 0xff, 0xff), #13 - 12h cyan
  (0x00, 0xff, 0xc0), #14 - 13h aquamarine
  (0x00, 0xff, 0x80), #15 - 14h spring green
  (0x00, 0xff, 0x40), #16 - 15h erin
  (0x00, 0xff, 0x00), #17 - 16h green
  (0x40, 0xff, 0x00), #18 - 17h harlequin
  (0x80, 0xff, 0x00), #19 - 18h chartreuse
  (0xc0, 0xff, 0x00), #20 - 19h lime
  (0xff, 0xff, 0x00), #21 - 20h yellow
  (0xff, 0xc0, 0x00), #22 - 21h amber
  (0xff, 0x80, 0x00), #23 - 22h orange
  (0xff, 0x40, 0x00), #24 - 23h vermilion
  (0xff, 0xff, 0xff), #25 - white
]

pixels = Neopixel((SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT * DIGITS) + DOTS, 0, 6, "GRB")

def mapDigits(value, dotState):
    pixels = [0 for x in range(len(value) * SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)]

    for dig in range(len(value)):
        a = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) for x in range(LEDS_BY_SEGMENT)]
        b = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) + (1 * LEDS_BY_SEGMENT) for x in range(LEDS_BY_SEGMENT)]
        c = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) + (2 * LEDS_BY_SEGMENT) for x in range(LEDS_BY_SEGMENT)]
        d = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) + (3 * LEDS_BY_SEGMENT) for x in range(LEDS_BY_SEGMENT)]
        e = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) + (4 * LEDS_BY_SEGMENT) for x in range(LEDS_BY_SEGMENT)]
        f = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) + (5 * LEDS_BY_SEGMENT) for x in range(LEDS_BY_SEGMENT)]
        g = [x + (dig * (SEGMENTS_BY_DIGIT * LEDS_BY_SEGMENT)) + (6 * LEDS_BY_SEGMENT) for x in range(LEDS_BY_SEGMENT)]

        digits = {
            "0": [a, b, c, d, e, f],
            "1": [d, e],
            "2": [b, c, e, f, g],
            "3": [c, d, e, f, g],
            "4": [a, d, e, g],
            "5": [a, c, d, f, g],
            "6": [a, b, c, d, f, g],
            "7": [d, e, f],
            "8": [a, b, c, d, e, f, g],
            "9": [a, c, d, e, f, g],
            " ": [],
            "-": [g]
        }

        for digit in digits[value[dig]]:
            for pixel in digit:
                pixels[pixel] = 1
                
        if dotState:
            dots = [1 for x in range(DOTS)]
        else:
            dots = [0 for x in range(DOTS)]

        pixels.extend(dots)

    return pixels


def setBrightness(value):
    pixels.brightness(value)


def refreshClock(data, color_index=1, brightness=127, dotState=True):
    p = mapDigits(data, dotState)

    pixels.brightness(brightness)
    
    for i in range(len(p)):
        if p[i]:
            pixels.set_pixel(i, colors[color_index])
        else:
            pixels.set_pixel(i, colors[0])

    pixels.show()

