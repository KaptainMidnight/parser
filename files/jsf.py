from time import sleep
from tqdm import tqdm


def progressbar():
    for i in tqdm(range(9000)):
        sleep(0.01)


print(progressbar())
