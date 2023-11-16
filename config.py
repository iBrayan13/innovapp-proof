from flet import Page, ThemeMode, MainAxisAlignment, CrossAxisAlignment

def config_page(page: Page):
    page.title = "InnovApp Test | Brayan Barreto"
    page.theme_mode = ThemeMode.LIGHT
    page.fonts = {"EB Garamond": "fonts/EBGaramond-Medium.ttf"}
    page.padding = 0
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window_height= 612
    page.window_width= 780
    page.window_max_height= 612
    page.window_max_width= 780
    page.window_resizable = False