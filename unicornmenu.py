from guizero import App, Text, PushButton, Slider
import unicornhat as uni

lastSelectedx = 0
lastSelectedy = 0

def btnPress(x, y):
    global lastSelectedx
    global lastSelectedy
    sldRed.value, sldGreen.value, sldBlue.value = uni.get_pixel(x,y)
    lastSelectedx, lastSelectedy = x, y
    
def btnPress00():
    btnPress(0, 0)

def btnPress10():
    btnPress(1, 0)

def btnPress20():
    btnPress(2, 0)

def btnPress30():
    btnPress(3, 0)

def btnPress40():
    btnPress(4, 0)

def btnPress50():
    btnPress(5, 0)

def btnPress60():
    btnPress(6, 0)

def btnPress70():
    btnPress(7, 0)

def btnPress01():
    btnPress(0, 1)

def btnPress11():
    btnPress(1, 1)
    
def btnPress21():
    btnPress(2, 1)

def btnPress31():
    btnPress(3, 1)

def btnPress41():
    btnPress(4, 1)

def btnPress51():
    btnPress(5, 1)

def btnPress61():
    btnPress(6, 1)

def btnPress71():
    btnPress(7, 1)

def btnPress02():
    btnPress(0, 2)

def btnPress12():
    btnPress(1, 2)

def btnPress22():
    btnPress(2, 2)

def btnPress32():
    btnPress(3, 2)

def btnPress42():
    btnPress(4, 2)

def btnPress52():
    btnPress(5, 2)

def btnPress62():
    btnPress(6, 2)

def btnPress72():
    btnPress(7, 2)

def btnPress03():
    btnPress(0, 3)

def btnPress13():
    btnPress(1, 3)

def btnPress23():
    btnPress(2, 3)

def btnPress33():
    btnPress(3, 3)

def btnPress43():
    btnPress(4, 3)

def btnPress53():
    btnPress(5, 3)

def btnPress63():
    btnPress(6, 3)

def btnPress73():
    btnPress(7, 3)

def btnPress04():
    btnPress(0, 4)

def btnPress14():
    btnPress(1, 4)

def btnPress24():
    btnPress(2, 4)

def btnPress34():
    btnPress(3, 4)

def btnPress44():
    btnPress(4, 4)

def btnPress54():
    btnPress(5, 4)

def btnPress64():
    btnPress(6, 4)

def btnPress74():
    btnPress(7, 4)

def btnPress05():
    btnPress(0, 5)

def btnPress15():
    btnPress(1, 5)

def btnPress25():
    btnPress(2, 5)

def btnPress35():
    btnPress(3, 5)

def btnPress45():
    btnPress(4, 5)

def btnPress55():
    btnPress(5, 5)

def btnPress65():
    btnPress(6, 5)

def btnPress75():
    btnPress(7, 5)

def btnPress06():
    btnPress(0, 6)

def btnPress16():
    btnPress(1, 6)

def btnPress26():
    btnPress(2, 6)

def btnPress36():
    btnPress(3, 6)

def btnPress46():
    btnPress(4, 6)

def btnPress56():
    btnPress(5, 6)

def btnPress66():
    btnPress(6, 6)

def btnPress76():
    btnPress(7, 6)

def btnPress07():
    btnPress(0, 7)

def btnPress17():
    btnPress(1, 7)

def btnPress27():
    btnPress(2, 7)

def btnPress37():
    btnPress(3, 7)

def btnPress47():
    btnPress(4, 7)

def btnPress57():
    btnPress(5, 7)

def btnPress67():
    btnPress(6, 7)

def btnPress77():
    btnPress(7, 7)

def sldSlide():
    global lastSelectedx
    global lastSelectedy
    red, green, blue = sldRed.value, sldGreen.value, sldBlue.value
    uni.set_pixel(lastSelectedx, lastSelectedy, red, green, blue)
    gridBtn[lastSelectedx][lastSelectedy].bg = (red, green, blue)
    uni.show()

def slideBright():
    uni.brightness(b=(sldBrightness.value/10))
    uni.show()

app = App(title = "Test", layout="grid", width=600)

