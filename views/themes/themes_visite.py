from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def themes_visite_view(page: Page):
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
        route= "/french/themes/visite",
        controls= [
            Container(
                content= Stack(
                    [
                        Image(
                            src= "img/themes/themes_visite_bg.png",
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
                                                "Des métiers millénaires au présent",
                                                color="#CECE63",
                                                size= 18,
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
                                                        "Les maítres-tanneurs.",
                                                        color="#CECE63",
                                                        size= 15,
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
                                                        "Les maítres zellijeurs.",
                                                        color="#CECE63",
                                                        size= 15,
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
                                                        "Les maítres ebénistes.",
                                                        color="#CECE63",
                                                        size= 15,
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
                                                        "Les maítres céramistes.",
                                                        color="#CECE63",
                                                        size= 15,
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
                                                        "Les maítres-tisserands.",
                                                        color="#CECE63",
                                                        size= 15,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                            ], spacing= 2),
                                            margin= margin.only(left= 40)
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
                                                "Cartographie utile des quartiers de l'artisanat\n(Des principalesvilles du Royaume)",
                                                color="#CECE63",
                                                size= 18,
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
                                                        "Fiches synoptiques des lieux de commerce.",
                                                        color="#CECE63",
                                                        size= 15,
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
                                                        "Bazars, ateliers et boutiques.",
                                                        color="#CECE63",
                                                        size= 15,
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
                                                        "Antiquares.",
                                                        color="#CECE63",
                                                        size= 15,
                                                        font_family= "EB Garamond"
                                                    ),
                                                ]),
                                            ], spacing= 2),
                                            margin= margin.only(left= 40)
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
                                                "Hyper-liens avec la Base de données genérale.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                    ], spacing= 3),
                                    width= 530,
                                    height= 398,
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
                            on_click= events.go_french_themes,
                        ),
                    ]
                )
            )
        ],
        padding= 0
    )