*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/check_buy_resources.robot
Variables  ../Locators/buy_items_locators.py

Suite Setup  Open my browser    ${url}  ${browser}
Suite Teardown  Close browsers

*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome

*** Test Cases ***
Buying some items and checking the quantity and price
    Buying an item
    ${i_price}=     get text    ${item_price}
    log to console  ${i_price}
    ${t_price}=     get text    ${total_price}
    log to console  ${t_price}
    capture page screenshot  C:/Users/anton/PycharmProjects/Automation_testing/ecommerce_demo_robotframework/Screenshots/price.png
    ${final_price}=     evaluate    ${i_price[1:]}!=${t_price[1:]}

Buying as a guest
    Buying an item
    Agree terms of service
    click element  ${checkout_btn}
    page should contain element  ${checkout_guest}

Removing an item from the cart
    Buying an item
    Remove the item from the cart
    wait until page contains element  ${empty_cart}
    page should contain element  ${empty_cart}

*** Keywords ***
Buying an item
    Go to Apparel tab
    Select the first product
    Select the quantity     2
    sleep   1
    Add it to cart
    Go to cart