from flet import Page, View, Stack, Row, Column, Container, Image, Text, FontWeight, MainAxisAlignment, CrossAxisAlignment, margin
from utils.events import Events

def themes_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    def handle_hover(e):
        if type(e.control.content.controls[0]) == Image:
            e.control.content.controls[0].src = "img/themes/themes_point_hover.png" if e.data == "true" else "img/themes/themes_point.png"
        elif type(e.control.content.controls[1]) == Image:
            e.control.content.controls[1].src = "img/themes/themes_point_hover.png" if e.data == "true" else "img/themes/themes_point.png"
        else:
            e.control.content.controls[1].content.src = "img/themes/themes_point_hover.png" if e.data == "true" else "img/themes/themes_point.png"

        e.control.update()
        
    bg = Image(
        src= "img/themes/themes_bg.png",
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
                            "L'artisanat\ncomme culture",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_200,
                            color= "orange"
                        ),
                        Image(
                            src= "img/themes/themes_point.png",
                            width= 50,
                            height= 50
                        ),
                    ],
                ),
                top= 120,
                right= 200,
                on_click= events.go_french_themes_lartisanat,
                on_hover= handle_hover
            ),
            Container(
                Row(
                    [
                        Image(
                            src= "img/themes/themes_point.png",
                            width= 50,
                            height= 50
                        ),
                        Text(
                            "Symbolique\nmathématique",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_200,
                            color= "orange"
                        )
                    ],
                ),
                bottom= 220,
                right= 100,
                on_click= events.go_french_themes_symbolique,
                on_hover= handle_hover
            ),
            Container(
                Column(
                    [
                        Image(
                            src= "img/themes/themes_point.png",
                            width= 50,
                            height= 50
                        ),
                        Text(
                            "Visite guidée\nAteliers des artisans",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_600,
                            color= "orange"
                        ),
                    ],
                ),
                bottom= 90,
                right= 240,
                on_click= events.go_french_themes_visite,
                on_hover= handle_hover
            ),
            Container(
                Row(
                    [
                        Text(
                            "Délectation\nexpériences\nmultimédia",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_200,
                            color= "orange"
                        ),
                        Container(
                            Image(
                                src= "img/themes/themes_point.png",
                                width= 50,
                                height= 50
                            ),
                            margin= margin.only(bottom= 40)
                        )
                    ],
                ),
                bottom= 182,
                left= 105,
                on_click= events.go_french_themes_delectation,
                on_hover= handle_hover
            ),
            Container(
                Column(
                    [
                        Text(
                            "Itinéraire\ngeographique",
                            font_family= "EB Garamond",
                            size= 22,
                            weight= FontWeight.W_200,
                            color= "orange"
                        ),
                        Container(
                            Image(
                                src= "img/themes/themes_point.png",
                                width= 50,
                                height= 50
                            ),
                            margin= margin.only(left= 70)
                        )
                    ],
                ),
                top= 120,
                left= 200,
                on_click= events.go_french_themes_itineraire,
                on_hover= handle_hover
            ),
        ],
        width= page.width,
        height= page.height
    )

    return View(
        "/french/themes",
        [
            Container(
                content= body
            ),
        ],
        padding= 0
    )