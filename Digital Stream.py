import random, shutil, sys, time

MIN_STREAM_LENGTH = 6  # (!) Try changing this to 1 or 50.
MAX_STREAM_LENGTH = 14  # (!) Try changing this to 100.
PAUSE = 0.3  # (!) Try changing this to 0.0 or 2.0.
STREAM_CHARS = ['0', '1']  # (!) Try changing this to other characters.
# Density can range from 0.0 to 1.0:
DENSITY = 0.1  # (!) Try changing this to 0.10 or 0.30.
WIDTH = shutil.get_terminal_size()[0]


time.sleep(2)
try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print('    ', end='')
        print()  # Print a newline at the end of the row of columns.
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
