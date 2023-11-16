from flet import Page, View, Stack, Container, Row, Column, Image, Text, margin
from utils.events import Events

def themes_visite_view(page: Page):
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
                    on_click= events.go_french_themes,
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
        bottom= 30,
        padding= 0
    )

    return View(
        route= "/french/themes/visite",
        controls= [
            Container(
                content= Stack(
                    [
                        Image(
                            src= "img/background.jpg",
                            width= 800,
                            height= 600
                        ),
                        Container(
                            Image(
                                src= "img/themes/themes_visite_imgs.png",
                                width= 80,
                                height= 540
                            ),
                            margin= margin.only(left=20, top= 25)
                        ),
                        Container(
                            content= Stack([
                                Column([
                                    Text(
                                        "Visite guidée dans les ateliers des\nmaitres-artisans",
                                        size= 32,
                                        color= "white",
                                        font_family= "EB Garamond"
                                    ),
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
                                                    "Des métiers millénaires au présent",
                                                    color="yellow",
                                                    size= 18,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
                                            Container(
                                                Column([
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Les maítres-tanneurs.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Les maítres zellijeurs.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Les maítres ebénistes.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Les maítres céramistes.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Les maítres-tisserands.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                ]),
                                                margin= margin.only(left= 40)
                                            ),
                                            Row([
                                                Container(
                                                    Image(
                                                        src= "img/menu_point.png",
                                                        width= 30,
                                                        height= 30,
                                                    ),
                                                    margin= margin.only(bottom= 23)
                                                ),
                                                Text(
                                                    "Cartographie utile des quartiers de l'artisanat\n(Des principalesvilles du Royaume)",
                                                    color="yellow",
                                                    size= 18,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
                                            Container(
                                                Column([
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Fiches synoptiques des lieux de commerce.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Bazars, ateliers et boutiques.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                    Row([
                                                        Container(
                                                            Image(
                                                                src= "img/menu_point.png",
                                                                width= 15,
                                                                height= 15,
                                                            )
                                                        ),
                                                        Text(
                                                            "Antiquares.",
                                                            color="yellow",
                                                            size= 14,
                                                            font_family= "EB Garamond"
                                                        ),
                                                    ]),
                                                ]),
                                                margin= margin.only(left= 40)
                                            ),
                                            Row([
                                                Container(
                                                    Image(
                                                        src= "img/menu_point.png",
                                                        width= 30,
                                                        height= 30,
                                                    )
                                                ),
                                                Text(
                                                    "Hyper-liens avec la Base de données genérale.",
                                                    color="yellow",
                                                    size= 18,
                                                    font_family= "EB Garamond"
                                                ),
                                            ]),
                                        ]),
                                        width= 530,
                                        height= 398,
                                        border_radius= 20,
                                        padding= 10,
                                        bgcolor= "#4D0130"
                                    )
                                ])
                            ]),
                            margin= margin.only(left= 145, top= 15)
                        ),
                        navbar
                    ]
                )
            )
        ],
        padding= 0
    )