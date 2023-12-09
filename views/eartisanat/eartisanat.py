from flet import Page, View, Stack, Row, Column, Container, Image, Text, FontWeight, MainAxisAlignment, CrossAxisAlignment, margin
from utils.events import Events

def eartisanat_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    def handle_hover(e):
        e.control.content.controls[0].src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        e.control.update()
    
    def handle_hover_container(e):
        e.control.content.controls[0].content.src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        e.control.update()

    bg = Image(
        src= "img/eartisanat/eartisanat_bg.png",
        width= 768,
        height= 576
    )
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

    body = Stack(
        [
            bg,
            navbar,
            Container(
                Row(
                    [
                        Image(
                            src= "img/menu_point.png",
                            width= 30,
                            height= 30
                        ),
                        Text(
                            "Simulation de maison marocaine en 3D",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_500,
                            color= "white"
                        )
                    ],
                ),
                top= 180,
                left= 100,
                on_click= events.go_french_eartisanat_simulation,
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
                        Text(
                            "Connexion Internet",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_500,
                            color= "white"
                        ),
                    ],
                ),
                top= 240,
                left= 100,
                on_click= events.go_french_eartisanat_connexion,
                on_hover= handle_hover
            ),
            Container(
                Row(
                    [
                        Container(
                            Image(
                                src= "img/menu_point.png",
                                width= 30,
                                height= 30
                            ),
                            margin= margin.only(bottom= 30)
                        ),
                        Text(
                            "Solutions de Ecommerce\net Commande en ligne",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_500,
                            color= "white"
                        ),
                    ],
                ),
                top= 300,
                left= 100,
                on_click= events.go_french_eartisanat_solutions,
                on_hover= handle_hover_container
            ),
        ],
        width= page.width,
        height= page.height
    )

    return View(
        "/french/eartisanat",
        [
            Container(
                content= body
            ),
        ],
        padding= 0
    )