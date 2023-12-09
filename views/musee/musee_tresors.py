from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def musee_tresors_view(page: Page):
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
                    on_click= events.go_french_musee,
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

    def handle_hover(e):
        e.control.content.controls[0].content.src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        e.control.update()

    return View(
        route= "/french/musee/tresors",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/musee/musee_tresors_bg.png",
                        width= 768,
                        height= 576
                    ),
                    Container(
                        content= Stack([
                            Container(
                                Column([
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "L'Univers des Sciences",
                                                color="#CECE63",
                                                size= 20,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        on_click = events.go_french_musee_tresors_sciences,
                                        on_hover= handle_hover
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "L'Univers de la Chevalerie",
                                                color="#CECE63",
                                                size= 20,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        on_click= events.go_french_musee_tresors_chevalerie,
                                        on_hover= handle_hover
                                    ),
                                    Container(
                                        Row([
                                            Container(
                                                Image(
                                                    src= "img/menu_point.png",
                                                    width= 30,
                                                    height= 30,
                                                )
                                            ),
                                            Text(
                                                "L'Univers du Savoir-etre",
                                                color="#CECE63",
                                                size= 20,
                                                font_family= "EB Garamond"
                                            ),
                                        ]),
                                        on_click= events.go_french_musee_tresors_savoir,
                                        on_hover= handle_hover
                                    ),
                                ]),
                                width= 310,
                                height= 135,
                                padding= 10,
                            )
                        ]),
                        margin= margin.only(left= 175, top= 160)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )