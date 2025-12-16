import pykraken as kn
from screens.Menu import Menu
from queue import Queue
from utils import Monitor
from shapes.Shape import Shape
from state.Game import Game
from screens.screensEnum import ScreensEnum

# Must get user monitor in order to become DPI aware
USER_SCN = Monitor.getUserMonitorSize()

# Constants
GAME_TITLE = "Cat's Paw"
ADJUSTED_SCN: tuple[float, float] = (USER_SCN[0] * 0.8, USER_SCN[1] * 0.8)


# Unleash the Kraken! *Must be called after getting monitor size*
kn.init()


# Create a fullscreen
kn.window.create(GAME_TITLE, kn.Vec2(ADJUSTED_SCN[0], ADJUSTED_SCN[1]))

# Make Game State
game = Game()

# Create Screens
screens = {
    ScreensEnum.MENU: Menu(game),
}


renderQueue: Queue[Shape] = Queue()
currentlyLoadedScreen = screens[ScreensEnum.MENU]
# Need to poll events to keep the window responsive
# Main loop
while kn.window.is_open():
    kn.renderer.clear()
    events = kn.event.poll()  # returns a list of events
    currentlyLoadedScreen.run(renderQueue)
    for e in events:
        currentlyLoadedScreen.handleEvent(e)
    while renderQueue.qsize() > 0:
        shape = renderQueue.get()
        shape.draw()
    kn.renderer.present()
    nextScreen = game.getCurrentScreen()
    currentlyLoadedScreen = screens[nextScreen]
# Cleanup
kn.quit()
