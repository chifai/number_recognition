from BinaryReader import BinaryReader
import matplotlib.pyplot as plt
import numpy as np

# read image and label data
image = BinaryReader("t10k-images.idx3-ubyte")
label = BinaryReader("t10k-labels.idx1-ubyte")

while True:
    print("Which image to display? Or Exit(q)\n")
    print("Range: 0 to " + image.m_lsDimension[0] + '\n')
    option = input()

    if option == 'q':
        print("Good day\n")
        break

    if option.isnumeric() is True:
        ind = int(option)
        if ind >= image.m_lsDimension[0] or ind < 0:
            # invalid input
            print("Invalid input\n")
            continue
        # print the answer which should be matching with the image
        print(label.GetOneData(int(option)))

        # show the image
        im = image.GetOneData(int(option))
        plt.imshow(np.array(im).reshape(image.m_lsDimension[1], image.m_lsDimension[2]), cmap='gray')

        # press the window to exit
        plt.waitforbuttonpress()
