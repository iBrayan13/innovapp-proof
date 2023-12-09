from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils. events import Events

def french_introduction_contexte_view(page: Page):
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
                    on_click= events.go_french_introduction,
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
        route= "/french/introduction/contexte",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/introduction/introduction_contexte_bg.png",
                        width= 768,
                        height= 576
                    ),
                    Container(
                        content= Stack([
                            Column([
                                Image(
                                    src= "img/introduction/contexte_title.png",
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
                                                margin= margin.only(bottom= 75)
                                            ),
                                            Text(
                                                "Les outils multimédia inventent un nouveau langage d'expression:\nSomme subtile du livre, du cinéma et de la musique, ce Musée\nentend exprimer une tradition millénaire a travers l'ingéniosité du\nlangage multimédia.",
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
                                                margin= margin.only(bottom= 50)
                                            ),
                                            Text(
                                                "Rendre hommage au génie créateur de l'artisan marocain a travers\nune tradition unique, de par la richesse et l'ingéniosité de ses\nmétiers, de son savoir-faire et de ses prodiuts.",
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
                                                margin= margin.only(bottom= 70)
                                            ),
                                            Text(
                                                "La médiatisation de l'artisanat marocain, via les nouveaux supports\n électroniques, constitue une pierre angulaire dans la stratégie du\nGouvernement visant la mise a niveau du secteur et la promotion du\n produit national.",
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
                                                margin= margin.only(bottom= 50)
                                            ),
                                            Text(
                                                "A l'heure de la mondialisation, la mise en place des infrastructures\ndu commerce électronique implique, a l'amont, une stratégie média\n basée sur les supports de la Societé de l'information.",
                                                color="#CECE63",
                                                size= 18,
                                                font_family= "EB Garamond"
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
                    navbar
                ])
            )
        ],
        padding= 0
    )