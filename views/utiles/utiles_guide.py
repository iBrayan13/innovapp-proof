from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def utiles_guide_view(page: Page):
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
                    on_click= events.go_french_utiles,
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
        route= "/french/utiles/guide",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/utiles/utiles_guide_bg.png",
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
                                            "Institutions de tutelle et organismes convergents.",
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
                                            "Evénements, dates, expositions nationales et internationales.",
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
                                            "Informations sur le commerces électroniques et sites utiles.",
                                            color="#CECE63",
                                            size= 18,
                                            font_family= "EB Garamond"
                                        ),
                                    ]),
                                ]),
                                width=540,
                                height= 130,
                                padding= 10,
                            )
                        ]),
                        margin= margin.only(left= 175, top= 180)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )