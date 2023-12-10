from flet import Page, View, Container, Stack, Row, Column, Image, Text, MainAxisAlignment, CrossAxisAlignment, margin
from utils.events import Events

def tapis_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    bg = Image(
        src= "img/tapis/tapis_bg.png",
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
            navbar_img,
        ]),
        right= 90,
        bottom= 23,
        padding= 0
    )

    # HOVER IMAGES
    historie_img = Image(
        src= "empty",
        width= 75,

        left= 50,
        bottom= 100,
    )
    def historie_hover(e):
        historie_img.src = "img/tapis/le_tapis_histoire_hover_img.png" if e.data == "true" else "empty"
        page.update()
    
    regions_img = Image(
        src= "empty",
        width= 75,

        left= 128,
        bottom= 100,
    )
    def regions_hover(e):
        regions_img.src = "img/tapis/le_tapis_regions_hover_img.png" if e.data == "true" else "empty"
        page.update()
    
    culture_img = Image(
        src= "empty",
        width= 75,

        left= 262,
        bottom= 96,
    )
    def culture_hover(e):
        culture_img.src = "img/tapis/le_tapis_culture_hover_img.png" if e.data == "true" else "empty"
        page.update()
    
    art_img = Image(
        src= "empty",
        width= 75,

        right= 299,
        bottom= 100,
    )
    def art_hover(e):
        art_img.src = "img/tapis/le_tapis_art_hover_img.png" if e.data == "true" else "empty"
        page.update()
    
    galerie_img = Image(
        src= "empty",
        width= 75,

        right= 166,
        bottom= 100,
    )
    def galerie_hover(e):
        galerie_img.src = "img/tapis/le_tapis_galerie_hover_img.png" if e.data == "true" else "empty"
        page.update()

    body = Container(
        Stack([
            bg,

            # HOVERS
            Container(
                width= 120,
                height= 25,
                left= 20,
                top= 159,
                on_click= events.go_french_tapis_histoire,
                on_hover= historie_hover,
            ),
            historie_img,
            Container(
                width= 58,
                height= 60,
                left= 59,
                bottom= 109,
                on_click= events.go_french_tapis_histoire,
                on_hover= historie_hover,
            ),

            Container(
                width= 115,
                height= 25,
                left= 135,
                top= 212,
                on_click= events.go_french_tapis_regions_cite,
                on_hover= regions_hover,
            ),
            regions_img,
            Container(
                width= 58,
                height= 60,
                left= 135,
                bottom= 109,
                on_click= events.go_french_tapis_regions_cite,
                on_hover= regions_hover,
            ),

            Container(
                width= 127,
                height= 25,
                left= 262,
                top= 269,
                on_click= events.go_french_tapis_culture,
                on_hover= culture_hover,
            ),
            culture_img,
            Container(
                width= 58,
                height= 60,
                left= 269,
                bottom= 105,
                on_click= events.go_french_tapis_culture,
                on_hover= culture_hover,
            ),

            Container(
                width= 75,
                height= 25,
                right= 294,
                bottom= 225,
                on_click= events.go_french_tapis_art_citadin,
                on_hover= art_hover,
            ),
            art_img,
            Container(
                width= 58,
                height= 60,
                right= 307,
                bottom= 106,
                on_click= events.go_french_tapis_art_citadin,
                on_hover= art_hover,
            ),

            Container(
                width= 160,
                height= 25,
                right= 84,
                bottom= 171,
                on_click= events.go_french_tapis_galerie_env,
                on_hover= galerie_hover,
            ),
            galerie_img,
            Container(
                width= 58,
                height= 60,
                right= 175,
                bottom= 108,
                on_click= events.go_french_tapis_galerie_env,
                on_hover= galerie_hover,
            ),

            navbar,
            Container(
                right= 22,
                bottom= 24,
                width= 143,
                height= 40,
                on_hover= handle_hover_navbar_right,
                on_click= events.go_home,
            ),
            Container(
                right= 185,
                bottom= 24,
                width= 123,
                height= 40,
                on_hover= handle_hover_navbar_left,
                on_click= events.go_french_menu,
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