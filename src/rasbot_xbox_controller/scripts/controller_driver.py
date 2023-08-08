from inputs import get_gamepad

class XboxController:

    def __init__(self):
        pass

while True:
    events = get_gamepad()
    for event in events:
        print(event.code)
