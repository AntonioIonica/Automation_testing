"""
Home page-Herokuapp
Clicking on buttons
"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage


class HomePage(BasePage):
    AB_BTN = (By.XPATH, '//*[@id="content"]/ul/li[1]/a')
    ADD_REMOVE_BTN = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    BASIC_AUTH_BTN = (By.XPATH, '//*[@id="content"]/ul/li[3]/a')
    BROKEN_IMG_BTN = (By.XPATH, '//*[@id="content"]/ul/li[4]/a')
    CHALLENGING_DOM_BTN = (By.XPATH, '//*[@id="content"]/ul/li[5]/a')
    CHK_BOX_BTN = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    CONTEXT_MENU_BTN = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')
    DIGEST_AUTH_BTN = (By.XPATH, '//*[@id="content"]/ul/li[8]/a')
    DISSAP_ELEMS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[9]/a')
    DRAG_DROP_BTN = (By.XPATH, '//*[@id="content"]/ul/li[10]/a')
    DROPDOWN_BTN = (By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    DYN_CONTENT_BTN = (By.XPATH, '//*[@id="content"]/ul/li[12]/a')
    DYN_CONTROLS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[13]/a')
    DYN_LOADING_BTN = (By.XPATH, '//*[@id="content"]/ul/li[14]/a')
    ENTRY_AD_BTN = (By.XPATH, '//*[@id="content"]/ul/li[15]/a')
    EXIT_INTENT_BTN = (By.XPATH, '//*[@id="content"]/ul/li[16]/a')
    FILE_DOWN_BTN = (By.XPATH, '//*[@id="content"]/ul/li[17]/a')
    FILE_UP_BTN = (By.XPATH, '//*[@id="content"]/ul/li[18]/a')
    FLOAT_MENU_BTN = (By.XPATH, '//*[@id="content"]/ul/li[19]/a')
    FORGOT_PASS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[20]/a')
    FORM_AUTH_BTN = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    FRAMES_BTN = (By.XPATH, '//*[@id="content"]/ul/li[22]/a')
    GEOLOCATION_BTN = (By.XPATH, '//*[@id="content"]/ul/li[23]/a')
    HORIZONTAL_SLIDER_BTN = (By.XPATH, '//*[@id="content"]/ul/li[24]/a')
    HOVERS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[25]/a')
    INFINITE_SCROLL_BTN = (By.XPATH, '//*[@id="content"]/ul/li[26]/a')
    INPUTS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[27]/a')
    JQUERY_BTN = (By.XPATH, '//*[@id="content"]/ul/li[28]/a')
    JS_ALERTS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[29]/a')
    JS_EVENT_ALERT_BTN = (By.XPATH, '//*[@id="content"]/ul/li[30]/a')
    KEY_PRESS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[31]/a')
    LARGE_DEEP_DOM_BTN = (By.XPATH, '//*[@id="content"]/ul/li[32]/a')
    MULTIPLE_WINDOWS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[33]/a')
    NESTED_FRAME_BTN = (By.XPATH, '//*[@id="content"]/ul/li[34]/a')
    NOTIF_MSGS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[35]/a')
    REDIRECT_LINK_BTN = (By.XPATH, '//*[@id="content"]/ul/li[36]/a')
    SECURE_DOWN_BTN = (By.XPATH, '//*[@id="content"]/ul/li[37]/a')
    SHADOW_DOM_BTN = (By.XPATH, '//*[@id="content"]/ul/li[38]/a')
    SHIFTING_CONTENT_BTN = (By.XPATH, '//*[@id="content"]/ul/li[39]/a')
    SLOW_RESOURCES_BTN = (By.XPATH, '//*[@id="content"]/ul/li[40]/a')
    SORTABLE_DATA_BTN = (By.XPATH, '//*[@id="content"]/ul/li[41]/a')
    STATUS_CODES_BTN = (By.XPATH, '//*[@id="content"]/ul/li[42]/a')
    TYPOS_BTN = (By.XPATH, '//*[@id="content"]/ul/li[43]/a')
    WYSIWYG_EDITOR_BTN = (By.XPATH, '//*[@id="content"]/ul/li[44]/a')

    def click_on_ab_btn(self):
        self.driver.find_element(*self.AB_BTN).click()
        print('I clicked on A/B testing button!')

    def click_on_add_remove_btn(self):
        self.driver.find_element(*self.ADD_REMOVE_BTN).click()
        print('I clicked on add/remove button!')

    def click_on_basic_auth_btn(self):
        self.driver.find_element(*self.BASIC_AUTH_BTN).click()
        print('I clicked on basic authentification button!')

    def click_on_broken_img_btn(self):
        self.driver.find_element(*self.BROKEN_IMG_BTN).click()
        print('I clicked on broken image button!')

    def click_on_challenging_btn(self):
        self.driver.find_element(*self.CHALLENGING_DOM_BTN).click()
        print('I clicked on challenging button!')

    def click_on_check_box_btn(self):
        self.driver.find_element(*self.CHK_BOX_BTN).click()
        print('I clicked on check box button!')

    def click_on_context_menu_btn(self):
        self.driver.find_element(*self.CONTEXT_MENU_BTN).click()
        print('I clicked on challenging button!')

    def click_on_digest_btn(self):
        self.driver.find_element(*self.DIGEST_AUTH_BTN).click()
        print('I clicked on challenging button!')

    def click_on_dissap_elements_btn(self):
        self.driver.find_element(*self.DISSAP_ELEMS_BTN).click()
        print('I clicked on dissapearing elements button!')

    def click_on_drag_drop_btn(self):
        self.driver.find_element(*self.DRAG_DROP_BTN).click()
        print('I clicked on drag and drop button!')

    def click_on_dropdown_btn(self):
        self.driver.find_element(*self.DROPDOWN_BTN).click()
        print('I clicked on dropdown button!')

    def click_on_dynamic_content_btn(self):
        self.driver.find_element(*self.DYN_CONTENT_BTN).click()
        print('I clicked on dynamic content button!')

    def click_on_dynamic_controls_btn(self):
        self.driver.find_element(*self.DYN_CONTROLS_BTN).click()
        print('I clicked on dynamic controls button!')

    def click_on_dynamic_loading_btn(self):
        self.driver.find_element(*self.DYN_LOADING_BTN).click()
        print('I clicked on dynamic loading button!')

    def click_on_entry_ad_btn(self):
        self.driver.find_element(*self.ENTRY_AD_BTN).click()
        print('I clicked on entry add button!')

    def click_on_exit_intent_btn(self):
        self.driver.find_element(*self.EXIT_INTENT_BTN).click()
        print('I clicked on exit intent button!')

    def click_on_file_down_btn(self):
        self.driver.find_element(*self.FILE_DOWN_BTN).click()
        print('I clicked on file download button!')

    def click_on_file_up_btn(self):
        self.driver.find_element(*self.FILE_UP_BTN).click()
        print('I clicked on file upload button!')

    def click_on_floating_menu_btn(self):
        self.driver.find_element(*self.FLOAT_MENU_BTN).click()
        print('I clicked on floating menu button!')

    def click_on_forgot_pass_btn(self):
        self.driver.find_element(*self.FORGOT_PASS_BTN).click()
        print('I clicked on forgot password button!')

    def click_on_form_auth_btn(self):
        self.driver.find_element(*self.FORM_AUTH_BTN).click()
        print('I clicked on form authentification button!')

    def click_on_frames_btn(self):
        self.driver.find_element(*self.FRAMES_BTN).click()
        print('I clicked on frames button!')

    def click_on_geolocation_btn(self):
        self.driver.find_element(*self.GEOLOCATION_BTN).click()
        print('I clicked on geolocation button!')

    def click_on_horizontal_slider_btn(self):
        self.driver.find_element(*self.HORIZONTAL_SLIDER_BTN).click()
        print('I clicked on horizontal slider button!')

    def click_hovers_btn(self):
        self.driver.find_element(*self.HOVERS_BTN).click()
        print('I clicked on hovers button!')

    def click_on_infinite_scroll_btn(self):
        self.driver.find_element(*self.INFINITE_SCROLL_BTN).click()
        print('I clicked on infinite scroll button!')

    def click_on_inputs_btn(self):
        self.driver.find_element(*self.INPUTS_BTN).click()
        print('I clicked on exit inputs button!')

    def click_on_jquery_ui_btn(self):
        self.driver.find_element(*self.JQUERY_BTN).click()
        print('I clicked on JQuery UI menu button!')

    def click_on_js_alerts_btn(self):
        self.driver.find_element(*self.JS_ALERTS_BTN).click()
        print('I clicked on JavaScript alerts button!')

    def click_on_js_onload_btn(self):
        self.driver.find_element(*self.JS_EVENT_ALERT_BTN).click()
        print('I clicked on JavaScript onload event error button!')

    def click_on_key_presses_btn(self):
        self.driver.find_element(*self.KEY_PRESS_BTN).click()
        print('I clicked on key presses button!')

    def click_on_large_deep_dom_btn(self):
        self.driver.find_element(*self.LARGE_DEEP_DOM_BTN).click()
        print('I clicked on large and deep DOM button!')

    def click_on_multiple_windows_btn(self):
        self.driver.find_element(*self.MULTIPLE_WINDOWS_BTN).click()
        print('I clicked on multiple windows button!')

    def click_on_nested_frames_btn(self):
        self.driver.find_element(*self.NESTED_FRAME_BTN).click()
        print('I clicked on nested frames button!')

    def click_on_notification_messages_btn(self):
        self.driver.find_element(*self.NOTIF_MSGS_BTN).click()
        print('I clicked on notification messages button!')

    def click_on_redirect_link_btn(self):
        self.driver.find_element(*self.REDIRECT_LINK_BTN).click()
        print('I clicked on redirect link button!')

    def click_on_secure_download_btn(self):
        self.driver.find_element(*self.SECURE_DOWN_BTN).click()
        print('I clicked on secure file download button!')

    def click_on_shadow_dom_btn(self):
        self.driver.find_element(*self.SHADOW_DOM_BTN).click()
        print('I clicked on shadow DOM button!')

    def click_on_shifting_content_btn(self):
        self.driver.find_element(*self.SHIFTING_CONTENT_BTN).click()
        print('I clicked on shifting content button!')

    def click_on_slow_resources_btn(self):
        self.driver.find_element(*self.SLOW_RESOURCES_BTN).click()
        print('I clicked on slow resources button!')

    def click_on_sortable_data_tables_btn(self):
        self.driver.find_element(*self.SORTABLE_DATA_BTN).click()
        print('I clicked on sortable data tables button!')

    def click_on_status_codes_btn(self):
        self.driver.find_element(*self.STATUS_CODES_BTN).click()
        print('I clicked on status codes button!')

    def click_on_typos_btn(self):
        self.driver.find_element(*self.TYPOS_BTN).click()
        print('I clicked on typos button!')

    def click_on_wysiwyg_editor_btn(self):
        self.driver.find_element(*self.EXIT_INTENT_BTN).click()
        print('I clicked on WYSIWYG Editor button!')

    def title_page(self):
        print('Title page is verified!')
        return self.driver.title
