import pyautogui as at
# here adding this comment


def click():
	at.click()
def dclick():
	at.doubleClick()


scWidth,scHeight = at.size()
curX,curY = at.position()
print(scWidth," : ",scHeight)
print(curX," : ",curY)
at.moveTo(500,150)
click()
dclick()
dclick()
at.typewrite("# here adding this comment")
at.keyDown('ctrl')
at.press(['enter','s'])
at.keyUp('ctrl')
# at.scroll(-100)

print(at.getWindows())