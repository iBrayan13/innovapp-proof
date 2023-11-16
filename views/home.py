from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin, MainAxisAlignment, CrossAxisAlignment
from utils.events import Events

def home_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    def handle_hover(e):
        e.control.content.controls[0].src = "img/quit_btn_hover.png" if e.data == "true" else "img/quit_btn.png"
        e.control.update()

    def handle_hover_lang(e):
        e.control.content.controls[1].src = "img/language_btn_hover.png" if e.data == "true" else "img/language_btn.png"
        e.control.update()

    return View(
        route= "/home",
        controls= [
            Container(
                Stack([
                    Image(
                        src= "img/background.jpg",
                        width= 800,
                        height= 600
                    ),
                    Container(
                        Image(
                            src= "img/title.png",
                            width= 400,
                            height= 200
                        ),
                        margin= margin.only(left= 180, top= 50)
                    ),
                    Container(
                        Row([
                            Text(
                                "Français",
                                font_family= "EB Garamond",
                                size= 20,
                                color= "white"
                            ),
                            Image(
                                src= "img/language_btn.png",
                                width= 100,
                                height= 100
                            ),
                        ]),
                        on_click= events.go_french,
                        on_hover= handle_hover_lang,
                        right= 10, 
                        bottom= 35
                    ),
                    Container(
                        Column([
                            Image(
                                src= "img/quit_btn.png",
                                width= 75,
                                height= 100
                            ),
                            Text(
                                "Quitter",
                                color= "orange",
                                size= 20,
                                font_family= "EB Garamond"
                            )
                        ], spacing= 5, height= 140),
                        on_click= events.go_quit,
                        ink= False,
                        on_hover= handle_hover,
                        left= 15,
                        bottom= 35
                    )
                ])
            ),
        ],
        padding= 0
    )