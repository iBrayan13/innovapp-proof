from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def musee_base_maison_view(page: Page):
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
                    on_click= events.go_french_musee_base,
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
        route= "/french/musee/base/maison",
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
                            src= "img/musee/musee_base_maison_imgs.png",
                            width= 80,
                            height= 540
                        ),
                        margin= margin.only(left=20, top= 25)
                    ),
                    Container(
                        content= Stack([
                            Column([
                                Text(
                                    "Les arts de la maison et du quotidien",
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
                                                    "Le Tapis.",
                                                    color="yellow",
                                                    size= 20,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
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
                                                    "La poterie.",
                                                    color="yellow",
                                                    size= 20,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
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
                                                    "La céramique.",
                                                    color="yellow",
                                                    size= 20,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
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
                                                    "La vannerie.",
                                                    color="yellow",
                                                    size= 20,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
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
                                                    "La marqueterie.",
                                                    color="yellow",
                                                    size= 20,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
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
                                                    "Le Thuya.",
                                                    color="yellow",
                                                    size= 20,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
                                        ),
                                    ]),
                                    width= 210,
                                    height= 255,
                                    border_radius= 20,
                                    padding= 10,
                                    bgcolor= "#4D0130"
                                )
                            ])
                        ]),
                        margin= margin.only(left= 145, top= 110)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )