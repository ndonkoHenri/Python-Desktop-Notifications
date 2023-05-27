import flet as ft
import utils


def main(page: ft.Page):
    page.title = "Flet Notifications - TheEthicalBoy"
    is_windows = page.platform == "windows"
    page.window_always_on_top = True
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "light"
    page.scroll = "auto"
    page.window_min_height, page.window_min_width = 371, 542
    page.window_height, page.window_width = 434, 595
    page.window_center()

    def show(e):
        if e.control.data == 1:
            page.show_snack_bar(ft.SnackBar(ft.Text("Running engine `plyer`..."), open=True))
            utils.notif_with_plyer(title_field.value, message_field.value)
        elif e.control.data == 2:
            page.show_snack_bar(ft.SnackBar(ft.Text("Running engine `notifpy`..."), open=True))
            utils.notif_with_notifpy(title_field.value, message_field.value)
        elif e.control.data == 3:
            page.show_snack_bar(ft.SnackBar(ft.Text("Running engine `pynotifier`..."), open=True))
            utils.notif_with_pynotifier(title_field.value, message_field.value)
        elif e.control.data == 4:
            page.show_snack_bar(ft.SnackBar(ft.Text("Running engine `win10toast`..."), open=True))
            utils.notif_with_win10toast(title_field.value, message_field.value)
        elif e.control.data == 5:
            page.show_snack_bar(ft.SnackBar(ft.Text("Running engine `win10toast_click`..."), open=True))
            utils.notif_with_win10toast_click(title_field.value, message_field.value)

    page.add(
        ft.Row(
            controls=[
                title_field := ft.TextField(
                    value="Ethical Title :)",
                    label="title",
                    width=210,
                    border=ft.InputBorder.UNDERLINE,
                    keyboard_type=ft.KeyboardType.TEXT,
                ),
                ft.Text("--", weight=ft.FontWeight.BOLD),
                message_field := ft.TextField(
                    value="Flet Notifications by TheEthicalBoy",
                    label="message",
                    width=260,
                    border=ft.InputBorder.UNDERLINE,
                    keyboard_type=ft.KeyboardType.TEXT,
                )
            ],
            # wrap=True,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Column(
            controls=[
                ft.FilledTonalButton(
                    "Show 'plyer' Notification",
                    data=1,
                    on_click=show
                ),
                ft.FilledTonalButton(
                    "Show 'notifpy' Notification",
                    data=2,
                    on_click=show
                ),
                ft.FilledTonalButton(
                    "Show 'pynotifier' Notification",
                    data=3,
                    on_click=show
                ),
                ft.FilledTonalButton(
                    "Show 'win10toast' Notification",
                    data=4, on_click=show,
                    disabled=not is_windows
                ),
                ft.FilledTonalButton(
                    "Show 'win10toast_click' Notification",
                    data=5,
                    on_click=show,
                    disabled=not is_windows
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    )


ft.app(target=main)
