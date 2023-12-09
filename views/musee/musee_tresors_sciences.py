from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def musee_tresors_sciences_view(page: Page):
    events = Events(page)

    navbar_img = Image(
        src= "img/navbar.png"
    )

    def handle_hover_navbar_left(e):
        navbar_img.src = "img/navbar_left_hover.png" if e.data == "true" else "img/navbar.png"
        page.update()
    def handle_hover_navbar_right(e):
        navbar_img.src = "img/navbar_right_hover.png" if e.data == "true" else "img/navbar.png"
        page.update()

    navbar = Container(
        content= Stack([
            navbar_img,
        ]),
        right= 90,
        bottom= 23,
        padding= 0
    )

    return View(
        route= "/french/musee/tresors/sciences",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/musee/tresors_sciences_bg.png",
                        width= 768,
                        height= 576
                    ),
                    Container(
                        content= Stack([
                            Container(
                                Column([
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Le saint livre du Coran.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ])
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les Rarae ou manuscrits rares.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ])
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les enluminures.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ])
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les manuscrits miniatures.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ])
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les instruments de mesure.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ])
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les horloges et les Astrolabes.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ])
                                    ),
                                ]),
                                width= 315,
                                height= 260,
                                padding= 10,
                            )
                        ]),
                        margin= margin.only(left= 175, top= 160)
                    ),
                    navbar,
                    Container(
                        right= 22,
                        bottom= 24,
                        width= 143,
                        height= 40,
                        on_hover= handle_hover_navbar_right,
                        on_click= events.go_home,
                    ),
                    Container(
                        right= 185,
                        bottom= 24,
                        width= 123,
                        height= 40,
                        on_hover= handle_hover_navbar_left,
                        on_click= events.go_french_musee_tresors,
                    ),
                ])
            )
        ],
        padding= 0
    )