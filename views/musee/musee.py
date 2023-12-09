from flet import Page, View, Stack, Row, Column, Container, Image, Text, FontWeight, MainAxisAlignment, CrossAxisAlignment, margin
from utils.events import Events

def musee_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    def handle_hover(e):
        if type(e.control.content.controls[0]) == Image:
            e.control.content.controls[0].src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        else:
            e.control.content.controls[1].src = "img/menu_point_hover.png" if e.data == "true" else "img/menu_point.png"
        e.control.update()

    bg = Image(
        src= "img/musee/musee_bg.png",
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
            navbar,
            Container(
                Column(
                    [
                        Text(
                            "Base de données\nreprésentative\net informative",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_200,
                            color= "white"
                        ),
                        Image(
                            src= "img/menu_point.png",
                            width= 50,
                            height= 50
                        ),
                    ],
                ),
                top= 120,
                right= 320,
                on_click= events.go_french_musee_base,
                on_hover= handle_hover
            ),
            Container(
                Row(
                    [
                        Image(
                            src= "img/menu_point.png",
                            width= 50,
                            height= 50
                        ),
                        Text(
                            "Les trésors\nde l'Artisanat",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_200,
                            color= "white"
                        )
                    ],
                ),
                bottom= 220,
                right= 220,
                on_click= events.go_french_musee_tresors,
                on_hover= handle_hover
            ),
        ],
        width= page.width,
        height= page.height
    )

    return View(
        "/french/musee",
        [
            Container(
                content= body
            ),
        ],
        padding= 0
    )