btn00 = PushButton(app, text="", command=btnPress00, height=1, width=2, grid=[0,0])
btn10 = PushButton(app, text="", command=btnPress10, height=1, width=2, grid=[1,0])
btn20 = PushButton(app, text="", command=btnPress20, height=1, width=2, grid=[2,0])
btn30 = PushButton(app, text="", command=btnPress30, height=1, width=2, grid=[3,0])
btn40 = PushButton(app, text="", command=btnPress40, height=1, width=2, grid=[4,0])
btn50 = PushButton(app, text="", command=btnPress50, height=1, width=2, grid=[5,0])
btn60 = PushButton(app, text="", command=btnPress60, height=1, width=2, grid=[6,0])
btn70 = PushButton(app, text="", command=btnPress70, height=1, width=2, grid=[7,0])
btn01 = PushButton(app, text="", command=btnPress01, height=1, width=2, grid=[0,1])
btn11 = PushButton(app, text="", command=btnPress11, height=1, width=2, grid=[1,1])
btn21 = PushButton(app, text="", command=btnPress21, height=1, width=2, grid=[2,1])
btn31 = PushButton(app, text="", command=btnPress31, height=1, width=2, grid=[3,1])
btn41 = PushButton(app, text="", command=btnPress41, height=1, width=2, grid=[4,1])
btn51 = PushButton(app, text="", command=btnPress51, height=1, width=2, grid=[5,1])
btn61 = PushButton(app, text="", command=btnPress61, height=1, width=2, grid=[6,1])
btn71 = PushButton(app, text="", command=btnPress71, height=1, width=2, grid=[7,1])
btn02 = PushButton(app, text="", command=btnPress02, height=1, width=2, grid=[0,2])
btn12 = PushButton(app, text="", command=btnPress12, height=1, width=2, grid=[1,2])
btn22 = PushButton(app, text="", command=btnPress22, height=1, width=2, grid=[2,2])
btn32 = PushButton(app, text="", command=btnPress32, height=1, width=2, grid=[3,2])
btn42 = PushButton(app, text="", command=btnPress42, height=1, width=2, grid=[4,2])
btn52 = PushButton(app, text="", command=btnPress52, height=1, width=2, grid=[5,2])
btn62 = PushButton(app, text="", command=btnPress62, height=1, width=2, grid=[6,2])
btn72 = PushButton(app, text="", command=btnPress72, height=1, width=2, grid=[7,2])
btn03 = PushButton(app, text="", command=btnPress03, height=1, width=2, grid=[0,3])
btn13 = PushButton(app, text="", command=btnPress13, height=1, width=2, grid=[1,3])
btn23 = PushButton(app, text="", command=btnPress23, height=1, width=2, grid=[2,3])
btn33 = PushButton(app, text="", command=btnPress33, height=1, width=2, grid=[3,3])
btn43 = PushButton(app, text="", command=btnPress43, height=1, width=2, grid=[4,3])
btn53 = PushButton(app, text="", command=btnPress53, height=1, width=2, grid=[5,3])
btn63 = PushButton(app, text="", command=btnPress63, height=1, width=2, grid=[6,3])
btn73 = PushButton(app, text="", command=btnPress73, height=1, width=2, grid=[7,3])
btn04 = PushButton(app, text="", command=btnPress04, height=1, width=2, grid=[0,4])
btn14 = PushButton(app, text="", command=btnPress14, height=1, width=2, grid=[1,4])
btn24 = PushButton(app, text="", command=btnPress24, height=1, width=2, grid=[2,4])
btn34 = PushButton(app, text="", command=btnPress34, height=1, width=2, grid=[3,4])
btn44 = PushButton(app, text="", command=btnPress44, height=1, width=2, grid=[4,4])
btn54 = PushButton(app, text="", command=btnPress54, height=1, width=2, grid=[5,4])
btn64 = PushButton(app, text="", command=btnPress64, height=1, width=2, grid=[6,4])
btn74 = PushButton(app, text="", command=btnPress74, height=1, width=2, grid=[7,4])
btn05 = PushButton(app, text="", command=btnPress05, height=1, width=2, grid=[0,5])
btn15 = PushButton(app, text="", command=btnPress15, height=1, width=2, grid=[1,5])
btn25 = PushButton(app, text="", command=btnPress25, height=1, width=2, grid=[2,5])
btn35 = PushButton(app, text="", command=btnPress35, height=1, width=2, grid=[3,5])
btn45 = PushButton(app, text="", command=btnPress45, height=1, width=2, grid=[4,5])
btn55 = PushButton(app, text="", command=btnPress55, height=1, width=2, grid=[5,5])
btn65 = PushButton(app, text="", command=btnPress65, height=1, width=2, grid=[6,5])
btn75 = PushButton(app, text="", command=btnPress75, height=1, width=2, grid=[7,5])
btn06 = PushButton(app, text="", command=btnPress06, height=1, width=2, grid=[0,6])
btn16 = PushButton(app, text="", command=btnPress16, height=1, width=2, grid=[1,6])
btn26 = PushButton(app, text="", command=btnPress26, height=1, width=2, grid=[2,6])
btn36 = PushButton(app, text="", command=btnPress36, height=1, width=2, grid=[3,6])
btn46 = PushButton(app, text="", command=btnPress46, height=1, width=2, grid=[4,6])
btn56 = PushButton(app, text="", command=btnPress56, height=1, width=2, grid=[5,6])
btn66 = PushButton(app, text="", command=btnPress66, height=1, width=2, grid=[6,6])
btn76 = PushButton(app, text="", command=btnPress76, height=1, width=2, grid=[7,6])
btn07 = PushButton(app, text="", command=btnPress07, height=1, width=2, grid=[0,7])
btn17 = PushButton(app, text="", command=btnPress17, height=1, width=2, grid=[1,7])
btn27 = PushButton(app, text="", command=btnPress27, height=1, width=2, grid=[2,7])
btn37 = PushButton(app, text="", command=btnPress37, height=1, width=2, grid=[3,7])
btn47 = PushButton(app, text="", command=btnPress47, height=1, width=2, grid=[4,7])
btn57 = PushButton(app, text="", command=btnPress57, height=1, width=2, grid=[5,7])
btn67 = PushButton(app, text="", command=btnPress67, height=1, width=2, grid=[6,7])
btn77 = PushButton(app, text="", command=btnPress77, height=1, width=2, grid=[7,7])

