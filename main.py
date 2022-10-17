from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.shaders import lit_with_shadows_shader 
import json

application.development_mode = False
Cursor.color = color.blue

app = Ursina()
#predef
def Start():
    Audio('click.wav')
    player.enabled = True
    player.position = (0, 0, 0)
    player.rotation_y = 0
    start_button.enabled = False
    options_button.enabled = False
    quit_button.enabled = False
    title.enabled = False
    health.enabled = True

def Start1():
    Audio('click.wav')
    player.enabled = True
    start_button.enabled = False
    options_button.enabled = False
    quit_button.enabled = False
    title.enabled = False
    health.enabled = True
    start_button1.enabled = False
    reset_button.enabled = False


def quit1():
    Audio('click.wav')
    app.exitFunc()


def Options_def():
    Audio('click.wav')
    start_button.enabled = False
    options_button.enabled = False
    quit_button.enabled = False
    levels_button.enabled = True
    customize_button.enabled = True
    back_button.enabled = True
    start_button1.enabled = False
    htp_button.enabled = False

def Back():
    Audio('click.wav')
    options_button.enabled = True
    quit_button.enabled = True
    levels_button.enabled = False
    customize_button.enabled = False
    back_button.enabled = False
    levels_button.enabled = False
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    customize_button.enabled = False
    ply1_button.enabled = False
    ply2_button.enabled = False
    back_button.enabled = False
    start_button1.enabled = True
    htpt.enabled = False
    title.enabled = True

def BAck1():
    Audio('click.wav')
    start_button.enabled = False
    reset_button.enabled = False
    options_button.enabled = False
    quit_button.enabled = False
    levels_button.enabled = True
    customize_button.enabled = True
    back_button.enabled = True
    back_button1.enabled = False
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    ply1_button.enabled = False
    ply2_button.enabled = False
    start_button1.enabled = False

def lvls():
    Audio('click.wav')
    with open("level.json", "r") as f:
        data = json.load(f)
    if data["levels"] == 1:
        lvl2_button.text = "C o m p l e t e - l v l - 1"
        lvl3_button.text = "?"
        lvl4_button.text = "?"
        lvl5_button.text = "?"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl2_button.on_click = None
        lvl3_button.on_click = None
        lvl4_button.on_click = None
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 2:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "C o m p l e t e - l v l - 2"
        lvl4_button.text = "?"
        lvl5_button.text = "?"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = None
        lvl4_button.on_click = None
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 3:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "C o m p l e t e - l v l - 3"
        lvl5_button.text = "?"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = None
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 4:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "L e v e l - 4"
        lvl5_button.text = "C o m p l e t e - l v l - 4"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = lelvels4
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 5:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "L e v e l - 4"
        lvl5_button.text = "L e v e l - 5"
        lvl6_button.text = "C o m p l e t e - l v l - 5"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = lelvels4
        lvl5_button.on_click = lelvels5
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 6:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "L e v e l - 4"
        lvl5_button.text = "L e v e l - 5"
        lvl6_button.text = "L e v e l - 6"
        lvl7_button.text = "C o m p l e t e - l v l - 6"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = lelvels4
        lvl5_button.on_click = lelvels5
        lvl6_button.on_click = lelvels6
     
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 7:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "L e v e l - 4"
        lvl5_button.text = "L e v e l - 5"
        lvl6_button.text = "L e v e l - 6"
        lvl7_button.text = "L e v e l - 7"
        lvl8_button.text = "C o m p l e t e - l v l - 7"
        lvl9_button.text = "?"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = lelvels4
        lvl5_button.on_click = lelvels5
        lvl6_button.on_click = lelvels6
        lvl7_button.on_click = lelvels7
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 8:
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = lelvels4
        lvl5_button.on_click = lelvels5
        lvl6_button.on_click = lelvels6
        lvl7_button.on_click = lelvels7
        lvl8_button.on_click = lelvels8
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "L e v e l - 4"
        lvl5_button.text = "L e v e l - 5"
        lvl6_button.text = "L e v e l - 6"
        lvl7_button.text = "L e v e l - 7"
        lvl8_button.text = "L e v e l - 8"
        lvl9_button.text = "C o m p l e t e - l v l - 8"
        lvl9_button.on_click = None
    if data["levels"] == 9:
        lvl2_button.text = "l e v e l - 2"
        lvl3_button.text = "L e v e l - 3"
        lvl4_button.text = "L e v e l - 4"
        lvl5_button.text = "L e v e l - 5"
        lvl6_button.text = "L e v e l - 6"
        lvl7_button.text = "L e v e l - 7"
        lvl9_button.text = "L e v e l - 9"
        lvl2_button.on_click = lelvels2
        lvl3_button.on_click = lelvels3
        lvl4_button.on_click = lelvels4
        lvl5_button.on_click = lelvels5
        lvl6_button.on_click = lelvels6
        lvl7_button.on_click = lelvels7
        lvl8_button.on_click = lelvels8
        lvl9_button.on_click = lelvels9
    lvl1_button.enabled = True
    lvl2_button.enabled = True
    lvl3_button.enabled = True
    lvl4_button.enabled = True
    lvl5_button.enabled = True
    lvl6_button.enabled = True
    lvl7_button.enabled = True
    lvl8_button.enabled = True
    lvl9_button.enabled = True
    reset_button.enabled = True
    levels_button.enabled = False
    customize_button.enabled = False
    back_button1.enabled = True
    back_button.enabled = False
    if data["levels"] == 1:
        reset_button.enabled = False

