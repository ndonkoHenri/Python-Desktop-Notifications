# Python Desktop Notifications

The Blog Post to this could be found [here]().

## Description

This repo is meant to expose the various ways one could send desktop notifications using python.
I went through some available python projects to send desktop notifications, and came up this List and also built a GUI app (with [Flet](https://flet.dev)) to compile all of them on one area.

I will keep updating the app once I discover any other python notification library.

Feel free to make suggestions too :)

### Libraries 

- [Plyer](https://github.com/kivy/plyer) - Cross platform
- [notify-py](https://github.com/ms7m/notify-py) - Cross Platform
- [Pynotifier](https://github.com/YuriyLisovskiy/pynotifier) - Cross platform
- [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications) - Windows only
- [win10toast_click](https://github.com/vardecab/win10toast-click) - Windows only

To install the packages, you could make use of this command:

```bash
pip install -r requirements.txt
```

## Note
- I tested these libraries only on Windows 10, so I don't/can't know exactly how they will behave on other operating systems. I will be happy to receive Feedbacks on how they work on your OSs.
- _For libraries which are 'Windows only', I added some conditions in the GUI application, so that their respective buttons are disabled on platforms other than Windows OS._ This is to avoid Mac or Linux Users from receiving unnecessary errors.


