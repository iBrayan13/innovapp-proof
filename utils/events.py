from flet import Page

class Events:
    def __init__(self, page: Page):
        self.page = page
        
        # Basic routes
        self.go_home = lambda e: self.page.go("/home")
        self.go_quit = lambda e: self.page.go("/quit")
        self.go_french = lambda e: self.page.go("/french")
        self.go_french_menu = lambda e: self.page.go("/french/menu")

        # Introduction routes
        self.go_french_introduction = lambda e: self.page.go("/french/introduction")
        self.go_french_introduction_contexte = lambda e: self.page.go("/french/introduction/contexte")
        self.go_french_introduction_public = lambda e: self.page.go("/french/introduction/public")
        self.go_french_introduction_objectifs = lambda e: self.page.go("/french/introduction/objectifs")
    
        # Themes routes
        self.go_french_themes = lambda e: self.page.go("/french/themes")
        self.go_french_themes_delectation = lambda e: self.page.go("/french/themes/delectation")
        self.go_french_themes_itineraire = lambda e: self.page.go("/french/themes/itineraire")
        self.go_french_themes_lartisanat = lambda e: self.page.go("/french/themes/lartisanat")
        self.go_french_themes_symbolique = lambda e: self.page.go("/french/themes/symbolique")
        self.go_french_themes_visite = lambda e: self.page.go("/french/themes/visite")

        # Musée Virtuel routes
        self.go_french_musee = lambda e: self.page.go("/french/musee")
        self.go_french_musee_base = lambda e: self.page.go("/french/musee/base")
        self.go_french_musee_base_decoration = lambda e: self.page.go("/french/musee/base/decoration")
        self.go_french_musee_base_maison = lambda e: self.page.go("/french/musee/base/maison")
        self.go_french_musee_base_parure = lambda e: self.page.go("/french/musee/base/parure")
        self.go_french_musee_base_metal = lambda e: self.page.go("/french/musee/base/metal")
        self.go_french_musee_tresors = lambda e: self.page.go("/french/musee/tresors")
        self.go_french_musee_tresors_chevalerie = lambda e: self.page.go("/french/musee/tresors/chevalerie")
        self.go_french_musee_tresors_sciences = lambda e: self.page.go("/french/musee/tresors/sciences")
        self.go_french_musee_tresors_savoir = lambda e: self.page.go("/french/musee/tresors/savoir")

        # Tapis Project Pilote routes
        self.go_french_tapis = lambda e: self.page.go("/french/tapis")
        self.go_french_tapis_histoire = lambda e: self.page.go("/french/tapis/histoire")
        self.go_french_tapis_regions_cite = lambda e: self.page.go("/french/tapis/regions-cite")
        self.go_french_tapis_regions_monde = lambda e: self.page.go("/french/tapis/regions-monde")
        self.go_french_tapis_culture = lambda e: self.page.go("/french/tapis/culture")
        self.go_french_tapis_art_citadin = lambda e: self.page.go("/french/tapis/art-citadin")
        self.go_french_tapis_art_rural = lambda e: self.page.go("/french/tapis/art-rural")
        self.go_french_tapis_galerie_env = lambda e: self.page.go("/french/tapis/galerie-env")
        self.go_french_tapis_galerie_oeuvres = lambda e: self.page.go("/french/tapis/galerie-oeuvres")

        # Liens Utiles routes
        self.go_french_utiles = lambda e: self.page.go("/french/utiles")
        self.go_french_utiles_guide = lambda e: self.page.go("/french/utiles/guide")
        self.go_french_utiles_informations = lambda e: self.page.go("/french/utiles/informations")

        # E-Artisanat routes
        self.go_french_eartisanat = lambda e: self.page.go("/french/eartisanat")
        self.go_french_eartisanat_simulation = lambda e: self.page.go("/french/eartisanat/simulation")
        self.go_french_eartisanat_connexion = lambda e: self.page.go("/french/eartisanat/connexion")
        self.go_french_eartisanat_solutions = lambda e: self.page.go("/french/eartisanat/solutions")