def customize():
    Audio('click.wav')
    ply1_button.enabled = True
    ply2_button.enabled = True
    levels_button.enabled = False
    customize_button.enabled = False
    back_button.enabled = True
    back_button1.enabled = True
    back_button.enabled = False

def lelvels1():
    Audio('click.wav')
    reset_button.enabled = False
    player.position = (0, 0, 0)
    player.rotation_y = 0
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    box1.enabled = True
    box2.enabled = True
    box3.enabled = True
    box4.enabled = True
    box5.enabled = True
    box6.enabled = True
    box7.enabled = True
    box8.enabled = True
    box9.enabled = True
    box10.enabled = True
    box11.enabled = True
    box12.enabled = True
    box13.enabled = True
    b2ox.enabled = False
    b2ox1.enabled = False
    b2ox2.enabled = False
    b2ox3.enabled = False
    b2ox4.enabled = False
    b2ox5.enabled = False
    b2ox6.enabled = False
    b2ox7.enabled = False
    b2ox8.enabled = False
    b2ox9.enabled = False
    b2ox10.enabled = False
    b2ox11.enabled = False
    b2ox12.enabled = False
    b2ox13.enabled = False
    b2ox14.enabled = False
    b2ox15.enabled = False
    b2ox16.enabled = False
    b3ox.enabled = False
    b3ox2.enabled = False
    b3ox3.enabled = False
    b3ox4.enabled = False
    b3ox5.enabled = False
    b3ox6.enabled = False
    back_button.enabled = False
    back_button1.enabled = False

def lelvels2():
    Audio('click.wav')
    reset_button.enabled = False
    player.position = (0, 0, 0)
    player.rotation_y = 0
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    box1.enabled = False
    box2.enabled = False
    box3.enabled = False
    box4.enabled = False
    box5.enabled = False
    box6.enabled = False
    box7.enabled = False
    box8.enabled = False
    box9.enabled = False
    box10.enabled = False
    box11.enabled = False
    box12.enabled = False
    box13.enabled = False
    b2ox.enabled = True
    b2ox1.enabled = True
    b2ox2.enabled = True
    b2ox3.enabled = True
    b2ox4.enabled = True
    b2ox5.enabled = True
    b2ox6.enabled = True
    b2ox7.enabled = True
    b2ox8.enabled = True
    b2ox9.enabled = True
    b2ox10.enabled = True
    b2ox11.enabled = True
    b2ox12.enabled = True
    b2ox13.enabled = True
    b2ox14.enabled = True
    b2ox15.enabled = True
    b2ox16.enabled = True
    b3ox.enabled = False
    b3ox2.enabled = False
    b3ox3.enabled = False
    b3ox4.enabled = False
    b3ox5.enabled = False
    b3ox6.enabled = False
    back_button.enabled = False
    back_button1.enabled = False

