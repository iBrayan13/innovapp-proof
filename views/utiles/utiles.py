from flet import Page, View, Stack, Row, Column, Container, Image, Text, FontWeight, MainAxisAlignment, CrossAxisAlignment, margin
from utils.events import Events

def utiles_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    def handle_hover(e):
        e.control.content.controls[0].src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        e.control.update()

    bg = Image(
        src= "img/background.jpg",
        width= 800,
        height= 600
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
            Text(
                "Liens utiles",
                size= 48,
                weight= FontWeight.W_200,
                color= "white",
                top= 15,
                left= 60,
                font_family= "EB Garamond"
            ),
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
                            "Guide pour les professionnels et pour le grand public",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_500,
                            color= "white"
                        )
                    ],
                ),
                top= 200,
                left= 70,
                on_click= events.go_french_utiles_guide,
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
                            "Informations pratiques",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_500,
                            color= "white"
                        ),
                    ],
                ),
                top= 260,
                left= 70,
                on_click= events.go_french_utiles_informations,
                on_hover= handle_hover
            ),
        ],
        width= page.width,
        height= page.height
    )

    return View(
        "/french/utiles",
        [
            Container(
                content= body
            ),
        ],
        padding= 0
    )