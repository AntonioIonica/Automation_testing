*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/register_page_resources.robot

Suite Setup  Open my browser    ${url}  ${browser}
Suite Teardown  Close browsers

*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome
${register}     https://demo.nopcommerce.com/register?returnUrl=%2F
${first_name}   Ionut
${last_name}    Andrei
${email}    andreiionut@gmail.com
${pwd}  dasdqdqs

*** Test Cases ***
Registration with valid info
    Open register page  ${register}
    Register page form

*** Keywords ***
Register page form
    Gender choose
    First name input    ${first_name}
    Last name input     ${last_name}
    Birth date-day
    Birth date-month
    Birth date-year
    Email address input     ${email}
    Company name input
    Newsletter box
    Password input  ${pwd}
    Password confirm input  ${pwd}
    Submit register infos
    Register complete