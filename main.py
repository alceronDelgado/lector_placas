from setuptools import setup
from package.functions import menu
from package.functions import video_recording


def main():
    video_recording(menu())


main()


if __name__ == '__main__':
    main()