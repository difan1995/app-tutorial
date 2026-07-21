import numpy as np
import cv2
from waggle.plugin import Plugin
from waggle.data.vision import Camera


def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)


def main():
    with Plugin() as plugin, Camera("file:///example.jpg") as camera:
        # read example image from file
        image = camera.snapshot()

        # compute mean color
        mean_color = compute_mean_color(image.data)

        # print mean color
        print(mean_color)
        plugin.publish("color.mean.r", mean_color[0], timestamp=image.timestamp)
        plugin.publish("color.mean.g", mean_color[1], timestamp=image.timestamp)
        plugin.publish("color.mean.b", mean_color[2], timestamp=image.timestamp)
        image.save("snapshot.jpg")
        plugin.upload_file("snapshot.jpg", timestamp=image.timestamp)

if __name__ == "__main__":
    main()
