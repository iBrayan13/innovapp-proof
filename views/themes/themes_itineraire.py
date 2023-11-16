from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def themes_itineraire_view(page: Page):
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
                    on_click= events.go_french_themes,
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
        top= 500,
        padding= 0
    )

    return View(
        route= "/french/themes/itineraire",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/background.jpg",
                        width= 800,
                        height= 600
                    ),
                    Container(
                        Image(
                            src= "img/themes/themes_itineraire_imgs.png",
                            width= 80,
                            height= 540
                        ),
                        margin= margin.only(left=20, top= 25)
                    ),
                    Container(
                        content= Stack([
                            Column([
                                Text(
                                    "Itinéraire géographique de l'artisanat",
                                    size= 34,
                                    color= "white",
                                    font_family= "EB Garamond"
                                ),
                                Text(
                                    "Visite du Royaume a la lumiere de son artisanat\n(Contenu éditorial des experts)",
                                    size= 24,
                                    color= "orange",
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
                                                "Les caractéristiques historiques.",
                                                color="yellow",
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
                                                "Les spécificités culturelles.",
                                                color="yellow",
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
                                                "Les spécificités géographiques.",
                                                color="yellow",
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
                                                "Cartographie interactive et hyper-liens.",
                                                color="yellow",
                                                size= 18,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                    ]),
                                    width=540,
                                    height= 190,
                                    border_radius= 20,
                                    padding= 10,
                                    bgcolor= "#4D0130"
                                )
                            ])
                        ]),
                        margin= margin.only(left= 145, top= 130)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )