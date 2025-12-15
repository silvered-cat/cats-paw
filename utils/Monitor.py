from ctypes import WinDLL


# This should return a tuple that has width(0) and height(1) as pixels(int).
def getUserMonitorSize() -> tuple[int, int]:
    """
    Returns a tuple with user screen width and height in pixels.
    Only supports Windows Operating systems.

    :rtype: tuple[int, int]
    :return: [width, height]
    """
    return _getWindowSizeWindows()


# This should return a tuple of the user's monitor size using the Windows API.
def _getWindowSizeWindows() -> tuple[int, int]:
    """
    Uses the Windows API to get the user's monitor size in pixels.

    :rtype: tuple[int, int]
    :return: [width, height]
    """

    # Load the user32 DLL
    user32 = WinDLL("user32")

    # Set the process to be DPI Aware
    isDPIAware = user32.SetProcessDPIAware()

    # Expect a non-zero return value for success.
    if isDPIAware == 0:
        raise RuntimeError("Failed to set process as DPI Aware.")

    # Get the screen width and height in pixels.
    windowWidth = user32.GetSystemMetrics(0)
    windowHeight = user32.GetSystemMetrics(1)

    # Create the return tuple for type inference.
    WINDOW_TUPLE = (windowWidth, windowHeight)

    return WINDOW_TUPLE