def lelvels3():
    Audio('click.wav')
    player.position = (0, 0, 0)
    player.rotation_y = 0
    reset_button.enabled = False
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False
    box1.enabled = False
    box2.enabled = False
    box3.enabled = False
    box4.enabled = False
    box5.enabled = False
    box6.enabled = False
    box7.enabled = False
    box8.enabled = False
    box9.enabled = False
    box10.enabled = False
    box11.enabled = False
    box12.enabled = False
    box13.enabled = False
    b2ox.enabled = False
    b2ox1.enabled = False
    b2ox2.enabled = False
    b2ox3.enabled = False
    b2ox4.enabled = False
    b2ox5.enabled = False
    b2ox6.enabled = False
    b2ox7.enabled = False
    b2ox8.enabled = False
    b2ox9.enabled = False
    b2ox10.enabled = False
    b2ox11.enabled = False
    b2ox12.enabled = False
    b2ox13.enabled = False
    b2ox14.enabled = False
    b2ox15.enabled = False
    b2ox16.enabled = False
    b3ox.enabled = True
    b3ox2.enabled = True
    b3ox3.enabled = True
    b3ox4.enabled = True
    b3ox5.enabled = True
    b3ox6.enabled = True

def lelvels4():
    Audio('click.wav')
    reset_button.enabled = False
    player.rotation_y = 0
    player.position = (0, 0, 0)
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def lelvels5():
    Audio('click.wav')
    reset_button.enabled = False
    player.rotation_y = 0
    player.position = (0, 0, 0)
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def lelvels6():
    Audio('click.wav')
    reset_button.enabled = False
    player.rotation_y = 0
    player.position = (0, 0, 0)
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def lelvels7():
    Audio('click.wav')
    reset_button.enabled = False
    player.rotation_y = 0
    player.position = (0, 0, 0)
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def lelvels8():
    Audio('click.wav')
    reset_button.enabled = False
    player.rotation_y = 0
    player.position = (0, 0, 0)
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def lelvels9():
    Audio('click.wav')
    reset_button.enabled = False
    player.rotation_y = 0
    player.position = (0, 0, 0)
    lvl1_button.enabled = False
    lvl2_button.enabled = False
    lvl3_button.enabled = False
    lvl4_button.enabled = False
    lvl5_button.enabled = False
    lvl6_button.enabled = False
    lvl7_button.enabled = False
    lvl8_button.enabled = False
    lvl9_button.enabled = False
    title.enabled = False
    player.enabled = True
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def player1():
    Audio('click.wav')
    player.position = (0, 0, 0)
    player.rotation_y = 0
    ply1_button.enabled = False
    ply2_button.enabled = False
    title.enabled = False
    player.enabled = True
    player.texture = "blue.png"
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False

def player2():
    Audio('click.wav')
    player.position = (0, 0, 0)
    player.rotation_y = 0
    ply1_button.enabled = False
    ply2_button.enabled = False
    title.enabled = False
    player.enabled = True
    player.texture = "green.png"
    health.enabled = True
    back_button.enabled = False
    back_button1.enabled = False   

def Reseta():
    Audio('click.wav')
    with open("level.json", "r") as f:
        data = json.load(f)
    data['levels'] = 1
    with open("level.json", "w") as f:
        json.dump(data, f)
    lvl2_button.text = "C o m p l e t e - l v l - 1"
    lvl3_button.text = "?"
    lvl4_button.text = "?"
    lvl5_button.text = "?"
    lvl6_button.text = "?"
    lvl7_button.text = "?"
    lvl8_button.text = "?"
    lvl9_button.text = "?"
    reset_button.enabled = False
    levelcheck()