txtBrightness = Text(app, text="Brightness", grid=[8,0])
sldBrightness = Slider(app, command=slideBright, start=0, end=10, width=255, grid=[8,1])
txtRed = Text(app, text="Red", color="red", grid=[8,2])
sldRed = Slider(app, command=sldSlide, start=0, end=255, width=255, grid=[8,3])
txtGreen = Text(app, text="Green", color="green", grid=[8,4])
sldGreen = Slider(app, command=sldSlide, start=0, end=255, width=255, grid=[8,5])
txtBlue = Text(app, text="Blue", color="blue", grid=[8,6])
sldBlue = Slider(app, command=sldSlide, start=0, end=255, width=255, grid=[8,7])

gridBtn = {
    0 : {
        0 : btn00,
        1 : btn01,
        2 : btn02,
        3 : btn03,
        4 : btn04,
        5 : btn05,
        6 : btn06,
        7 : btn07
    },
    1 : {
        0 : btn10,
        1 : btn11,
        2 : btn12,
        3 : btn13,
        4 : btn14,
        5 : btn15,
        6 : btn16,
        7 : btn17
    },
    2 : {
        0 : btn20,
        1 : btn21,
        2 : btn22,
        3 : btn23,
        4 : btn24,
        5 : btn25,
        6 : btn26,
        7 : btn27
    },
    3 : {
        0 : btn30,
        1 : btn31,
        2 : btn32,
        3 : btn33,
        4 : btn34,
        5 : btn35,
        6 : btn36,
        7 : btn37
    },
    4 : {
        0 : btn40,
        1 : btn41,
        2 : btn42,
        3 : btn43,
        4 : btn44,
        5 : btn45,
        6 : btn46,
        7 : btn47
    },
    5 : {
        0 : btn50,
        1 : btn51,
        2 : btn52,
        3 : btn53,
        4 : btn54,
        5 : btn55,
        6 : btn56,
        7 : btn57
    },
    6 : {
        0 : btn60,
        1 : btn61,
        2 : btn62,
        3 : btn63,
        4 : btn64,
        5 : btn65,
        6 : btn66,
        7 : btn67
    },
    7 : {
        0 : btn70,
        1 : btn71,
        2 : btn72,
        3 : btn73,
        4 : btn74,
        5 : btn75,
        6 : btn76,
        7 : btn77
    }    
    }

app.display()