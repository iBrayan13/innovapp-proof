from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils. events import Events

def eartisanat_simulation_view(page: Page):
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
                    on_click= events.go_french_eartisanat,
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
        route= "/french/eartisanat/simulation",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/eartisanat/eartisanat_simulation_bg.png",
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
                                            ),
                                            margin= margin.only(bottom= 25)
                                        ),
                                        Text(
                                            "Le musée virtuel propose un menu de CAO pour la décoration\ninteractive.",
                                            color="#CCC424",
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
                                            "Des modeles d'habitat, afin d'essayer diverses proposition de Design.",
                                            color="#CCC424",
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
                                            ),
                                            margin= margin.only(bottom= 25)
                                        ),
                                        Text(
                                            "Des produits de l'Artisanat comme Menu d'agencement et\nd'embellissement.",
                                            color="#CCC424",
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
                                            "De l'architecture et des éléments de décoration au bout de la souris.",
                                            color="#CCC424",
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
                                            ),
                                            margin= margin.only(bottom= 25)
                                        ),
                                        Text(
                                            "Une base de données multi-criteres controle l'importation les objets\net leur agencement.",
                                            color="#CCC424",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                ]),
                                width=565,
                                height= 295,
                                padding= 10,
                            )
                        ]),
                        margin= margin.only(left= 175, top= 140)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )