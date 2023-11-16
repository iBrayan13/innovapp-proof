from flet import Page, app
from config import config_page
from router.router import router

def main(page: Page):
    config_page(page)
    router(page)
    

app(target= main, assets_dir="assets")