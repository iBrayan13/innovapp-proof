from flet import Page, View, Image, Text, Container, Stack, margin, padding
from time import sleep

def quit_view(page: Page):
    def handle_hover(e):
        e.control.on_hover = None
        for i in range(9, -1, -1):
            sleep(1)
            e.control.content.controls[1].content.value = f"Sortir en  {i}"
            e.control.update()

        page.window_close()

    body = Container(
        Stack([
            Image(
                src= "img/quit_bg.png",
                width= 800,
                height= 600
            ),
            Container(
                Text(
                    "Sortir en 10",
                    size= 30,
                    color= "white",
                    font_family= "EB Garamond"
                ),
                padding= padding.only(left= 10, bottom= 8),
                width= 160,
                height= 50,
                #bgcolor= "#4D0130",
                border_radius= 10,
                margin= margin.only(top= 515, left= 10)
            )
        ]),
        padding= 0,
        on_hover= handle_hover
    )

    return View(
        "/quit",
        [
            body
        ],
        padding= 0
    )