from flet import Page, View, Stack, Container, Row, Column, Image, Text, FontWeight, margin
from utils.events import Events

def french_view(page: Page):
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
                    Text("Principal", font_family= "EB Garamond", color= "white", size= 18),
                    on_click= events.go_home,
                    padding= 0,
                    on_hover= handle_hover_navbar_left
                ),
                navbar_img,
                Container(
                    Text("Contenu", font_family= "EB Garamond", color= "white", size= 18),
                    on_click= events.go_french_menu,
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
        route= "/french",
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
                            content= Image(
                                src= "img/title.png",
                                width= 400,
                                height= 200
                            ),
                            margin= margin.only(left= 180, top= 50)
                        ),
                        Container(
                            content= Stack([
                                Row(controls= [
                                    Column(controls= [
                                        Text(
                                            value= "Objet",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                        Text(
                                            value= "Theme",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                        Text(
                                            value= "Delivrable",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                        Text(
                                            value= "Commanditaire",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                    ]),
                                    Column(controls= [
                                        Text(
                                            value= "Axes formateurs du futur portail de l'Artisanat",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                        Text(
                                            value= "Trésors de l'artisanat du Royaume du Maroc",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                        Text(
                                            value= "Maquette du musée virtuel du tapis",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        ),
                                        Text(
                                            value= "Département de l'Artisanat et de l'Economie\nSociale, Ministere de l'Artisanat, Royaume du\nMaroc",
                                            font_family= "EB Garamond",
                                            color= "#CCC424",
                                            size= 20,
                                            weight= FontWeight.W_600,
                                        )
                                    ]),
                                ]),
                            ]),
                            margin= margin.only(left= 110, top= 270),
                            width=548,
                            height= 220,
                            border_radius= 20,
                            padding= 10,
                            bgcolor= "#4D0130"
                        ),
                        navbar
                    ],
                    width= 800,
                    height= 600
                )
            ),
        ],
        padding= 0
    )