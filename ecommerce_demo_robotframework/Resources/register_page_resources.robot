*** Settings ***
Library  SeleniumLibrary
Variables  ../Locators/register_page_locators.py

*** Keywords ***
Open my browser
    [Arguments]  ${url}     ${browser}
    open browser  ${url}    ${browser}
    maximize browser window

Close browsers
    close all browsers

Open register page
    [Arguments]  ${register}
    go to  ${register}

Gender choose
    click element  ${gender_male}

First name input
    [Arguments]  ${first_name}
    input text  ${f_name}   ${first_name}

Last name input
    [Arguments]  ${last_name}
    input text  ${l_name}   ${last_name}

Birth date-day
    select from list by index  ${day_birth}     5

Birth date-month
    select from list by index  ${month_birth}   4

Birth date-year
    select from list by label  ${year_birth}   1996

Email address input
    [Arguments]  ${email}
    input text  ${email_box}    ${email}

Company name input
    input text  ${company_name}    California SRL

Newsletter box
    select checkbox  ${news_checkbox}

Password input
    [Arguments]  ${pwd}
    input text  ${password_box}    ${pwd}

Password confirm input
    [Arguments]  ${pwd}
    input text  ${password_check}    ${pwd}

Submit register infos
    click element  ${register_btn}

Register complete
    wait until page contains element  ${reg_complete}
    page should contain element  ${reg_complete}