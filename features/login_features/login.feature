#@order(1)
Feature: Login functionality

    @login @retry
    Scenario: Verify user login
        Given launch chrome browser
        When open Yieldwerx link
        And enter username and password
        And click on login button
        Then user must login to the main screen
        And close browser