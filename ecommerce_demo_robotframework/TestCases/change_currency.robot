*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/price_checker_resources.robot
Variables  ../Locators/value_locators.py

Suite Setup  Open my browser    ${url}  ${browser}
Suite Teardown  Close browsers

*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome

*** Test Cases ***
Euro checker currency
    Changing currency on website

Dolar checker currency
    Getting the first currency back

*** Keywords ***
Changing currency on website
    Go to desktop tab
    ${first_price}=     get text    ${dollar_price}
    log to console  ${first_price}
    Select the other currency
    sleep   2s
    ${updated_price}=   get text   ${euro_price}
    log to console  ${updated_price}
    ${final_price}=     evaluate    ${first_price[1:]}!=${updated_price[1:]}

Getting the first currency back
    Go to desktop tab
    Select the other currency
    sleep   2s
    ${first_price}=     get text    ${euro_price}
    log to console  ${first_price}
    Select the first currency
    sleep   2s
    ${updated_price}=   get text   ${dollar_price}
    log to console  ${updated_price}
    ${final_price}=     evaluate    ${first_price[1:]}!=${updated_price[1:]}