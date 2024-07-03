Feature: Automate SWM Policies

	@YWPD-TC-336 @retry
	Scenario Outline: YWPD-TC-336 - Verify that the user is able to automate SWM Policies successfully with web small
	dataset
	The objective of this test case is to ensure that the users can successfully automate SWM Policies with web small dataset. Additionally, this test case aims to validate the functionality of saved auto SWM wafer (C) in yieldWerx desktop application through Wafer Map Report.
		Given The user is successfully logged in the yieldWerx web application
		When Click on "SWM" in the left menu bar
		When Click "Automate SWM Policies" and new window will open
		When Click on "Automate SWM Policy" and Create Automate SWM Policy window will open
		When Select Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select Source Device as "<Source Device>", Source Test Program as "<Source Test Program>"
		When Select the Target Facility as "<Target Facility>", Target Work Center as "<Target Work Center>"
		When Select Target Device as "<Target Device>", Target Test Program as "<Target Test Program>"
		When Select policy from Policies as "<Policies>" section and click on "Save" button
		When SWM Policy has been created and displayed in "Automate SWM Policies" window
		When Enable check box available infront of each created Automate SWM Policy in Automate SWM Policies window to automate the policy
		Then Verify that the policy will be automated with success message


		# following steps of this scenario are related to desktop app
#		When Combine wafer (C) will be saved in yieldWerx desktop application against selection
#		When Select wafer table in database, provide Lot_Sequence, and see the C wafer with probing sequence = -8
#		When Open yieldWerx desktop application and open Bin Wafer Map report
#		When Select that facility where SWM Combine Wafer Map has been saved
#		When Combine wafer has been displayed with probe count C against the selected facility
#		Then Verify the <Expected Chart>
#		When Click Legend button available in right bottom right corner of generated chart of C wafer in gallery view
#		Then Verify the <Expected Legend>

	Examples:
		| Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility   | Target Work Center | Target Device | Target Test Program | Policies          | Expected Chart                                                                      | Expected Legend                                                                                                                                                  |
		| WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670 Test Program | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_WM_C_Chart.jpg | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_WM_C_Legend.jpg                                                                             |
		| WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670 device       | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_WM_C_Chart.jpg       | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_WM_C_Legend1.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_WM_C_Legend2.jpg |


	@YWPD-TC-337 @retry
	Scenario: YWPD-TC-337 -Verify that the user is able to Un-Automate SWM Policies with web small dataset
	The objective of this test case is to ensure that the users can successfully Un-Automate SWM Policies with web small dataset.
		Given The user is successfully logged in the yieldWerx web application
		When Click on "SWM" in the left menu bar
		When Click "Automate SWM Policies" and new window will open
		When See the list of already created Automate SWM Policies
		When Uncheck the check box available infront of already automated SWM Policy
		When Confirmation Required pop-up window with options "Yes, No, Cancel" will open
		When Click Yes to un-automate the Policy
		Then Verify that the policy will be un-automated and window of Automate SWM Policies will be refresh


	@YWPD-TC-338 @retry
	Scenario: YWPD-TC-338 - Verify that the user is able to delete automated SWM Policies successfully with web small
	dataset
	The objective of this test case is to ensure that the users can successfully delete automated SWM Policies with web small dataset.
		Given The user is successfully logged in the yieldWerx web application
		When Click on "SWM" in the left menu bar
		When Click "Automate SWM Policies" and new window will open
		When See the list of already created Automate SWM Policies
		When Click the "Delete" button available at the end of already created and automated SWM Policy
		When Confirmation Required pop-up window with options "Yes, No, Cancel" will open
		When Click Yes to delete the policy
		Then Verify that the policy will be deleted from Automate SWM Policies window
#		Then The policy will remove from "SWMAutomatedPolicies" table in database