def levelcheck():
    with open("level.json", "r") as f:
            data = json.load(f)
            if data['levels'] == 2:
                box1.enabled = False
                box2.enabled = False
                box3.enabled = False
                box4.enabled = False
                box5.enabled = False
                box6.enabled = False
                box7.enabled = False
                box8.enabled = False
                box9.enabled = False
                box10.enabled = False
                box11.enabled = False
                box12.enabled = False
                box13.enabled = False
                b2ox.enabled = True
                b2ox1.enabled = True
                b2ox2.enabled = True
                b2ox3.enabled = True
                b2ox4.enabled = True
                b2ox5.enabled = True
                b2ox6.enabled = True
                b2ox7.enabled = True
                b2ox8.enabled = True
                b2ox9.enabled = True
                b2ox10.enabled = True
                b2ox11.enabled = True
                b2ox12.enabled = True
                b2ox13.enabled = True
                b2ox14.enabled = True
                b2ox15.enabled = True
                b2ox16.enabled = True
                b3ox.enabled = False
                if player.enabled == False:
                    player.position = (0, 0, 0)
                    player.rotation_y = 0
            if data['levels'] == 1:
                box1.enabled = True
                box2.enabled = True
                box3.enabled = True
                box4.enabled = True
                box5.enabled = True
                box6.enabled = True
                box7.enabled = True
                box8.enabled = True
                box9.enabled = True
                box10.enabled = True
                box11.enabled = True
                box12.enabled = True
                box13.enabled = True
                b2ox.enabled = False
                b2ox1.enabled = False
                b2ox2.enabled = False
                b2ox3.enabled = False
                b2ox4.enabled = False
                b2ox5.enabled = False
                b2ox6.enabled = False
                b2ox7.enabled = False
                b2ox8.enabled = False
                b2ox9.enabled = False
                b2ox10.enabled = False
                b2ox11.enabled = False
                b2ox12.enabled = False
                b2ox13.enabled = False
                b2ox14.enabled = False
                b2ox15.enabled = False
                b2ox16.enabled = False
                b3ox.enabled = False

def respawn0():
        camera.rotation_z = 0
        health.value = 15
        start_button.enabled = True
        quit_button.enabled = True
        options_button.enabled = True
        player.enabled = False
        health.enabled = False
        title.enabled = True

def esct():
    if player.enabled == True:
        start_button1.enabled = True
        quit_button.enabled = True
        options_button.enabled = True
        player.enabled = False
        title.enabled = True
        health.enabled = False
        start_button.enabled = False

def esc1():
    options_button.enabled = False
    player.enabled = False
    quit_button.enabled = False
    start_button.enabled = False
    title.enabled = True
    health.enabled = False
    start_button1.enabled = False


def htpp():
    start_button1.enabled = False
    start_button.enabled = False
    quit_button.enabled = False
    options_button.enabled = False
    back_button.enabled = True
    title.enabled = False
    htpt.enabled = True


