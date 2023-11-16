from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def eartisanat_connexion_view(page: Page):
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
        route= "/french/eartisanat/connexion",
        controls= [
            Container(
                content= Stack([
                    Image(
                        src= "img/background.jpg",
                        width= 800,
                        height= 600
                    ),
                    Container(
                        content= Stack([
                            Column([
                                Text(
                                    "Connexion Internet",
                                    size= 32,
                                    color= "white",
                                    font_family= "EB Garamond"
                                ),
                                Container(
                                    width= 270,
                                    height= 140,
                                    border_radius= 20,
                                    padding= 10,
                                    #bgcolor= "#4D0130"
                                )
                            ])
                        ]),
                        margin= margin.only(left= 145, top= 50)
                    ),
                    navbar
                ])
            )
        ],
        padding= 0
    )