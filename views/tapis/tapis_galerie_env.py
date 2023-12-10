from flet import Page, View, Container, Stack, Row, Column, Image, Text, MainAxisAlignment, CrossAxisAlignment, padding
from utils.events import Events

def tapis_galerie_env_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    bg = Image(
        src= "img/tapis/tapis_galerie_bg.png",
        width= 768,
        height= 576
    )

    navbar_img = Image(
        src= "img/tapis/navbar_tapis.png"
    )
    def handle_hover_navbar_left(e):
        navbar_img.src = "img/tapis/navbar_tapis_left_hover.png" if e.data == "true" else "img/tapis/navbar_tapis.png"
        page.update()
    def handle_hover_navbar_right(e):
        navbar_img.src = "img/tapis/navbar_tapis_rigth_hover.png" if e.data == "true" else "img/tapis/navbar_tapis.png"
        page.update()
    navbar = Container(
        Row(
            [
                Container(
                    Text("Retour", font_family= "EB Garamond", color= "white", size= 18),
                    on_click= events.go_french_tapis,
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
            ], 
            spacing= 0
        ),
        left= 420,
        top= 500,
        padding= 0
    )

    def handle_color(e):
        e.control.content.color = "orange" if e.data == "true" else "white"
        e.control.update()
    bar = Container(
        Row([
            Container(
                Text(
                    "De l'Histoire",
                    font_family= "Eb Garamond",
                    color= "white",
                    size= 22
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_histoire
            ),
            Container(
                Text(
                    "De Régions",
                    font_family= "Eb Garamond",
                    color= "white",
                    size= 22
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_regions_cite
            ),
            Container(
                Text(
                    "De la Culture",
                    font_family= "Eb Garamond",
                    color= "white",
                    size= 22
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_culture
            ),
            Container(
                Text(
                    "De l'Art",
                    font_family= "Eb Garamond",
                    color= "white",
                    size= 22
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_art_citadin
            ),
            Container(
                Text(
                    "Galerie Virtuelle",
                    font_family= "Eb Garamond",
                    color= "orange",
                    size= 22
                ),
            ),
        ], spacing= 23),
        width= page.width - 40,
        height= 40,
        padding= padding.only(left= 30, right= 30),
        left= 20,
        right= 20,
        top= 30
    )

    current_page = Container(
        Column([
            Container(
                Text(
                    "Environnement",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "orange"
                ),
            ),
            Container(
                Text(
                    "Oeuvres",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "white"
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_galerie_oeuvres
            ),
        ], spacing= 10),
        width= 195,
        height= 100,
        padding= 10,
        top= 70,
        right= 20
    )

    def change_img_onec(e):
        img_id = e.control.content.src[14]
        current_img.src = f"img/tapis/env/{img_id}_text.png"
        page.update()
    def change_img_twoc(e):
        img_id = e.control.content.src[14:16]
        current_img.src = f"img/tapis/env/{img_id}_text.png"
        page.update()

    current_img = Image(
        src= "img/tapis/env/0_text.png",
        width= 255,
        height= 320,
        right= 100,
        top= 165,
    )
    content_body = Container(
        Row(
            [
                Column([
                    Row([
                        Container(
                            Image(
                                src= "img/tapis/env/0.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/1.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/2.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/3.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/4.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                    ]),
                    Row([
                        Container(
                            Image(
                                src= "img/tapis/env/5.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/6.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/7.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/8.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/9.png",
                                height= 50
                            ),
                            on_hover= change_img_onec
                        ),
                    ]),
                    Row([
                        Container(
                            Image(
                                src= "img/tapis/env/10.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/11.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/12.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/13.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/14.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                    ]),
                    Row([
                        Container(
                            Image(
                                src= "img/tapis/env/15.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/16.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/17.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/18.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/19.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                    ]),
                    Row([
                        Container(
                            Image(
                                src= "img/tapis/env/20.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/21.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/22.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/23.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                        Container(
                            Image(
                                src= "img/tapis/env/24.png",
                                height= 50
                            ),
                            on_hover= change_img_twoc
                        ),
                    ]),
                ], spacing= 10,),
                Container(
                    width= 320,
                    height= 395
                )
            ], 
            spacing= 20
        ),
        width= page.width - 120,
        height= 350,
        padding= padding.only(50, 30, 15, 15),
        bgcolor= "#9080460E",
        right= 60,
        top= 150,
    )

    body = Container(
        Stack([
            bg,
            navbar,
            bar,
            content_body,
            current_img,
            Image(
                src= "img/tapis/tapis_text_img.png",
                width= 48,
                height= 350,
                left= 60,
                top= 150,
            ),
            current_page
        ])
    )

    return View(
        "/french/tapis/galerie-env",
        [
            body
        ],
        padding= 0,
    )