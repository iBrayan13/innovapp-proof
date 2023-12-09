from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def musee_tresors_savoir_view(page: Page):
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
        right= 88,
        bottom= 26,
        padding= 0
    )

    return View(
        route= "/french/themes/visite",
        controls= [
            Container(
                content= Stack(
                    [
                        Image(
                            src= "img/musee/tresors_savoir_bg.png",
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
                                                "La splendeur de l'habit, racontée par la soie.",
                                                color="#CECE63",
                                                size= 16,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        Container(
                                            Column([
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Typologies.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Muséographie.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Notices et Catalogue.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                            ], spacing= 0),
                                            margin= margin.only(left= 40),
                                            padding= 0
                                        ),
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                ),
                                                margin= margin.only(bottom= 23)
                                            ),
                                            Text(
                                                "Le témoignage des parures\nL'histoire se fait présent par la magie de l'or et de l'argent.",
                                                color="#CECE63",
                                                size= 16,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        Container(
                                            Column([
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Typologies.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Muséographie.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Notices et Catalogue.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                            ], spacing= 0),
                                            margin= margin.only(left= 40),
                                            padding= 0
                                        ),
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les instruments de musique.",
                                                color="#CECE63",
                                                size= 16,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        Container(
                                            Column([
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Typologies par régions , écoles et traditions.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Muséographie.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Notices et Catalogue.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                            ], spacing= 0),
                                            margin= margin.only(left= 40),
                                            padding= 0
                                        ),
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "Les plaisirs du corps et de l'esprit.",
                                                color="#CECE63",
                                                size= 16,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        Container(
                                            Column([
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Les arts de la table.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Les objets d'art au quotidien.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Les supports de la lumiere.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                                Row([
                                                    Container(
                                                        Image(
                                                            src= "img/menu_point.png",
                                                            width= 15,
                                                            height= 15,
                                                        )
                                                    ),
                                                    Text(
                                                        "Les supports des parfums.",
                                                        color="#CECE63",
                                                        size= 14,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                            ], spacing= 0),
                                            margin= margin.only(left= 40),
                                            padding= 0
                                        ),
                                    ], spacing= 1),
                                    width= 530,
                                    height= 450,
                                    padding= 6,
                                )
                            ]),
                            margin= margin.only(left= 175, top= 130)
                        ),
                        navbar,
                        Container(
                            right= 22,
                            bottom= 26,
                            width= 143,
                            height= 40,
                            on_hover= handle_hover_navbar_right,
                            on_click= events.go_home,
                        ),
                        Container(
                            right= 185,
                            bottom= 26,
                            width= 123,
                            height= 40,
                            on_hover= handle_hover_navbar_left,
                            on_click= events.go_french_musee_tresors,
                        ),
                    ]
                )
            )
        ],
        padding= 0
    )