#menu
start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.002, highlight_color = color.azure, highlight_scale = 1.01)
start_button1 = Button(text = "C o n t i n u e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.002,highlight_color=color.azure, highlight_scale = 1.01)
options_button = Button(text = "O p t i o n s", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.11,highlight_color=color.azure, highlight_scale = 1.01)
levels_button = Button(text = "L e v e l s", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.002,highlight_color=color.azure, highlight_scale = 1.01)
customize_button = Button(text = "C u s t o m i s e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.11,highlight_color=color.azure, highlight_scale = 1.01)
lvl1_button = Button(text = "L e v e l - 1", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.05, x = -0.5,highlight_color = color.azure,highlight_scale = 1.06)
lvl2_button = Button(text = "L e v e l - 2", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.05, x = 0,highlight_color = color.azure,highlight_scale = 1.06)
lvl3_button = Button(text = "L e v e l - 3", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.05, x = 0.5, highlight_color = color.azure,highlight_scale = 1.06)

lvl4_button = Button(text = "L e v e l - 4", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.15, x = -0.5, highlight_color = color.azure,highlight_scale = 1.06)
lvl5_button = Button(text = "L e v e l - 5", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.15, x = 0, highlight_color = color.azure,highlight_scale = 1.06)
lvl6_button = Button(text = "L e v e l - 6", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.15, x = 0.5, highlight_color = color.azure,highlight_scale = 1.06)

lvl7_button = Button(text = "L e v e l - 7", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.35, x = -0.5,highlight_color = color.azure,highlight_scale = 1.06)
lvl8_button = Button(text = "L e v e l - 8", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.35, x = 0,highlight_color = color.azure,highlight_scale = 1.06)
lvl9_button = Button(text = "L e v e l - 9", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.35, x = 0.5, highlight_color = color.azure,highlight_scale = 1.06)
ply1_button = Button(text = "P l a y e r - 1", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.002,highlight_color=color.azure,)
ply2_button = Button(text = "P l a y e r - 2", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.11,highlight_color=color.lime)
back_button = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = 0.45, x = -0.75,highlight_color=color.azure,highlight_scale = 1.06)
back_button1 = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = 0.45, x = -0.75,highlight_color=color.azure,highlight_scale = 1.06)
reset_button = Button(text = "R e s e t - L e v e l s", color = color.gray, scale_y = 0.05, scale_x = 0.25, y = 0.45, x = 0.75,highlight_color=color.azure,highlight_scale = 1.06)
quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.22,highlight_color=color.azure, highlight_scale = 1.01)
title = Entity(model = "quad", scale = (0.8, 0.2, 0.2), texture = "title.png", y = 0.23, parent = camera.ui)
health = HealthBar(max_value= 15, value = 15, show_lines= False,y = -0.44, x = -0.85,)
htp_button = Button(text = "?", color = color.gray, scale_y = 0.05, scale_x = 0.06, y = -0.46, x = 0.83,highlight_color=color.azure,highlight_scale = 1.06)
htpt = Text("controls: w,a,s,d + spacebar",
scale = 1.5, line_height = 2, x = 0, origin = 0, y = 0, z = -100, color = color.black)


#icons
lvl1_button.texture = "b1"
lvl2_button.texture = "b1"
lvl3_button.texture = "b1"
lvl4_button.texture = "b1"
lvl5_button.texture = "b1"
lvl6_button.texture = "b1"
lvl7_button.texture = "b1"
lvl8_button.texture = "b1"
lvl9_button.texture = "b1"

#player
player = FirstPersonController(
    model = "player3.obj",
    collider = "box",
    texture = "blue.png",
    shader=lit_with_shadows_shader
)

#onclick
start_button.on_click = Start
start_button1.on_click = Start1
quit_button.on_click = quit1
options_button.on_click = Options_def
back_button.on_click = Back
levels_button.on_click = lvls
customize_button.on_click = customize
lvl1_button.on_click = lelvels1
lvl2_button.on_click = lelvels2
lvl3_button.on_click = lelvels3
lvl4_button.on_click = lelvels4
lvl5_button.on_click = lelvels5
lvl6_button.on_click = lelvels6
lvl7_button.on_click = lelvels7
lvl8_button.on_click = lelvels8
lvl9_button.on_click = lelvels9
ply1_button.on_click = player1
ply2_button.on_click = player2
back_button1.on_click = BAck1
reset_button.on_click = Reseta
htp_button.on_click = htpp

