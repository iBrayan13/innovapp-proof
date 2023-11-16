from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def musee_tresors_chevalerie_view(page: Page):
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
        top= 500,
        padding= 0
    )

    return View(
        route= "/french/musee/tresors/chevalerie",
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
                            src= "img/musee/musee_tresors_chevalerie_imgs.png",
                            width= 80,
                            height= 540
                        ),
                        margin= margin.only(left=20, top= 25)
                    ),
                    Container(
                        content= Stack([
                            Column([
                                Text(
                                    "L'Univers de la Chevalerie",
                                    size= 32,
                                    color= "white",
                                    font_family= "EB Garamond"
                                ),
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
                                                    "Les armures.",
                                                    color="yellow",
                                                    size= 18,
                                                    font_family= "EB Garamond"
                                                ),
                                            ])
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
                                                    "Les armes nobles.",
                                                    color="yellow",
                                                    size= 18,
                                                    font_family= "EB Garamond"
                                                ),
                                            ])
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
                                                    "Les armes a feu.",
                                                    color="yellow",
                                                    size= 18,
                                                    font_family= "EB Garamond"
                                                ),
                                            ])
                                        ),
                                    ]),
                                    width= 270,
                                    height= 135,
                                    border_radius= 20,
                                    padding= 10,
                                    bgcolor= "#4D0130"
                                )
                            ])
                        ]),
                        margin= margin.only(left= 145, top= 160)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )