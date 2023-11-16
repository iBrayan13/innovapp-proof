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
            Row([
                Container(
                    Text("Retour", font_family= "EB Garamond", color= "white", size= 18),
                    on_click= events.go_french_musee_tresors,
                    padding= 0,
                    on_hover= handle_hover_navbar_left
                ),
                navbar_img,
                Container(
                    Text("Principal", font_family= "EB Garamond", color= "white", size= 18),
                    on_click= events.go_home,
                    padding= 0,
                    on_hover= handle_hover_navbar_right
                )
            ], spacing= 0)
        ]),
        left= 420,
        bottom= 30,
        padding= 0
    )

    return View(
        route= "/french/themes/visite",
        controls= [
            Container(
                content= Stack(
                    [
                        Image(
                            src= "img/background.jpg",
                            width= 800,
                            height= 600
                        ),
                        Container(
                            Image(
                                src= "img/musee/musee_tresors_savoir_imgs.png",
                                width= 80,
                                height= 540
                            ),
                            margin= margin.only(left=20, top= 25)
                        ),
                        Container(
                            content= Stack([
                                Column([
                                    Text(
                                        "L'Univers du Savoir-etre",
                                        size= 32,
                                        color= "white",
                                        font_family= "EB Garamond"
                                    ),
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
                                                    color="yellow",
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
                                                            "Typologies.",
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                    color="yellow",
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
                                                            "Typologies.",
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                            color="yellow",
                                                            size= 10,
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
                                                    color="yellow",
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
                                                            "Typologies par régions , écoles et traditions.",
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                    color="yellow",
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
                                                            "Les arts de la table.",
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                            color="yellow",
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
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                ], spacing= 0),
                                                margin= margin.only(left= 40),
                                                padding= 0
                                            ),
                                        ], spacing= 5),
                                        width= 530,
                                        height= 450,
                                        border_radius= 20,
                                        padding= 6,
                                        bgcolor= "#4D0130"
                                    )
                                ])
                            ]),
                            margin= margin.only(left= 145, top= 15)
                        ),
                        navbar
                    ]
                )
            )
        ],
        padding= 0
    )