#enabled/disabled
player.enabled = False
start_button.enabled = True
start_button1.enabled = False
options_button.enabled = True
quit_button.enabled = True
title.enabled = True
health.enabled = False
levels_button.enabled = False
customize_button.enabled = False
back_button.enabled = False
lvl1_button.enabled = False
lvl2_button.enabled = False
lvl3_button.enabled = False
lvl4_button.enabled = False
lvl5_button.enabled = False
lvl6_button.enabled = False
lvl7_button.enabled = False
lvl8_button.enabled = False
lvl9_button.enabled = False
ply1_button.enabled = False
ply2_button.enabled = False
back_button.enabled = False
back_button1.enabled = False
reset_button.enabled = False
htpt.enabled = False

def levelupdate():
    with open("level.json", "r") as f:
        data = json.load(f)
    data['levels'] += 1

    with open("level.json", "w") as f:
        json.dump(data, f)
    print(data['levels'])
    lvlupdate2()

def lvlupdate2():
    with open("level.json", "r") as f:
        data = json.load(f)
    if data["levels"] == 2:
        lelvels2()
        lvl3_button.text = "C o m p l e t e - l v l - 2"
        lvl4_button.text = "?"
        lvl5_button.text = "?"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl3_button.on_click = None
        lvl4_button.on_click = None
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 3:
        lelvels3()
        lvl4_button.text = "C o m p l e t e - l v l - 3"
        lvl5_button.text = "?"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl4_button.on_click = None
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 4:
        lelvels4()
        lvl5_button.text = "C o m p l e t e - l v l - 4"
        lvl6_button.text = "?"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl5_button.on_click = None
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 5:
        lelvels5()
        lvl6_button.text = "C o m p l e t e - l v l - 5"
        lvl7_button.text = "?"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl6_button.on_click = None
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 6:
        lelvels6()
        lvl7_button.text = "C o m p l e t e - l v l - 6"
        lvl8_button.text = "?"
        lvl9_button.text = "?"
        lvl7_button.on_click = None
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 7:
        lelvels7()
        lvl8_button.text = "C o m p l e t e - l v l - 7"
        lvl9_button.text = "?"
        lvl8_button.on_click = None
        lvl9_button.on_click = None
    if data["levels"] == 8:
        lelvels8()
        lvl9_button.text = "C o m p l e t e - l v l - 8"
        lvl9_button.on_click = None
    if data["levels"] == 9:
        lelvels9()
        lvl9_button.text = "L e v e l - 9"
        lvl9_button.on_click = lelvels9

#world options
Sky()
camera.z = -5
window.exit_button.enabled = False
window.fullscreen = True
player.speed = 8
window.fps_counter.enabled = False
velocity_y = player.jump_height * 40
Text.default_font = "Roboto.ttf"
window.show_ursina_splash = True
window.borderless = True
health.text_entity.disable()
DirectionalLight(direction = (-0.7, -0.9, 0.5), resolution = 5000)
AmbientLight(color = Vec4(0.5, 0.55, 0.66, 0) * 1.3)

