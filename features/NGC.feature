#Feature: NGC
#
##    Rule 1
#Scenario: Create SWM Rule 4670-PrePostMerge-Missing-F
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-Missing-F
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Missing Source Wafer Bin In Bin Rule Details
#    And Select Failing Target Wafer Bin In Bin Rule Details
#    And Select Target Wafer Bin In Combine Wafer Bin Details
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##   Rule 2
#Scenario: Create SWM Rule 4670-PrePostMerge-F-Missing
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-F-Missing
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Failing Source Wafer Bin In Bin Rule Details
#    And Select Missing Target Wafer Bin In Bin Rule Details
#    And Select Source Wafer Bin In Combine Wafer Bin Details
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##   Rule3
#Scenario: Create SWM Rule 4670-PrePostMerge-Missing-P
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-Missing-P
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Missing Source Wafer Bin In Bin Rule Details
#    And Select Passing Target Wafer Bin In Bin Rule Details
#    And Select Custom Bin In Combine Wafer Bin Details
#    And Enter Bin Number 60 & Name
#    And Select Probe Dies form Die Type
#    And Select Target Wafer In Other Fields Data
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##    Rule4
#Scenario: Create SWM Rule 4670-PrePostMerge-P-Missing
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-P-Missing
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Passing Source Wafer Bin In Bin Rule Details
#    And Select Missing Target Wafer Bin In Bin Rule Details
#    And Select Custom Bin In Combine Wafer Bin Details
#    And Enter Bin Number 61 & Name
#    And Select Probe Dies form Die Type
#    And Select Target Wafer In Other Fields Data
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##   Rule 5
#Scenario: Create SWM Rule 4670-PrePostMerge-Missing-Missing
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-Missing-Missing
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Missing Source Wafer Bin In Bin Rule Details
#    And Select Missing Target Wafer Bin In Bin Rule Details
#    And Select Target Wafer Bin In Combine Wafer Bin Details
#    And Click Save
#    Then close browser
#
##   Rule6
#Scenario: Create SWM Rule 4670-PrePostMerge-NA-F
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-NA-F
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select If Die Exist IN Only Target Wafer
#    And Select Failing Target Wafer Bin In Bin Rule Details
#    And Select Target Wafer Bin In Combine Wafer Bin Details
#    And Select Target In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##    Rule7
#Scenario: Create SWM 4670-PrePostMerge-F-NA
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-F-NA
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select If Die Exist IN Only Source Wafer
#    And Select Failing Source Wafer Bin In Bin Rule Details
#    And Select Source Wafer Bin In Combine Wafer Bin Details
#    And Select Source In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##   Rule8
#Scenario: Create SWM 4670-PrePostMerge-NA-P
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-NA-P
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select If Die Exist IN Only Target Wafer
#    And Select Passing Target Wafer Bin In Bin Rule Details
#    And Select Custom Bin In Combine Wafer Bin Details
#    And Enter Bin Number 60 & Name
#    And Select Target Wafer In Other Fields Data
#    And Select Probe Dies form Die Type
#    And Select Target In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##    Rule9
#Scenario: Create SWM 4670-PrePostMerge-P-NA
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-P-NA
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select If Die Exist IN Only Source Wafer
#    And Select Passing Source Wafer Bin In Bin Rule Details
#    And Select Custom Bin In Combine Wafer Bin Details
#    And Enter Bin Number 61 & Name
#    And Select Probe Dies form Die Type
#    And Select Target Wafer In Other Fields Data
#    And Select Source In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##   Rule10
#Scenario: Create SWM 4670-PrePostMerge-F-F
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-F-F
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Failing Source Wafer Bin In Bin Rule Details
#    And Select Failing Target Wafer Bin In Bin Rule Details
#    And Select Target Wafer Bin In Combine Wafer Bin Details
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##    Rule11
#Scenario: Create SWM 4670-PrePostMerge-F-P
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-F-P
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Failing Source Wafer Bin In Bin Rule Details
#    And Select Passing Target Wafer Bin In Bin Rule Details
#    And Select Source Wafer Bin In Combine Wafer Bin Details
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##    Rule12
#Scenario: Create SWM 4670-PrePostMerge-P-F
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-P-F
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Passing Source Wafer Bin In Bin Rule Details
#    And Select Failing Target Wafer Bin In Bin Rule Details
#    And Select Target Wafer Bin In Combine Wafer Bin Details
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##    Rule13
#Scenario: Create SWM 4670-PrePostMerge-P-P
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-PrePostMerge-P-P
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Passing Source Wafer Bin In Bin Rule Details
#    And Select Passing Target Wafer Bin In Bin Rule Details
#    And Select Target Wafer Bin In Combine Wafer Bin Details
#    And Select Both In Copy Parametric Data
#    And Click Save
#    Then close browser
#
##   Rule14
#Scenario: Create SWM 4670-Delta Merge
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-Delta Merge
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Bin Rule Type Bin & Parametric Rule
#    And Select Passing Source Wafer Bin In Bin Rule Details
#    And Select Passing Target Wafer Bin In Bin Rule Details
#    And Select Source Parameter 62 idd Post Stress mA
#    And Select Target Parameter 3 idd Post Bake mA
#    And Select Delta Parameter 500 idd Delta Post Bake mA
#    And Enter test value 10 & delta value 0
#    And Select Custom Bin In Combine Wafer Bin Details
#    And Enter Bin Number 41 & Name
#    And Select Target Wafer In Other Fields Data
#    And Select Probe Dies form Die Type
#    And Select Both In Copy Parametric Data
#    And Click on Combine Wafer Bin 2 Details
#    And Select Custom Bin In Combine Wafer Bin Details For 2nd
#    And Enter Bin Number 40 & Name For 2nd
#    And Select Target Wafer In Other Fields Data For 2nd
#    And Selected Probe Dies From Die Type For 2nd
#    And Select Both In Copy Parametric Data For 2nd
#    And Click Save
#    Then close browser
#
##    Rule15
#Scenario: Create SWM 4670-Delta1 Merge
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Rules.
#    And Verify that SWM Rules Page has been opened.
#    And Click on New SWM Rule to create new rule.
#    And Enter the SWM Rule Name as 4670-Delta1 Merge
#    And Enter the Description.
#    And Click on Input Data Selection.
#    And Select Rules Validation Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Source Device
#    And Select 4670 Target Device
#    And Click on Rule Definition Page.
#    And Select Bin Rule Type Bin & Parametric Rule
#    And Select Source Parameter 62 idd Post Stress mA
#    And Select Target Parameter 2 idd Post Bake mA
#    And Select Delta Parameter 501 idd Delta Post Bake mA
#    And Enter test value 10 & delta value 0
#    And Select Custom Bin In Combine Wafer Bin Details
#    And Enter Bin Number 51 & Name
#    And Select Target Wafer In Other Fields Data
#    And Select Probe Dies form Die Type
#    And Select Both In Copy Parametric Data
#    And Click on Combine Wafer Bin 2 Details
#    And Select Custom Bin In Combine Wafer Bin Details For 2nd
#    And Enter Bin Number 50 & Name For 2nd
#    And Select Target Wafer In Other Fields Data For 2nd
#    And Selected Probe Dies From Die Type For 2nd
#    And Select Both In Copy Parametric Data For 2nd
#    And Click Save
#    Then close browser
#
##    SWM NGC Silicon Custom Policy
#Scenario: Policy End To End
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on SWM Policies
#    And Click on the New SWM Policy.
#    And Enter SWM Policy name and Descriptions
#    And Click on the input data and rules selections
#    When Click on Test Program Options radio button Custom
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Target Device
#    And Select 4670 Source Device
#    And Click on Manage Test Program
#    And Select Prebake_A_4670 - Postbake_A_4670 & Click Add
#    And Select Prebake_A_4670 - Postbake_B_4670 & Click Add
#    And Select Prebake_B_4670 - Postbake_B_4670 & Click Add
#    And Select Prebake_A_stdf_4670 - Postbake_A_stdf_4670 & Click Add
#    And Select PREBAKE_-_STDF_4670 - POSTBAKE_-_STDF_4670 & Click Add
#    And Select & order rules
#    And Click on the output data Selection tab.
#    And Click on Merge Work Center, Clear it and And Wafer Sort into the Merge Work Center Field
#    And Selected all from Die Type Details from Source and Target Wafer
#    And Click On Save And Verify Policy is Saved
#
##        Automate Policy
#Scenario: Automate the Created Policy
#    Given I am on the home page
#    When Click on SWM Dropdown.
#    And Click on Automate SWM Policies from dropdown
#    And Click on Automate SWM Policy Button
#    And Select SILICON Source Facility
#    And Select SILICON Target Facility
#    And Select 4670 Target Device
#    And Select 4670 Source Device
#    And Select the created Policy
#    And Click on Save Button
#    And Click on Checkbox to automate the policy
#    And Click on Yes from Confirmation Required Pop-up Window
#    And Verify Confirmation Message
#    Then close browser
