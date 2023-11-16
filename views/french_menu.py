from flet import Page, View, Stack, Container, Row, Image, Text, MainAxisAlignment, CrossAxisAlignment
from utils.events import Events

def french_menu_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    navbar_img = Image(
        src= "img/retour_btn.png"
    )

    def handle_hover_navbar_left(e):
        navbar_img.src = "img/retour_btn_hover.png" if e.data == "true" else "img/retour_btn.png"
        page.update()

    navbar = Container(
        content= Stack([
            Row([
                Container(
                    Text("Retour", font_family= "EB Garamond", color= "white", size= 18),
                    on_click= events.go_home,
                    padding= 0,
                    on_hover= handle_hover_navbar_left
                ),
                navbar_img,
            ], spacing= 0)
        ]),
        right= 15,
        bottom= 10,
        padding= 0
    )

    def handle_hover(e):
        e.control.content.controls[0].src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        e.control.update()

    return View(
        route= "/french/menu",
        controls= [
            Container(
                content= Stack(
                    [
                        Image(
                                src= "img/background.jpg",
                                width= 800,
                                height= 600
                        ),
                        Stack([
                            Container(
                                Row(
                                    [
                                        Image(
                                            src= "img/menu_point.png",
                                            width= 30,
                                            height= 30
                                        ),
                                        Text("Introduction", font_family= "EB Garamond", color= "white", size= 18),
                                    ]
                                ),
                                on_click= events.go_french_introduction,
                                left= 305,
                                top= 135,
                                on_hover= handle_hover
                            ),
                            Container(
                                Row(
                                    [
                                        Image(
                                            src= "img/menu_point.png",
                                            width= 30,
                                            height= 30
                                        ),
                                        Text("Thémes", font_family= "EB Garamond", color= "white", size= 18),
                                    ]
                                ),
                                on_click= events.go_french_themes,
                                left= 420,
                                top= 180,
                                on_hover= handle_hover
                            ),
                            Container(
                                Row(
                                    [
                                        Image(
                                            src= "img/menu_point.png",
                                            width= 30,
                                            height= 30
                                        ),
                                        Text("Musée Virtuel", font_family= "EB Garamond", color= "white", size= 18),
                                    ]
                                ),
                                left= 473,
                                top= 265,
                                on_click= events.go_french_musee,
                                on_hover= handle_hover
                            ),
                            Container(
                                Row(
                                    [
                                        Image(
                                            src= "img/menu_point.png",
                                            width= 30,
                                            height= 30
                                        ),
                                        Text("Tapis Project Pilote", font_family= "EB Garamond", color= "white", size= 18),
                                    ]
                                ),
                                left= 476,
                                bottom= 175,
                                on_hover= handle_hover,
                                on_click= events.go_french_tapis
                            ),
                            Container(
                                Row(
                                    [
                                        Image(
                                            src= "img/menu_point.png",
                                            width= 30,
                                            height= 30
                                        ),
                                        Text("E-Artisanat", font_family= "EB Garamond", color= "white", size= 18),
                                    ]
                                ),
                                left= 415,
                                bottom= 90,
                                on_click= events.go_french_eartisanat,
                                on_hover= handle_hover
                            ),
                            Container(
                                Row(
                                    [
                                        Image(
                                            src= "img/menu_point.png",
                                            width= 30,
                                            height= 30
                                        ),
                                        Text("Liens utiles", font_family= "EB Garamond", color= "white", size= 18),
                                    ]
                                ),
                                left= 305,
                                bottom= 49,
                                on_click= events.go_french_utiles,
                                on_hover= handle_hover
                            ),
                        ]),
                        navbar
                    ],
                    width= page.width,
                    height= page.height
                )
            )
        ],
        padding= 0
    )