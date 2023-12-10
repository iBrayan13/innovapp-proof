from flet import Page, View, Container, Stack, Row, Column, Image, Text, MainAxisAlignment, CrossAxisAlignment, padding, margin
from utils.events import Events

# Text
from .text import tapis_regions_cite_rabat, tapis_regions_cite_mediouna, tapis_regions_cite_fes

def get_txt(text_list: list):
    lines = []
    for line in text_list:
        new_line = line.replace('Ã©','é').replace('Ã\xad', 'í')
        lines.append(
            Text(
                new_line,
                size= 19,
                color= "white",
                font_family= "EB Garamond"
            )
        )
    
    return lines

def tapis_regions_cite_view(page: Page):
    page.scroll = "always"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    bg = Image(
        src= "img/tapis/regions/tapis_regions_bg.png",
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
        page.update()
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
                    color= "orange",
                    size= 22
                ),
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
                    color= "white",
                    size= 22
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_galerie_env
            ),
        ], spacing= 23),
        width= page.width - 40,
        height= 40,
        padding= padding.only(left= 30, right= 30),
        left= 20,
        right= 20,
        top= 30
    )

    content_body = Container(
        Column(
            [],
            spacing= 0,
            scroll= "always",
            height= 220
        ),
        width= 365,
        height= 250,
        padding= padding.only(50, 15, 15, 15),
        bgcolor= "#9080460E",
        left= 60,
        top= 250,
    )
    # Default content
    for i in get_txt(tapis_regions_cite_rabat.textList):
        content_body.content.controls.append(i)
    content_second_body = Container(
        Column(
            [
                Row([
                    Row([
                        Text(
                            "Photo",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 16
                        ),
                        Text(
                            "1",
                            font_family= "EB Garamond",
                            color= "orange",
                            size= 16
                        ),
                        Text(
                            "2",
                            font_family= "EB Garamond",
                            color= "orange",
                            size= 16
                        ),
                        Text(
                            "3",
                            font_family= "EB Garamond",
                            color= "gray",
                            size= 16
                        ),
                        Text(
                            "4",
                            font_family= "EB Garamond",
                            color= "gray",
                            size= 16
                        ),
                        Text(
                            "5",
                            font_family= "EB Garamond",
                            color= "gray",
                            size= 16
                        ),
                    ], spacing= 5),
                    Row([
                        Text(
                            "Dessin",
                            font_family= "EB Garamond",
                            color= "white",
                            size= 16
                        ),
                        Text(
                            "1",
                            font_family= "EB Garamond",
                            color= "orange",
                            size= 16
                        ),
                        Text(
                            "2",
                            font_family= "EB Garamond",
                            color= "orange",
                            size= 16
                        ),
                        Text(
                            "3",
                            font_family= "EB Garamond",
                            color= "orange",
                            size= 16
                        ),
                        Text(
                            "4",
                            font_family= "EB Garamond",
                            color= "gray",
                            size= 16
                        ),
                        Text(
                            "5",
                            font_family= "EB Garamond",
                            color= "gray",
                            size= 16
                        ),
                    ], spacing= 5)
                ], spacing= 10),
                Container(
                    Image(
                        src= "img/tapis/regions/cite_rabat_imgs.png",
                        height= 160,
                    ),
                    margin= margin.only(left= 40)
                )
            ],
            spacing= 10,
            height= 220
        ),
        width= 285,
        height= 250,
        padding= 15,
        bgcolor= "#9080460E",
        right= 60,
        top= 250,
    )
    def handle_content(e):
        content_body.content.controls = []

        if e.control.content.value == "Le Tapis Rabat":
            txt_list = tapis_regions_cite_rabat.textList
            content_second_body.content.controls[1].content.src = "img/tapis/regions/cite_rabat_imgs.png"

            # Photo Text
            content_second_body.content.controls[0].controls[0].controls[1].color = "orange"
            content_second_body.content.controls[0].controls[0].controls[2].color = "orange"
            content_second_body.content.controls[0].controls[0].controls[3].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[4].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[5].color = "gray"
            # Dessin Text
            content_second_body.content.controls[0].controls[1].controls[1].color = "orange"
            content_second_body.content.controls[0].controls[1].controls[2].color = "orange"
            content_second_body.content.controls[0].controls[1].controls[3].color = "orange"
            content_second_body.content.controls[0].controls[1].controls[4].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[5].color = "gray"
        
        elif e.control.content.value == "Le Tapis de Médiouna":
            txt_list = tapis_regions_cite_mediouna.textList
            content_second_body.content.controls[1].content.src = "img/tapis/regions/cite_mediouna_imgs.png"

            # Photo Text
            content_second_body.content.controls[0].controls[0].controls[1].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[2].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[3].color = "orange"
            content_second_body.content.controls[0].controls[0].controls[4].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[5].color = "gray"
            # Dessin Text
            content_second_body.content.controls[0].controls[1].controls[1].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[2].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[3].color = "orange"
            content_second_body.content.controls[0].controls[1].controls[4].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[5].color = "gray"

        elif e.control.content.value == "Le Tapis de Fes":
            txt_list = tapis_regions_cite_fes.textList
            content_second_body.content.controls[1].content.src = "img/tapis/regions/cite_fes_imgs.png"

            # Photo Text
            content_second_body.content.controls[0].controls[0].controls[1].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[2].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[3].color = "gray"
            content_second_body.content.controls[0].controls[0].controls[4].color = "orange"
            content_second_body.content.controls[0].controls[0].controls[5].color = "orange"
            # Dessin Text
            content_second_body.content.controls[0].controls[1].controls[1].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[2].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[3].color = "gray"
            content_second_body.content.controls[0].controls[1].controls[4].color = "orange"
            content_second_body.content.controls[0].controls[1].controls[5].color = "orange"

        for i in get_txt(txt_list):
            content_body.content.controls.append(i)
    content_bar_body = Container(
        Row(
            [
                Container(
                    Text(
                        "Le Tapis Rabat",
                        font_family= "EB Garamond",
                        size= 20,
                        color= "white"
                    ),
                    on_hover= handle_color,
                    on_click= handle_content
                ),
                Container(
                    Text(
                        "Le Tapis de Médiouna",
                        font_family= "EB Garamond",
                        size= 20,
                        color= "white"
                    ),
                    on_hover= handle_color,
                    on_click= handle_content
                ),
                Container(
                    Text(
                        "Le Tapis de Fes",
                        font_family= "EB Garamond",
                        size= 20,
                        color= "white"
                    ),
                    on_hover= handle_color,
                    on_click= handle_content
                ),
            ],
            spacing= 50,
            width= 567
        ),
        width= 645,
        height= 60,
        padding= padding.only(63, 15, 25, 15),
        bgcolor= "#904D0130",
        left= 60,
        top= 190,
    )
    current_page = Container(
        Column([
            Container(
                Text(
                    "A travers la cité",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "orange"
                ),
            ),
            Container(
                Text(
                    "A travers le monde rural",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "white"
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_regions_monde
            ),
        ], spacing= 10),
        width= 210,
        height= 90,
        padding= 10,
        top= 70,
        left= 180
    )

    body = Container(
        Stack([
            bg,
            navbar,
            bar,
            content_body,
            content_bar_body,
            Image(
                src= "img/tapis/tapis_text_img.png",
                height= 310,
                left= 60,
                top= 188,
            ),
            content_second_body,
            current_page
        ])
    )

    return View(
        "/french/tapis/regions-cite",
        [
            body
        ],
        padding= 0,
    )