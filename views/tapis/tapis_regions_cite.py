from flet import Page, View, Container, Stack, Row, Column, Image, Text, MainAxisAlignment, CrossAxisAlignment, border_radius, padding, margin
from utils.events import Events
from time import sleep

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
        src= "img/background.jpg",
        width= 800,
        height= 600
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

    def show_hover_galerie(e):
        body.content.controls[7] = galerie_bar
        e.control.on_hover = None
        page.update()

        sleep(3)

        body.content.controls[7] = Container()
        e.control.on_hover = show_hover_galerie
        page.update()

    def show_hover_art(e):
        body.content.controls[4] = art_page
        e.control.content.color = "orange"
        e.control.on_hover = None
        page.update()

        sleep(3)

        body.content.controls[4] = Container()
        e.control.on_hover = show_hover_art
        e.control.content.color = "white"
        art_page.content.controls[0].content.color = "white"
        art_page.content.controls[1].content.color = "white"
        page.update()

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
                on_hover= show_hover_art
            ),
            Container(
                Text(
                    "Galerie Virtuelle",
                    font_family= "Eb Garamond",
                    color= "white",
                    size= 22
                ),
                on_hover= show_hover_galerie
            ),
        ], spacing= 23),
        width= page.width - 40,
        height= 100,
        padding= 30,
        bgcolor= "#4D0130",
        border_radius= 20,
        left= 20,
        right= 20,
        top= 30
    )

    art_page = Container(
        Column([
            Container(
                Text(
                    "Variantes du tapis citadin",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "white"
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_art_citadin
            ),
            Container(
                Text(
                    "Variations du tapis rural",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "white"
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_art_rural
            ),
        ], spacing= 10),
        width= 210,
        height= 90,
        padding= 10,
        bgcolor= "#4D0130",
        border_radius= border_radius.only(bottom_left= 15, bottom_right= 15),
        top= 120,
        right= 105
    )

    content_body = Container(
        Column(
            [],
            spacing= 0,
            scroll= "always",
            height= 190
        ),
        width= 375,
        height= 220,
        padding= padding.only(50, 15, 15, 15),
        bgcolor= "#80460E",
        left= 60,
        top= 280,
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
            height= 190
        ),
        width= 285,
        height= 220,
        padding= 15,
        bgcolor= "#80460E",
        border_radius= border_radius.only(bottom_right= 15),
        right= 60,
        top= 280,
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
        bgcolor= "#4D0130",
        border_radius= border_radius.only(top_right= 15),
        left= 60,
        top= 220,
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
                on_click= events.go_french_tapis_regions_cite
            ),
        ], spacing= 10),
        width= 210,
        height= 90,
        padding= 10,
        bgcolor= "#4D0130",
        border_radius= border_radius.only(bottom_left= 15, bottom_right= 15),
        top= 120,
        left= 180
    )
    
    galerie_bar = Container(
        Column([
            Container(
                Text(
                    "Environnement",
                    font_family= "EB Garamond",
                    size= 18,
                    color= "white"
                ),
                on_hover= handle_color,
                on_click= events.go_french_tapis_galerie_env
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
        padding= padding.only(10, 20, 10, 10),
        bgcolor= "#4D0130",
        border_radius= border_radius.only(bottom_left= 15, bottom_right= 15),
        top= 110,
        right= 20
    )

    body = Container(
        Stack([
            bg,
            navbar,
            bar,
            content_body,
            Container(),
            content_bar_body,
            Image(
                src= "img/tapis/tapis_text_img.png",
                width= 38,
                height= 330,
                left= 60,
                top= 195,
            ),
            Container(),
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