from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils. events import Events

def french_introduction_objectifs_view(page: Page):
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
        route= "/french/introduction/objectifs",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/introduction/introduction_objectifs.png",
                        width= 768,
                        height= 576
                    ),
                    Container(
                        content= Stack([
                            Column([
                                Image(
                                    src= "img/introduction/objectifs_title.png",
                                ),
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
                                                "Itinéraire géographique de l'artisanat, a travers la diversité des\nrégions et des cultures.",
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
                                                "Visite virtuelle des secteurs de l'artisanat.",
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
                                                "Exploration multimédia des trésors des métiers d'art.",
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
                                                ),
                                                margin= margin.only(bottom= 25)
                                            ),
                                            Text(
                                                "Reférencement des ceuvres, ou pieces universelles, a travers\nun catalogue interactif.",
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
                                                "Moteur de Rechecche multi-criteres, et connexion internet.",
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
                                                ),
                                                margin= margin.only(bottom= 25)
                                            ),
                                            Text(
                                                "Reperes économiques, liens utiles, guide practique et\ncarnet d'adresses",
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
                                                ),
                                                margin= margin.only(bottom=50)
                                            ),
                                            Text(
                                                "Plate-forme modele, prototype pour la réalisation d'un portail, a\nla fois de visibilité universelle et de commerce électronique des\nobjets d'art et de l'artisanat.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond",
                                            ),
                                        ]),
                                    ]),
                                    width=555,
                                    height= 420,
                                    padding= 10,
                                )
                            ])
                        ]),
                        margin= margin.only(left= 150, top= 45)
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
                        on_click= events.go_french_introduction,
                    ),
                ])
            )
        ],
        padding= 0
    )