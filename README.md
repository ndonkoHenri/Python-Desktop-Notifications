# Python Desktop Notifications

The Blog Post to this could be found [here](https://ndonkohenri.medium.com/sending-desktop-notifications-in-python-flet-97f0834f993d).

## Description

This repo is meant to expose the various ways one could send desktop notifications using python.
I went through some available python projects to send desktop notifications, and came up this List and also built a GUI app (with [Flet](https://flet.dev)) to compile all of them on one area.

## Some Captures
- GUI application ran on windows:

![gui-application-python-desktop-notification](https://github.com/ndonkoHenri/Python-Desktop-Notifications/assets/98978078/d7ac5fe6-237a-4704-9690-6f2542d0ec66)

- Notfication sent with Plyer

![notif_plyer](https://github.com/ndonkoHenri/Python-Desktop-Notifications/assets/98978078/46171908-db5f-4cd7-bc8e-018a3c84391e)


I will keep this repo updated once I find any other python notification library. Please, feel free to make suggestions too :)

### Libraries 

- **[Plyer](https://github.com/kivy/plyer)** - Cross platform
- **[notify-py](https://github.com/ms7m/notify-py)** - Cross Platform
- **[Pynotifier](https://github.com/YuriyLisovskiy/pynotifier)** - Cross platform
- **[win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)** - Windows only
- **[win10toast_click](https://github.com/vardecab/win10toast-click)** - Windows only

To install the packages, you could make use of this command:

```bash
pip install -r requirements.txt
```
## Code Structure
- `main.py`: contains the code for the flet-made GUI application;
- `utils.py`: contains the how-to-use code for each notification engine mentioned above;
- `test_images` folder: contains images used used in `utils.py`


## Note
- I tested these libraries only on Windows 10, so I don't/can't know exactly how they will behave on other operating systems. I will be happy to receive Feedbacks on how they work on your OSs.
- _For libraries which are 'Windows only', I added some conditions in the GUI application, so that their respective buttons are disabled on platforms other than Windows OS._ This is to avoid Mac or Linux Users from receiving unnecessary errors.


