import pykraken as kn
from screens.Menu import Menu
from queue import Queue
from utils import Monitor
from shapes.ShapeFactory import ShapeFactory
from shapes.Shape import Shape

# Must get user monitor in order to become DPI aware
USER_SCN = Monitor.getUserMonitorSize()

# Constants
GAME_TITLE = "Cat's Paw"
ADJUSTED_SCN: tuple[float, float] = (USER_SCN[0] * 0.8, USER_SCN[1] * 0.8)


# Unleash the Kraken! *Must be called after getting monitor size*
kn.init()


# Create a fullscreen
kn.window.create(GAME_TITLE, kn.Vec2(ADJUSTED_SCN[0], ADJUSTED_SCN[1]))

# Create shapes
shapeFactory = ShapeFactory()

titleScreen = Menu(ADJUSTED_SCN)
renderQueue: Queue[Shape] = Queue()

# Need to poll events to keep the window responsive
# Main loop
while kn.window.is_open():
    kn.event.poll()  # returns a list of events
    kn.renderer.clear()
    while renderQueue.qsize() > 0:
        shape = renderQueue.get()
        shape.draw()

    titleScreen.run(renderQueue)
    kn.renderer.present()
# Cleanup
kn.quit()
