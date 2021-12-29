*** Settings ***
Library  SeleniumLibrary
Variables  ../Locators/buy_items_locators.py

*** Keywords ***
Open my browser
    [Arguments]  ${url}     ${browser}
    open browser  ${url}    ${browser}
    maximize browser window

Close browsers
    close all browsers

Go to Apparel tab
    click element  ${apparel_tab}
    wait until page contains element  ${shoes_tab}
    click element  ${shoes_tab}

Select the first product
    click element  ${add_to_cart_1}
    wait until page contains element  ${product_1_size}
    select from list by index  ${product_1_size}    3
    select from list by index  ${product_1_color}    1
    click element  ${product_1_print}
    click element  xpath://*[@id="main-product-img-24"]

Select the quantity
    [Arguments]  ${quantity}
    input text  ${product_1_quantity}   ${quantity}

Add it to cart
    sleep   2s
    click element   ${add_to_buy}

Go to cart
    wait until page contains element    ${cart_tab}
    click element  ${cart_tab}

Remove the item from the cart
    click element  ${remove_btn}

Agree terms of service
    wait until page contains element    ${agree_terms}
    click element  ${agree_terms}
