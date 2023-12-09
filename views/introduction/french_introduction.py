from flet import Page, View, Stack, Container, Row, Image, Text, MainAxisAlignment, CrossAxisAlignment
from utils.events import Events

def french_introduction_view(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    events = Events(page)

    introduction_img = Image(
        src= "img/introduction/introduction_bg.png",
        width= 800,
        height= 600
    )
    objectifs_img = Image(src= "empty")
    public_img = Image(src= "empty")
    contexte_img = Image(src= "empty")
    def handle_hover_introduction_objectifs(e):
        objectifs_img.src = "img/introduction/objectifs_hover.png" if e.data == "true" else "empty"
        page.update()
    def handle_hover_introduction_public(e):
        public_img.src = "img/introduction/public_hover.png" if e.data == "true" else "empty"
        page.update()
    def handle_hover_introduction_contexte(e):
        contexte_img.src = "img/introduction/contexte_hover.png" if e.data == "true" else "empty"
        page.update()

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

    return View(
        route= "/french/introduction",
        controls= [
            Container(
                content= Stack(
                    [
                       introduction_img,
                       Container(
                           content= objectifs_img,
                            width= 70,
                            height= 70,
                            right= 246,
                            bottom= 154,
                            on_click= events.go_french_introduction_objectifs,
                            on_hover= handle_hover_introduction_objectifs,
                        ),
                        Container(
                            width= 118,
                            height= 32,
                            right= 56,
                            bottom= 130,
                            on_click= events.go_french_introduction_objectifs,
                            on_hover= handle_hover_introduction_objectifs,
                        ),
                        Container(
                            content= public_img,
                            width= 70,
                            height= 70,
                            left= 223, 
                            top= 315,
                            on_click= events.go_french_introduction_public,
                            on_hover= handle_hover_introduction_public,
                        ),
                        Container(
                            width= 80,
                            height= 32,
                            left= 65,
                            top= 355,
                            on_click= events.go_french_introduction_public,
                            on_hover= handle_hover_introduction_public,
                        ),
                        Container(
                            content= contexte_img,
                            width= 60,
                            height= 70,
                            right= 327,
                            top= 174,
                            on_click= events.go_french_introduction_contexte,
                            on_hover= handle_hover_introduction_contexte,
                        ),
                        Container(
                            width= 120,
                            height= 32,
                            right= 277,
                            top= 100,
                            on_click= events.go_french_introduction_contexte,
                            on_hover= handle_hover_introduction_contexte,
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
                    ],
                ),
                width= page.width,
                height= page.height
            )
        ],
        padding= 0
    )