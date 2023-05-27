# pip install win10toast_click --> https://github.com/vardecab/win10toast-click
import win10toast_click
import webbrowser

# pip install notify-py --> https://github.com/ms7m/notify-py
import notifypy

# pip install plyer --> https://github.com/kivy/plyer
import plyer

# pip install win10toast --> https://github.com/jithurjacob/Windows-10-Toast-Notifications
import win10toast

# pip install py-notifier  --> https://github.com/YuriyLisovskiy/pynotifier
import pynotifier
from pynotifier.backends import platform

# import notify2  # this is for the commented code block at the enbottom - I got some dbus errors while running it

# some defaults just in case
default_title = "Ethical Title :)"
default_message = "This is a very long description written by TheEthicalBoy :-)"


def notif_with_win10toast_click(title: str = default_title, message: str = default_message):
    """
    Sends a notification using the win10toast_click engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    Note:
        Works only on the Windows OS.
    """

    def click_callback():
        """
        Called/fired when the user clicks on the notification banner/toast.
        Use it to run some other code block. Ex: open a web page
        """
        try:
            webbrowser.open("https://github.com/ndonkoHenri/Flet-Samples", autoraise=True)
        except:
            print('Failed to open URL :(')

    toaster = win10toast_click.ToastNotifier()

    # show up notification
    toaster.show_toast(
        title,
        message,
        icon_path="test_images/ico_test_image.ico",  # .ico image file
        duration=10,  # notification timeout; None = leave notification in Notification Center
        threaded=True, # True: spawns a separate thread inorder not to block the main app thread
        callback_on_click=click_callback  # function to run when notification is clicked
    )


def notif_with_notifpy(title: str = default_title, message: str = default_message):
    """
    Sends a notification using the notif-py engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    Note:
        Cross-Platform: could be used on any OS.
    """
    notification = notifypy.Notify(enable_logging=True)
    notification.application_name = "Notify-py Notif"
    notification.title = title
    notification.message = message
    notification.urgency = "critical"  # 'low', 'normal' or 'critical'
    notification.icon = "test_images/png_test_image.png"
    notification.application_name = "Flet Notification - TheEthicalBoy"

    notification.send(block=False)  # block= False is to not block the main application thread


def notif_with_plyer(title: str = default_title, message: str = default_message):
    """
    Sends a notification using the plyer engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    """
    plyer.notification.notify(
        app_name="Plyer Notif",
        title=title,
        message=message,
        app_icon="test_images/ico_test_image.ico",  # On Windows, the icon must be .ico
        timeout=10,  # For how long the notification should be shown
    )


def notif_with_win10toast(title: str = default_title, message: str = default_message):
    """
    Sends a notification using the win10toast engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    Note:
        Works only on the Windows OS.
    """

    toaster = win10toast.ToastNotifier()
    toaster.show_toast(
        title=title,
        msg=message,
        icon_path="test_images/ico_test_image.ico",
        duration=10
    )


def notif_with_pynotifier(title: str = default_title, message: str = default_message):
    """
    Sends a notification using the pynotifier engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    Note:
        Cross-Platform: could be used on any OS.
    """
    c = pynotifier.NotificationClient()
    c.register_backend(platform.Backend())

    notification = pynotifier.Notification(
        title=title,
        message=message,
        icon_path='test_images/ico_test_image.ico',
        duration=5,
        keep_alive=True,  # keep toast alive in System Tray whether it was clicked or not
        threaded=True   # spawns a separate thread inorder not to block the main app thread
    )

    c.notify_all(notification)


# This should also work, but I got a 'dbus error' when executing this code block
'''def notif_with_notify2(title: str = default_title, message: str = default_message):
    """
    Sends a notification using the win10toast engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    """
    # initialise the d-bus connection
    notify2.init("Flet Notification - By TheEthicalBoy")
    n = notify2.Notification(title, message, icon="png_test_image.png")  # create Notification object
    n.set_urgency(1)
    n.set_timeout(10000)  # set timeout for a notification - in milliseconds
    n.show()
'''


def main():
    notif_with_win10toast_click("Hello, Win10ToastClick!")
    notif_with_win10toast("Hello, Win10Toast!")
    notif_with_pynotifier("Hello, Pynotifier!")
    notif_with_plyer("Hello, Plyer!")
    notif_with_notifpy("Hello, Notify-Py!")
    # notif_with_notify2()


if __name__ == "__main__":
    main()
