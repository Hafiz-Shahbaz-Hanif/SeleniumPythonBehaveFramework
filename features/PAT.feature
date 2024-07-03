#
#Feature: PAT
#
#
#
#  Scenario: Creating the PAT Policy of created PAT Rule.
#    Given Now we were at PAT Rules Screen after creating one PAT Rule.
#    When Created rule displayed on dashboard then click on PAT Policies.
#    And Check that the PAT Policy page displayed.
#    And Click on New Policy.
#    And Give the Policy Name in the Policy Name Text Field.
#    And Select the type of policy that it is device level or program level by using Type dropdown.
#    And Selected the device from devices dropdown.
#    Given Launch Chrome Browser.
#    When yieldWerx Web Module Launched.
#    And Verified that the application logged In successfully.
#    And Clicked on PAT Dropdown.
#    And Clicked on PAT Rules.
#    And Verified that the PAT Rules page has been Opened.
#    And Clicked on New Dynamic PAT.
#    And Verified that the Create PAT Rule page has been displayed.
#    And Enter the PAT Rule Name.
#    And Select the Parameter Tab.
#    And Select the Facility from Parameter Tab.
#    And Select the Work Center from Parameter Tab of that facility.
#    And Select the Device from Parameter Tab of that facility and work center.
#    And Select the Test Program related to Facility, work center and device.
#    And Selected the Parameter from that selected test program.
#    And Select the Dynamic Limit Tab.
#    And Selected PAT Distribution to Unknown and verify
#    And Find and Enter Bin Number.
#    And Find and Enter Bin Name.
#    And Click on that Save Button.
#    And Get the Success Message.
#    And Close the browser.
#
#
#  Scenario: Creating Static Device Level PAT Rule
#    Given I am on the On the PAT Rule Page.
#    When Clicked on New Static PAT Rule.
#    And Verified that the Create PAT Rule page has been displayed.
#    And Enter the PAT Rule Name.
#    And Select the Parameter Tab.
#    And Select the Facility from Parameter Tab.
#    And Select the Work Center from Parameter Tab of that facility.
#    And Select the Device from Parameter Tab of that facility and work center.
#    And Select the Test Program related to Facility, work center and device.
#    And Selected the Parameter from that selected test program.
#    And Check the Apply PAT Rule to device level CheckBox.
#    And Select the Static Limit Tab.
#    And Calculate the Seed Limits.
#    And EnterRe-Calculate Static Limits After.
#    And Find and Enter Static Bin Number.
#    And Find and Enter Static Bin Name.
#    And Select Email Notification Tab.
#    And Enter Name & Email.
#    And Click on that Save Button.
#    And Get the Success Message.
#    And Close the browser.
#    And Selected the Test Program from Test Programs dropdown.
#    And Click on the checkbox of created rule.
#    And Click on Save Button.
#    Then Verify policy is created.
#
#
#  Scenario: Run the PAT Policy Manually.
#    Given Click on Manual PAT.
#    When Select the Facility for Manual PAT.
#    And Select the Work Center for Manual PAT.
#    And Select the Device  for Manual PAT.
#    And Select the Test Program on which PAT Policy is created.
#    And Select the Lot  for Manual PAT.
#    And Select the wafer  for Manual PAT.
#    And Select the Created Policy  for Manual PAT.
#    And Click on Calculate Manual PAT button.
#    And Verify that the Manual PAT Wafer Viewed.
#    And Click on Save to YieldWerx Button.
#    Then Verify Success message of saved
#    And Click on Export Button.
#    Then Check the Wafer Exported  & Close Browser.
#
#
#  Scenario: Create Automate Business Rule.
#    Given We were at Home screen after creating PAT policy.
#    When Click on Automate business rule from PAT dropdown.
#    And Click on Create Automate Business Policy Rule.
#    And Select the Facility.
#    And Select the Work Center.
#    And Select the Device
#    And Select the Test Program
#    And Selected the created policy from policies section in Create Automate Business Policy Rule Page.
#    And Click on the Save Button.
#    Then Verify Record is created and Delete it.
#
#
#  Scenario: Automate the Created Business Rule Setup.
#    Given Now the Automated Business Rule Setup Created.
#    When Verify that the rule is created and displayed.
#    And Click on the unchecked check box and mark as checked.
#    And Verify that the pop up window appears & Click on the Yes to automate the policy.
#    And Automated Successfully Message Displayed.
#    And Check the status is completed.
#    And Close the Browser.
#
#
#  Scenario: End to End Cycle of Manual PAT Module.
#    Given Click on PAT Module.
#    When Select the Facility From Manual PAT Module.
#    And Select the Work Center From Manual PAT Module.
#    And Select the Device From Manual PAT Module.
#    And Select the Test Program on which PAT Policy is created From Manual PAT Module.
#    And Select the Lot From Manual PAT Module.
#    And Select the wafer From Manual PAT Module.
#    And Select the Created Policy From Manual PAT Module.
#    And Click on Calculate Manual PAT button From Manual PAT Module.
#    And Verify that the Manual PAT Wafer Viewed From Manual PAT Module.
#    And Select checked "Enable Multi Site DPAT Functionality" From Manual PAT Module.
#    And Click on Execute button From Manual PAT Module.
#    And Click on Wafer Map tab and then click on Legend in Wafer Map Tab and then close the legend From Manual PAT Module.
#    And Click on Histogram Tab and then click on Legend of Histogram and close the legend From Manual PAT Module.
#    And Click on Trend Tab and then click on Legend of Trend and close the legend From Manual PAT Module.
#    And Click on Zoom button of Die Loss Section and close the tab From Manual PAT Module.
#    And Click on Zoom button of By Wafer, Pass and Fail Count and Close the tab From Manual PAT Module.
#    And Click on Zoom button of By Lot, Pass and Fail Count and Close the tab From Manual PAT Module.
#    And Select Die to downgrade and Click on downgrade button From Manual PAT Module.
#    And Click on Orignal Bin Wafer Map Zoom,Verify new window Open & close new Window & Back to Main window
#    And Click on PAT Both Limits Wafer Map Zoom,Verify new window Open & close new Window & Back to Main window
#    And Click on Save Button From Manual PAT Module.
#    Then Verify success message From Manual PAT Module & Close Browser.
#
#
#
#
#
#
#
#
