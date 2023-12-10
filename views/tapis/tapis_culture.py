from flet import Page, View, Container, Stack, Row, Column, Image, Text, MainAxisAlignment, CrossAxisAlignment, padding
from utils.events import Events

# Text
from .text import tapis_culture

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

def tapis_culture_view(page: Page):
    page.scroll = "always"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    bg = Image(
        src= "img/tapis/tapis_art_bg.png",
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
                    color= "orange",
                    size= 22
                ),
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
            height= 310
        ),
        width= page.width - 120,
        height= 350,
        padding= padding.only(60, 15, 15, 15),
        bgcolor= "#9080460E",
        right= 60,
        top= 130,
    )
    for i in get_txt(tapis_culture.textList):
        content_body.content.controls.append(i)

    body = Container(
        Stack([
            bg,
            navbar,
            bar,
            content_body,
            Image(
                src= "img/tapis/tapis_text_img.png",
                width= 48,
                height= 350,
                left= 60,
                top= 130,
            ),
        ])
    )

    return View(
        "/french/tapis/culture",
        [
            body
        ],
        padding= 0,
    )