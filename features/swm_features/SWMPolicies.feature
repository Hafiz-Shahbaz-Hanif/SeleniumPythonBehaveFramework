Feature: SWM Policies

	@YWPD-TC-328 @retry
	Scenario Outline: YWPD-TC-328 - Verify that the user is able to create SWM Policy at Test Program Level with web small dataset
	The objective of this test case is to ensure that the users can successfully create SWM Policy at Test Program Level with web small dataset
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When Click New SWM Policy button from SWM Policies window
		When Create SWM Policy Window will open
		When Enter "<Name>" And description in "General" tab
		When Click "Input Data & Rule Selection" And Select "<Level>" from dropdown
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select Source Device as "<Source Device>"
		When Select Source Probe as "(1|M)" and Source Test Program as "<Source Test Program>"
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Device as "<Target Device>"
		When Select Target Test Program as "<Target Test Program>", Target Probe "(1|M)"
		When Select "<Rules>" from the Rules section
		When Click "Output Data Selection" tab and provide all the information like
			 """
			 Metadata Selection From, Merge Facility, Merge Work Center, Merge Device, Merge Test Program
			 """
		When Enter the information for
			 """
			 Source Parameter Prefix, Target Parameter Prefix,
			 Delta Parameter Prefix in 'Parameter Generation Option' tab if required otherwise keep it as default
			 """
		When Enter the information for "Wafer Rotation" like
			 """
	  		 'Rotate Wafer, Apply Offset, Include Die Types' if required otherwise keep it as default
	  		 """
		When Select Die Type Details by using checkbox
		When Click Manage Exception tab and select the required option otherwise keep it as default
		When Click Save button to save the new created policy
		Then Verify that the policy has been saved and appears in the SWM Policies window
			 """
			 and in "SWMPolicies" table in database
			 """

	Examples:
		| Name                   | Level        | Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility    | Target Work Center | Target Device | Target Test Program | Rules                                                                                                                                             |
		| SWM_Policy_TestProgram | Test Program | WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATA SET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670-PrePostMerge-P-P _TestProgram, 4670-PrePostMerge-F-F - TestProgram, 4670-PrePostMerge-P-F - TestProgram, 4670-PrePostMerge-F-P - TestProgram |



	@YWPD-TC-330 @retry
	Scenario Outline: YWPD-TC-330 - Verify that the user is able to create SWM Policy at Device Level Custom Test Program with web small dataset
	The objective of this test case is to ensure that the users has successfully created SWM Policy on Device Level Custom Test Program with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When Click New SWM Policy button from SWM Policies window
		When Create SWM Policy Window will open
		When Enter "<Name>" And description in "General" tab
		When Click "Input Data & Rule Selection" And Select "<Level>" from dropdown
		When Select "<Test Program Options>" as Custom
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select Source Device as "<Source Device>"
		When Select "(1|M)" as a Source Probe
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Device as "<Target Device>"
		When Select the "(1|M)" option as Target Probe
		When Select "<Rules>" from the Rules section
		When Click on Manage Test Programs Hyperlink and provide Test Programs Mapping
		When Select Source Test Program and Target Test Program from their respective dropdowns and click Add button
		When Click Apply button after adding
			 """
			 Source Test Program and Target Test Program,
	 		 Test Program Mapping has been applied
	 		 """
		When Click "Output Data Selection" tab and provide all the information like
			 """
			 Metadata Selection From, Merge Facility, Merge Work Center, Merge Device, Merge Test Program
			 """
		When Enter the information for
			 """
			 Source Parameter Prefix, Target Parameter Prefix,
			 Delta Parameter Prefix in 'Parameter Generation Option' tab if required otherwise keep it as default
			 """
		When Enter the information for "Wafer Rotation" like
			 """
	  		 'Rotate Wafer, Apply Offset, Include Die Types' if required otherwise keep it as default
	  		 """
		When Select Die Type Details by using checkbox
		When Click Manage Exception tab and select the required option otherwise keep it as default
		When Click Save button to save the new created policy
		Then Verify that the policy has been saved and appears in the SWM Policies window
			 """
			 and in "SWMPolicies" table in database
			 """

	Examples:
		| Name                     | Level  | Test Program Options | Source Facility    | Source Work Center | Source Device | Target Facility    | Target Work Center | Target Device | Rules                                                                                                                                                                                                                                                                                                                                              |
		| SWM_Policy_Device_Custom | Device | Custom               | WEB SMALL DATA SET | WAFER SORT         | 4670          | WEB SMALL DATA SET | WAFER SORT         | 4670          | 4670-PrePostMerge-P-P, 4670-PrePostMerge-P-F, 4670-PrePostMerge-F-P, 4670-PrePostMerge-F-F, 4670-PrePostMerge-Missing-Missing, 4670-PrePostMerge-P-Missing, 4670-PrePostMerge-Missing-P, 4670-PrePostMerge-F-Missing, 4670-PrePostMerge-Missing-F, 4670-PrePostMerge-P-NA, 4670-PrePostMerge-F-NA, 4670-PrePostMerge-NA-P, 	4670-PrePostMerge-NA-F |


	@YWPD-TC-331 @retry
	Scenario: YWPD-TC-331 - Verify that the user is able to Modify SWM Policy successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully Modify SWM Policy with web small dataset.
		Given The user successfully opened the yieldWerx web application
		When Click on SWM Policies and SWM Policies Window will open
		When See the list of already created SWM policies
		When Click 'Edit' button available for each policy
		When Create SWM Policy window will open and make changes that you want in 'General' tab, 'Input Data & Rule Selection', 'Output Data Selection' and 'Manage Exceptions
		When Change Bin Type and Test Program Options.
		When Click 'Output Data Selection' tab And change all the information like Metadata Selection From, Merge Facility, Merge Work Center, Merge Device, Merge Test Program if want to change the default information
		When Change Information for Source Parameter Prefix, Target Parameter Prefix, Delta Parameter Prefix in 'Parameter Generation Option' tab, if want to change the default information
		When Change information for 'Wafer Rotation' like 'Rotate Wafer, Apply Offset, Include Die Types' if want to change the default information
		When Change Die Type Details if user wants to change the default settings
		When Click Manage Exception tab, and change the settings of own choice if user wants to change the default settings
		When Click on Save button to save the policy
		Then Verify that the policy will be saved and appear in the SWM Policies window and in "SWMPolicies" table in database