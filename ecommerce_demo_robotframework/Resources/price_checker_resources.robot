*** Settings ***
Library  SeleniumLibrary
Variables  ../Locators/value_locators.py

*** Keywords ***
Open my browser
    [Arguments]  ${url}     ${browser}
    open browser  ${url}    ${browser}
    maximize browser window

Close browsers
    close all browsers

Go to desktop tab
    click element  ${computers_tab}
    wait until page contains element  ${desktop_tab}
    click element  ${desktop_tab}

Select the other currency
    select from list by index   ${currency_changer}    1

Select the first currency
    select from list by index   ${currency_changer}    0