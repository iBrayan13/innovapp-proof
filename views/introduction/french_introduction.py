from flet import Page, View, Stack, Container, Row, Image, Text, FontWeight, margin, MainAxisAlignment, CrossAxisAlignment
from utils.events import Events

def french_introduction_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    introduction_img = Image(
        src= "img/introduction/introduction.png",
        width= 800,
        height= 600
    )
    def handle_hover_introduction_objectifs(e):
        introduction_img.src = "img/introduction/introduction_objectifs_hover.png" if e.data == "true" else "img/introduction/introduction.png"
        page.update()
    def handle_hover_introduction_public(e):
        introduction_img.src = "img/introduction/introduction_public_hover.png" if e.data == "true" else "img/introduction/introduction.png"
        page.update()
    def handle_hover_introduction_contexte(e):
        introduction_img.src = "img/introduction/introduction_contexte_hover.png" if e.data == "true" else "img/introduction/introduction.png"
        page.update()

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
                    on_click= events.go_french_menu,
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
        route= "/french/introduction",
        controls= [
            Container(
                content= Stack(
                    [
                        Image(
                            src= "img/background.jpg",
                            width= 800,
                            height= 600
                        ),
                        introduction_img,
                        Container(
                            content= Text(
                                "Introduction",
                                font_family= "EB Garamond",
                                color= "white",
                                size= 62,
                                weight= FontWeight.W_100
                            ),
                            margin= margin.only(left= 215, top= 60)
                        ),
                        Container(
                            content= Text(
                                "Contexte",
                                font_family= "EB Garamond",
                                color= "white",
                                size= 28,
                                weight= FontWeight.W_100
                            ),
                            left= 405, 
                            top= 140,
                            width= 120,
                            height= 50,
                            on_click= events.go_french_introduction_contexte,
                        ),
                        Container(
                            content= Text(
                                "Public",
                                font_family= "EB Garamond",
                                color= "white",
                                size= 28,
                                weight= FontWeight.W_100
                            ),
                            left= 160, 
                            top= 340,
                            width= 120,
                            height= 50,
                            on_click= events.go_french_introduction_public,
                        ),
                        Container(
                            content= Text(
                                "Objectifs",
                                font_family= "EB Garamond",
                                color= "white",
                                size= 28,
                                weight= FontWeight.W_100
                            ),
                            right= 42,
                            bottom= 110,
                            width= 120,
                            height= 50,
                        ),
                        navbar,
                        Container(
                            width= 45,
                            height= 38,
                            right= 240,
                            bottom= 188,
                            on_click= events.go_french_introduction_objectifs,
                            on_hover= handle_hover_introduction_objectifs
                        ),
                        Container(
                            width= 45,
                            height= 38,
                            left= 312, 
                            top= 318,
                            on_click= events.go_french_introduction_public,
                            on_hover= handle_hover_introduction_public
                        ),
                        Container(
                            width= 38,
                            height= 38,
                            right= 298,
                            top= 220,
                            on_click= events.go_french_introduction_contexte,
                            on_hover= handle_hover_introduction_contexte
                        ),
                    ],
                ),
                width= page.width,
                height= page.height
            )
        ],
        padding= 0
    )