from flet import Page
from views.intro import intro_view
from views.home import home_view
from views.quit import quit_view
from views.french import french_view
from views.french_menu import french_menu_view

# INTRODUCTION VIEWS
from views.introduction.french_introduction import french_introduction_view
from views.introduction.french_introduction_contexte import french_introduction_contexte_view
from views.introduction.french_introduction_public import french_introduction_public_view
from views.introduction.french_introduction_objectifs import french_introduction_objectifs_view

# THEMES VIEWS
from views.themes.themes import themes_view
from views.themes.themes_delectation import themes_delectation_view
from views.themes.themes_itineraire import themes_itineraire_view
from views.themes.themes_lartisanat import themes_lartisanat_view
from views.themes.themes_symbolique import themes_symbolique_view
from views.themes.themes_visite import themes_visite_view

# MUSÉE VIRTUEL VIEWS
from views.musee.musee import musee_view
from views.musee.musee_base import musee_base_view
from views.musee.musee_base_decoration import musee_base_decoration_view
from views.musee.musee_base_maison import musee_base_maison_view
from views.musee.musee_base_parure import musee_base_parure_view
from views.musee.musee_base_metal import musee_base_metal_view
from views.musee.musee_tresors import musee_tresors_view
from views.musee.musee_tresors_chevalerie import musee_tresors_chevalerie_view
from views.musee.musee_tresors_sciences import musee_tresors_sciences_view
from views.musee.musee_tresors_savoir import musee_tresors_savoir_view

# TAPIS PROJECT PILOTE VIEWS
from views.tapis.tapis import tapis_view
from views.tapis.tapis_histoire import tapis_histoire_view
from views.tapis.tapis_culture import tapis_culture_view
from views.tapis.tapis_art_citadin import tapis_art_citadin_view
from views.tapis.tapis_art_rural import tapis_art_rural_view
from views.tapis.tapis_galerie_env import tapis_galerie_env_view
from views.tapis.tapis_galerie_oeuvres import tapis_galerie_oeuvres_view

# LIENS UTILES VIEWS
from views.utiles.utiles import utiles_view
from views.utiles.utiles_guide import utiles_guide_view
from views.utiles.utiles_informations import utiles_informations_view

# E-ARTISANAT VIEWS
from views.eartisanat.eartisanat import eartisanat_view
from views.eartisanat.eartisanat_connexion import eartisanat_connexion_view
from views.eartisanat.eartisanat_solutions import eartisanat_solutions_view
from views.eartisanat.eartisanat_simulation import eartisanat_simulation_view

def router(page: Page):

    def route_change(e):
        page.views.clear()
        page.views.append(intro_view(page))

        if page.route == "/home":
            page.views.append(home_view(page))
        if page.route == "/quit":
            page.views.append(quit_view(page))
        if page.route == "/french":
            page.views.append(french_view(page))
        if page.route == "/french/menu":
            page.views.append(french_menu_view(page))

        # Introduction
        if page.route == "/french/introduction":
            page.views.append(french_introduction_view(page))
        if page.route == "/french/introduction/contexte":
            page.views.append(french_introduction_contexte_view(page))
        if page.route == "/french/introduction/public":
            page.views.append(french_introduction_public_view(page))
        if page.route == "/french/introduction/objectifs":
            page.views.append(french_introduction_objectifs_view(page))
        
        # Themes
        if page.route == "/french/themes":
            page.views.append(themes_view(page))
        if page.route == "/french/themes/delectation":
            page.views.append(themes_delectation_view(page))
        if page.route == "/french/themes/itineraire":
            page.views.append(themes_itineraire_view(page))
        if page.route == "/french/themes/lartisanat":
            page.views.append(themes_lartisanat_view(page))
        if page.route == "/french/themes/symbolique":
            page.views.append(themes_symbolique_view(page))
        if page.route == "/french/themes/visite":
            page.views.append(themes_visite_view(page))
        
        # Musée Virtuel
        if page.route == "/french/musee":
            page.views.append(musee_view(page))
        if page.route == "/french/musee/base":
            page.views.append(musee_base_view(page))
        if page.route == "/french/musee/base/decoration":
            page.views.append(musee_base_decoration_view(page))
        if page.route == "/french/musee/base/maison":
            page.views.append(musee_base_maison_view(page))
        if page.route == "/french/musee/base/parure":
            page.views.append(musee_base_parure_view(page))
        if page.route == "/french/musee/base/metal":
            page.views.append(musee_base_metal_view(page))
        if page.route == "/french/musee/tresors":
            page.views.append(musee_tresors_view(page))
        if page.route == "/french/musee/tresors/chevalerie":
            page.views.append(musee_tresors_chevalerie_view(page))
        if page.route == "/french/musee/tresors/sciences":
            page.views.append(musee_tresors_sciences_view(page))
        if page.route == "/french/musee/tresors/savoir":
            page.views.append(musee_tresors_savoir_view(page))

        # Tapis Project Pilote
        if page.route == "/french/tapis":
            page.views.append(tapis_view(page))
        if page.route == "/french/tapis/histoire":
            page.views.append(tapis_histoire_view(page))
        if page.route == "/french/tapis/culture":
            page.views.append(tapis_culture_view(page))
        if page.route == "/french/tapis/art-citadin":
            page.views.append(tapis_art_citadin_view(page))
        if page.route == "/french/tapis/art-rural":
            page.views.append(tapis_art_rural_view(page))
        if page.route == "/french/tapis/galerie-env":
            page.views.append(tapis_galerie_env_view(page))
        if page.route == "/french/tapis/galerie-oeuvres":
            page.views.append(tapis_galerie_oeuvres_view(page))
        
        # Liens Utiles
        if page.route == "/french/utiles":
            page.views.append(utiles_view(page))
        if page.route == "/french/utiles/guide":
            page.views.append(utiles_guide_view(page))
        if page.route == "/french/utiles/informations":
            page.views.append(utiles_informations_view(page))
        
        # E-Artisanat
        if page.route == "/french/eartisanat":
            page.views.append(eartisanat_view(page))
        if page.route == "/french/eartisanat/connexion":
            page.views.append(eartisanat_connexion_view(page))
        if page.route == "/french/eartisanat/solutions":
            page.views.append(eartisanat_solutions_view(page))
        if page.route == "/french/eartisanat/simulation":
            page.views.append(eartisanat_simulation_view(page))

        page.update()

    page.on_route_change = route_change

    page.go(page.route)