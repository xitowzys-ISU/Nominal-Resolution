import numpy as np
import matplotlib.pyplot as plt


def nominal_resolution(image, max_mm):
    pixel = [i for i in image if 1 in i]

    if (len(pixel)) == 0:
        return "Объекта нету"
    else:
        res = max_mm / len(pixel)
        return res


for i in range(1, 7):
    file = open(f"./data/figure{i}.txt")

    max_mm = float(file.readline())

    file.readline()

    image = []
    for line in file:
        image.append([int(ch) for ch in line.split()])

    image = np.array(image)

    plt.subplot(int("23" + str(i)))
    plt.imshow(image)

    plt.title(nominal_resolution(image, max_mm), fontsize=6)
    plt.axis("off")

plt.Figure((20, 20))
plt.show()
