*** Settings ***
Library  SeleniumLibrary
Variables  ../Locators/login_page_locators.py

*** Keywords ***
Open my browser
    [Arguments]  ${url}     ${browser}
    open browser  ${url}    ${browser}
    maximize browser window

Close browsers
    close all browsers

Email input
    [Arguments]     ${email_address}
    input text  ${email_box}    ${email_address}

Password input
    [Arguments]     ${pwd}
    input text  ${password_box}    ${pwd}

Submit button
    click element  ${login_btn}

User not found alert
    sleep   2s
    page should contain element     ${no_customer_alert}
