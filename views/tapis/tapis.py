from flet import Page, View, Container, Stack, Row, Column, Image, Text, MainAxisAlignment, CrossAxisAlignment, margin
from utils.events import Events

def tapis_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    bg = Image(
        src= "img/background.jpg",
        width= 800,
        height= 600
    )

    def handle_hover_cont(e):
        e.control.content.controls[1].color = "yellow" if e.data == "true" else "white"
        src_img = e.control.content.controls[0].content.src
        e.control.content.controls[0].content.src = f"{src_img[0 : len(src_img) - 7]}hover_img.png" if e.data == "true" else f"{src_img[0 : len(src_img) - 13]}img.png"
        e.control.update()

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

    body = Container(
        Stack([
            bg,
            navbar,
            Column(
                [
                    Text(
                        "Le Tapis",
                        font_family= "EB Garamond",
                        size= 48,
                        color= "white"
                    ),
                    Text(
                        "Project pilote",
                        font_family= "EB Garamond",
                        size= 30,
                        color= "white"
                    ),
                ],
                spacing= 0,
                left= 40,
                top= 20
            ),
            Container(
                Column(
                    [
                        Container(
                            Image(
                                src= "img/tapis/le_tapis_histoire_img.png",
                                width= 75,
                                height= 75
                            ),
                            margin= margin.only(left= 15)
                        ),
                        Text(
                            "De l'Histoire",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 20
                        ),
                    ],
                    spacing= 8,
                ),
                top= 190,
                left= 120,
                bgcolor= "#4D0130",
                border_radius= 20,
                padding= 10,
                width= 130,
                height= 130,
                on_hover= handle_hover_cont,
                on_click = events.go_french_tapis_histoire
            ),
            Container(
                Column(
                    [
                        Container(
                            Image(
                                src= "img/tapis/le_tapis_regions_img.png",
                                width= 75,
                                height= 75
                            ),
                            margin= margin.only(left= 15)
                        ),
                        Text(
                            "Des Régions",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 20
                        ),
                    ],
                    spacing= 8,
                ),
                bottom= 140,
                left= 210,
                bgcolor= "#4D0130",
                border_radius= 20,
                padding= 10,
                width= 130,
                height= 130,
                on_hover= handle_hover_cont
            ),
            Container(
                Column(
                    [
                        Container(
                            Image(
                                src= "img/tapis/le_tapis_culture_img.png",
                                width= 75,
                                height= 75
                            ),
                            margin= margin.only(left= 20)
                        ),
                        Text(
                            "De la Culture",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 20
                        ),
                    ],
                    spacing= 8,
                ),
                top= 190,
                left= 300,
                bgcolor= "#4D0130",
                border_radius= 20,
                padding= 10,
                width= 135,
                height= 130,
                on_hover= handle_hover_cont,
                on_click= events.go_french_tapis_culture
            ),
            Container(
                Column(
                    [
                        Container(
                            Image(
                                src= "img/tapis/le_tapis_art_img.png",
                                width= 75,
                                height= 75
                            ),
                            margin= margin.only(left= 17)
                        ),
                        Text(
                            "     De l'Art",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 20
                        ),
                    ],
                    spacing= 8,
                ),
                bottom= 140,
                right= 240,
                bgcolor= "#4D0130",
                border_radius= 20,
                padding= 10,
                width= 130,
                height= 130,
                on_hover= handle_hover_cont,
                on_click= events.go_french_tapis_art_citadin
            ),
            Container(
                Column(
                    [
                        Container(
                            Image(
                                src= "img/tapis/le_tapis_galerie_img.png",
                                width= 75,
                                height= 75
                            ),
                            margin= margin.only(left= 32)
                        ),
                        Text(
                            "Galerie Virtuelle",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 20
                        ),
                    ],
                    spacing= 8,
                ),
                top= 190,
                right= 120,
                bgcolor= "#4D0130",
                border_radius= 20,
                padding= 10,
                width= 160,
                height= 130,
                on_hover= handle_hover_cont,
                on_click= events.go_french_tapis_galerie_env
            ),

        ])
    )

    return View(
        "/french/tapis",
        [
            body
        ],
        padding= 0
    )