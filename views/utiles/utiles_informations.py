from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def utiles_informations_view(page: Page):
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
        route= "/french/utiles/informations",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/utiles/utiles_informations_bg.png",
                        width= 768,
                        height= 576
                    ),
                    Container(
                        content= Stack([
                            Container(
                                Column([
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Guide des musées.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Evénements et dates du tourisme national.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Prix homologués du Ministere de l'Artisanat et du Tourisme.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Conseils supplémentaires et carnet d'adresses.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Bibliographies.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Lexique.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                    Row([
                                        Container(
                                            Image(
                                                src= "img/menu_point.png",
                                                width= 30,
                                                height= 30,
                                            )
                                        ),
                                        Text(
                                            "Index.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                ]),
                                width=540,
                                height= 290,
                                padding= 10,
                            )
                        ]),
                        margin= margin.only(left= 175, top= 145)
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
                        on_click= events.go_french_utiles,
                    ),
                ])
            )
        ],
        padding= 0
    )