from flet import Page, View, Image, Container, Stack, Text, TextAlign, MainAxisAlignment, CrossAxisAlignment
from time import sleep

def intro_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    def go_home(e):
        e.control.on_hover = None
        for i in range(4, -1, -1):
            sleep(1)
            e.control.content.controls[1].value = f"{i}"
            page.update()

        page.go("/home")

    bg = Image(
            src= "img/intro_bg.png",
            width= 800,
            height= 600,
        )

    body = Container(
        content= Stack([
            bg,
            Text(
                value= "5",
                font_family= "EB Garamond",
                size= 28,
                color= "white",
                text_align= TextAlign.CENTER,
                left= 375,
                bottom= 40
            ),
        ]),
        padding= 0,
        on_hover= go_home
    )

    return View(
            "/",
            [
                body
            ],
            padding= 0
        )