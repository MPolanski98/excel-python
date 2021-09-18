import pyautogui, sys
print('Press Ctrl-C to quit.')

points = []
max_points = 6



try:
    while len(points) < max_points - 1:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')