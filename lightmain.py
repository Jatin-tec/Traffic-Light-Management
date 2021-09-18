import turtle as t
import time as te
import test
import logic
import math

maxt = 30
mint = 10

class Tlight:
    cordx = None
    cordy = None


    def tlight(self, rlight, ylight, glight):

        t.pencolor('white')
        t.penup()
        t.goto(-30, 60)
        t.pendown()
        t.pensize(5)
        t.goto(30, 60)
        t.goto(30, -60)
        t.goto(-30, -60)
        t.goto(-30, 60)

        red_light = t.Turtle()
        red_light.penup()
        red_light.goto(-0.5, 45)
        red_light.pendown()
        red_light.pensize(5)
        red_light.shape('circle')
        red_light.color(rlight)
        red_light.goto(-0.5, 45)

        yellow_light = t.Turtle()
        yellow_light.penup()
        yellow_light.goto(-0.5, 5)
        yellow_light.pendown()
        yellow_light.pensize(5)
        yellow_light.shape('circle')
        yellow_light.color(ylight)
        yellow_light.goto(-0.5, 5)

        green_light = t.Turtle()
        green_light.penup()
        green_light.goto(-0.5, -35)
        green_light.pendown()
        green_light.pensize(5)
        green_light.shape('circle')
        green_light.color(glight)
        green_light.goto(-0.5, -35)



rlight = 'red'
ylight = 'yellow'
glight = 'green'

north = Tlight()

north.cordx = -0.5
north.cordy = 10

south = Tlight()
south.cordx = 69.5
south.cordy = 10

def light_control(val):
   while True:
        north.tlight(rlight, 'grey', 'grey')
        te.sleep(4)
        north.tlight('gray', ylight, 'gray')
        te.sleep(3)
        north.tlight('gray', 'gray', glight)
        print(val)
        te.sleep(val)

def create_win():
    wn = t.Screen()
    wn.title('traffic light')
    wn.bgcolor('black')
    light_control(get_val())
    wn.mainloop()

def get_val():
    factor = logic.factor_cal()
    car = test.count()
    if factor < 3:
        result = car * math.log(car, 4)
    elif factor > 5:
        result = car * car * math.log(car)
    else:
        result = car*1

    return result