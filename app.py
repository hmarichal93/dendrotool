import streamlit as st

from streamlit_option_menu import option_menu
from PIL import Image


from ui.image import main as image
from ui.automatic import main as automatic_ring_delineation
from ui.home import main as home

from lib.io import load_json, write_json, bytesio_to_dict

class Menu:
    home = "Home"
    image = "Image"
    automatic_ring_delineation = "Automatic"
    manual_ring_delineation = "Manual"
    metrics = "Metrics"
    save = "Save"

APP_NAME = "UruDendro-Tool"
DEFAULT_CONFIG_PATH = "./config/default.json"
RUNTIME_CONFIG_PATH = "./config/runtime.json"






def main():
    im = Image.open('assets/pixels_wood.jpg')
    # Adding Image to web app
    st.set_page_config(page_title=APP_NAME, page_icon=im)
    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu(APP_NAME, [Menu.home, Menu.image, Menu.automatic_ring_delineation,
                                          Menu.manual_ring_delineation, Menu.metrics, Menu.save],
                            icons=['house', 'gear',':robot_face:', ':muscle:','🔎'], menu_icon="cast", default_index=0)


    if selected == Menu.home:
        home(DEFAULT_CONFIG_PATH, RUNTIME_CONFIG_PATH)

    elif selected == Menu.image:
        image(RUNTIME_CONFIG_PATH)


    elif selected == Menu.automatic_ring_delineation:
        automatic_ring_delineation()

    elif selected == Menu.manual_ring_delineation:
        st.write("You are at Manual-Ring-Delineation")

    elif selected == Menu.metrics:
        st.write("You are at Metrics")

    elif selected == Menu.save:
        st.write("You are at Save")


    with st.sidebar:
        realtime_update = st.checkbox("Update in realtime", True)
        st.image("assets/logo.jpg")





if __name__ == "__main__":
    main()