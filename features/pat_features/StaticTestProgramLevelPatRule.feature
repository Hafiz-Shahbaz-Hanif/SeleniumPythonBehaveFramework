Feature: PAT Rule

	@YWPD-TC-339 @retry
	Scenario Outline: YWPD-TC-339 - Verify that user is able to generate the Static PAT Test Program Level Rule
		Given After login click on "Quality & PAT" in the left menu bar
		When Click on "PAT Rules"
		When Click "New Static PAT" button from PAT Rules window
		When Create PAT Rule window will be open and enter rule name as "<name>" and description in "General" tab
		When Navigate into the parameters tab and select "Facility" as "<Facility>"
		When After selecting "Facility" data will be populated automatically for work center, device and test program
		When Select the "<Parameter Number>"
		When Keep default settings for "Validate PAT Limits Against" check box
		When Select Bin Type from drop down
		When Navigate to the "Static Limits" tab and enter value for as "<Low Seed Limit>" and  as "<High Seed Limit>"
		When Click on the "Calculate Seed" button
		When Create PAT Rule window will open after clicking "Calculate Seed" button and available Lots will appear
		When Select Lot and click "Calculate" button
		When Value for "<Low Seed Limit>" and "<High Seed Limit>" will be calculated automatically
		When Enter the lot number for "<After Every Lots>"
		When Provide the "<Value of K>"
		When Select option from "<PAT limit to Apply>" dropdown
		When Provide "<Hard Bin Number for Lower PAT limit>" and "<Soft Bin Number for Lower PAT limit>"
		When Then provide the "<Hard Bin Number for Upper PAT limit>" and "<Soft Bin Number for Upper PAT limit>"
		When Click "Save" button
#		When The rule will be saved and appear in the PAT Rules window and PAT_RulesDetails table in database
        Examples:
		  | name                            | Facility           | Parameter Number                | Low Seed Limit    | High Seed Limit    | After Every Lots | Value of K | PAT limit to Apply              | Hard Bin Number for Lower PAT limit  | Soft Bin Number for Lower PAT limit  |  Hard Bin Number for Upper PAT limit | Soft Bin Number for Upper PAT limit |
		  | Static Test program level rule  | WEB SMALL DATA SET | Idd_prewrite Idd_prewrite       | 6.502738888888891 | 14.922961111111107 | 8                | 6          | Both (Lower & Upper) PAT Limits | 22                                   | 22                                   | 44                                   | 44                                  |