"""
home page
"""

from pages.base_page import BasePage


class HomePage(BasePage):

    AUTOCOMPLETE_BTN = 'TBA'
    BUTTONS_BTN = 'TBA'
    CHECKBOX_BTN = 'TBA'
    DATEPICKER_BTN = 'TBA'
    DRAG_AND_DROP_BTN = 'TBA'
    DROPDOWN_BTN = 'TBA'
    ENAB_DISAB_ELEMS_BTN = 'TBA'
    FILE_UPLOAD_BTN = 'TBA'
    KEY_MOUSE_PRESS_BTN = 'TBA'
    MODAL_BTN = 'TBA'
    PAGE_SCROLL_BTN = 'TBA'
    RADIO_BTN = 'TBA'
    SWITCH_WINDOW_BTN = 'TBA'
    COMPLETE_WEB_FORM_BTN = 'TBA'

    def click_on_autocomplete_btn(self):
        print('I clicked on Autocomplete!')

    def click_on_buttons_btn(self):
        print('I clicked on Buttons!')

    def click_on_checkbox_btn(self):
        print('I clicked on Checkbox!')

    def click_on_datepicker_btn(self):
        print('I clicked on Datepicker!')

    def click_on_drag_and_drop_btn(self):
        print('I clicked on Drag and drop!')

    def click_on_dropdown_btn(self):
        print('I clicked on Dropdown!')

    def click_on_enab_disab_elems_btn(self):
        print('I clicked on Enabled and disabled elements!')

    def click_on_file_upload_btn(self):
        print('I clicked on File upload!')

    def click_on_key_mouse_press_btn(self):
        print('I clicked on Key and mouse press!')

    def click_on_page_scroll_btn(self):
        print('I clicked on Page scroll!')

    def click_on_radio_btn(self):
        print('I clicked on Radio button!')

    def click_on_switch_window_btn(self):
        print('I clicked on Switch window!')

    def click_on_complete_web_form_btn(self):
        print('I clicked on Complete web form!')