#level
box = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
    
)
box1 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box2 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box3 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box4 = Entity(
    model = "cube",
    scale = (0.5, 1, 0.5),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box5 = Entity(
    model = "cube",
    scale = (0.5, 1, 0.5),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box6 = Entity(
    model = "cube",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box7 = Entity(
    model = "cube",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box8 = Entity(
    model = "sphere",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box9 = Entity(
    model = "sphere",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box10 = Entity(
    model = "sphere",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box11 = Entity(
    model = "cube",
    scale = (3, 0.2, 0.3),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box12 = Entity(
    model = "cube",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

box13 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    color = color.lime,
    shader=lit_with_shadows_shader
)


box1.position = (0, 1, 4)
box2.position = (-2, 2, 7)
box3.position = (-2, 3, 10)
box4.position = (1, 4, 10)
box5.position = (3, 5, 10)
box6.position = (3, 6, 12)
box7.position = (3, 7, 14)
box8.position = (3, 7, 17)
box9.position = (0, 8, 19)
box10.position = (-2, 9, 23)
box11.position = (-5, 9, 23)
box12.position = (-8, 9, 23)
box13.position = (-8, 10, 26)

#level 2
b2ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
    shader=lit_with_shadows_shader
)

b2ox1 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox2 = Entity(
    model = "cube",
    scale = (3, 0.2, 0.3),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox3 = Entity(
    model = "cube",
    scale = (1, 0.5, 1),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

b2ox4 = Entity(
    model = "cube",
    scale = (0.5, 1, 0.5),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

b2ox5 = Entity(
    model = "cube",
    scale = (0.5, 1, 0.5),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

b2ox6 = Entity(
    model = "cube",
    scale = (0.5, 1, 0.5),
    collider = "box",
    texture = "white_cube",
    parent = "box",
    shader=lit_with_shadows_shader
)

b2ox7 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox8 = Entity(
    model = "cube",
    scale = (3, 0.2, 0.3),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox9 = Entity(
    model = "cube",
    scale = (3, 0.2, 0.3),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox10 = Entity(
    model = "cube",
    scale = (3, 0.2, 0.3),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox11 = Entity(
    model = "cube",
    scale = (3, 0.2, 0.3),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox12 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox13 = Entity(
    model = "sphere",
    scale = (1, 1, 1),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox14 = Entity(
    model = "sphere",
    scale = (1.5, 1.5, 1.5),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)
b2ox15 = Entity(
    model = "sphere",
    scale = (1.8, 1.8, 1.8),
    collider = "box",
    texture = "white_cube",
    parent = "b2ox",
    shader=lit_with_shadows_shader
)

b2ox16 = Entity(
    model = "cube",
    scale = (2, 0.5, 2),
    collider = "box",
    texture = "white_cube",
    color = color.lime,
    shader=lit_with_shadows_shader
)



#enabled/disabled
b2ox.enabled = False
b2ox1.enabled = False
b2ox2.enabled = False
b2ox3.enabled = False
b2ox4.enabled = False
b2ox5.enabled = False
b2ox6.enabled = False
b2ox7.enabled = False
b2ox8.enabled = False
b2ox9.enabled = False
b2ox10.enabled = False
b2ox11.enabled = False
b2ox12.enabled = False
b2ox13.enabled = False
b2ox14.enabled = False
b2ox15.enabled = False
b2ox16.enabled = False
#positions

b2ox1.position = (0,1,4)
b2ox2.position = (3,1,4)
b2ox3.position = (6, 1, 4)
b2ox4.position = (6, 2, 6)
b2ox5.position = (8, 3, 8)
b2ox6.position = (6, 4, 10)
b2ox7.position = (6, 5, 13)
b2ox8.position = (6, 6, 15)
b2ox9.position = (6, 7, 16)
b2ox10.position = (6, 8, 17)
b2ox11.position = (6, 9, 18)
b2ox12.position = (6, 9, 20)
b2ox13.position = (8, 10, 20)
b2ox14.position = (10, 11, 20)
b2ox15.position = (12, 12, 20)
b2ox16.position = (15, 12, 20)

#level 3
b3ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)
b3ox2 = Entity(
    model = "cube",
    collider = "box",
    texture = "white_cube"
)
b3ox3 = Entity(
    model = "cube",
    collider = "box",
    texture = "white_cube"
)
b3ox4 = Entity(
    model = "cube",
    collider = "box",
    texture = "white_cube"
)
b3ox5 = Entity(
    model = "cube",
    collider = "box",
    texture = "white_cube"
)
b3ox6 = Entity(
    model = "cube",
    collider = "box",
    texture = "white_cube"
)


#enabled disabled lvl3
b3ox.enabled = False
b3ox2.enabled = False
b3ox3.enabled = False
b3ox4.enabled = False
b3ox5.enabled = False
b3ox6.enabled = False

#positions
b3ox2.position = (0, 1, 4)
b3ox3.position = (0, 2, 7)
b3ox4.position = (-3, 3, 7)
b3ox5.position = (-3, 4, 4)
b3ox6.position = (1.5, 5, 4)



#level 4
b4ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)

#enabled disabled lvl4
b4ox.enabled = False

#level 5
b5ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)

#enabled disabled lvl5
b5ox.enabled = False

#level 6
b6ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)

#enabled disabled lvl6
b6ox.enabled = False

#level 7
b7ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)

#enabled disabled lvl7
b7ox.enabled = False

#level 8 
b8ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)

#enabled disabled lvl8
b8ox.enabled = False

#level 9
b9ox = Entity(
    model = "cube",
    scale = (3, 0.5, 3),
    collider = "box",
    texture = "white_cube",
)

#enabled disabled lvl9
b9ox.enabled = False
#update
def update():
    if held_keys['escape']:
        esct()

    if player.y < -20:
        player.position = (0, 0, 0)
        player.rotation_y = 0
        health.value -= 1
        player.blink(color.red)

    if health.value == 0:
        respawn0()

    if lvl1_button.enabled == True:
        if held_keys['escape']:
           esc1()

    if back_button.enabled == True:
        if held_keys['escape']:
           options_button.enabled = False
           player.enabled = False
           quit_button.enabled = False
           start_button.enabled = False
           title.enabled = True
           health.enabled = False
           start_button1.enabled = False

    if back_button1.enabled == True:
        if held_keys['escape']:
           options_button.enabled = False
           player.enabled = False
           quit_button.enabled = False
           start_button.enabled = False
           title.enabled = True
           health.enabled = False
           start_button1.enabled = False

    if ply1_button.enabled == True:
        if held_keys['escape']:
           options_button.enabled = False
           player.enabled = False
           quit_button.enabled = False
           start_button.enabled = False
           title.enabled = True
           health.enabled = False
           start_button1.enabled = False

    if start_button.enabled == True:
        if held_keys['escape']:
           options_button.enabled = True
           player.enabled = False
           quit_button.enabled = True
           start_button.enabled = True
           title.enabled = True
           health.enabled = False 
           start_button1.enabled = False
           levels_button.enabled = False
           customize_button.enabled = False

    if levels_button.enabled == True:
        start_button1.enabled = False
        quit_button.enabled = False
        options_button.enabled = False

    if back_button1.enabled == True:
        start_button.enabled = False
        start_button1.enabled = False
        quit_button.enabled = False
        options_button.enabled = False

    if start_button1.enabled == True:
        start_button.enabled = False

    if start_button.enabled == True:
        back_button1.enabled = False
        back_button.enabled = False

    if player.z > 26:
        with open("level.json", "r") as f:
            data = json.load(f)
        if data['levels'] == 1:
            levelupdate()

    if player.x > 15:
        with open("level.json", "r") as f:
            data = json.load(f)
        if data['levels'] == 2:
            levelupdate()

    if player.z > 26:
        with open("level.json", "r") as f:
            data = json.load(f)
        if data['levels'] > 1:
            lelvels2()

    if player.z > 26:
        with open("level.json", "r") as f:
            data = json.load(f)
        if data['levels'] > 2:
            lelvels3()

    if player.x > 15:
        lelvels3()

    if player.air_time > 0:
        if held_keys['escape']:
           options_button.enabled = False
           player.enabled = True
           quit_button.enabled = False
           health.enabled = True
           title.enabled = False
           start_button1.enabled = False
           player.position = player.position

    if start_button.enabled == False:
        htp_button.enabled = False

    if start_button.enabled == True:
        htp_button.enabled = True

    if player.enabled == False:
        htp_button.enabled = True

    if levels_button.enabled == True:
        htp_button.enabled = False

    if lvl1_button.enabled == True:
        htp_button.enabled = False

    if ply1_button.enabled == True:
        htp_button.enabled = False

    if htpt.enabled == True:
        htp_button.enabled = False


levelcheck()
app.run()