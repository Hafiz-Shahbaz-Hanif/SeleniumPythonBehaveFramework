Feature: SWM Dashboard

@YWPD-TC-857 @retry
	Scenario: YWPD-TC-857 - Verify that the user views the status and information of automated SWM Policies having
processed and pending wafers in 'SWM Status by Devices' and 'Wafer Processed List' table in SWM Dashboard
	The objective of this test case is to ensure that the users can successfully view the generated and pending wafers list.
		Given The user in on the main screen
		When User clicks on SWM Dropdown from Left Menu
		When Click on "SWM Dashboard"
		When SWM Dashboard window will open with "SWM Status by Devices" table and "Wafer Processed List" table
		When Verify that "SWM Status by Devices" table having "Source Facility", "Source Work Center"
		When Also verify "Source Device", "Target Facility", "Target Work Center"
		When Also verify the display of "Target Device", "No.of Policies", "Is Automated"
   		When And verify the "Processed Wafers" and "Remaining Wafers" columns
		When Click on the device from available devices list in "SWM Status by Device" table
		When Verify that the "Show Inactive Wafers checkbox" is checked by default
		When Automated policy will appear in Wafer Processed List with
			 """
			 Policy Name,  Policy Version, Facility, Work Center, Device, Test Program, Lot ID, Wafer ID, Test
			 Temprature, Source Wafer Bin Yield, Target Wafer Bin Yield, Combine Wafer Bin Yield, Source Yield Loss/Gain, Target Yield
			 Loss/Gain, Wafer Status, and Wafer Active Status' information
			 """
		Then All the related pending and processed wafer has been displayed
			 """
			 based on the selected device from "SWM Status by Device" table
			 """
