*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/login_page_resources.robot
Library  DataDriver     ../TestData/login_data.xlsx    sheet_name=Sheet1

Suite Setup  Open my browser    ${url}  ${browser}
Suite Teardown  Close browsers
Test Template   Login form

*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome

*** Test Cases ***
Invalid data using  ${email_address}    ${pwd}

*** Keywords ***
Login form
    [Arguments]  ${email_address}    ${pwd}
    go to   https://demo.nopcommerce.com/login?returnUrl=%2F
    Email input     ${email_address}
    Password input  ${pwd}
    Submit button
    User not found alert