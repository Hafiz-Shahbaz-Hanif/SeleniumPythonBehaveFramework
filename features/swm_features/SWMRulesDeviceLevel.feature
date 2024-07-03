Feature: SWM Device Level Rules with Web Small Data Set

	@YWPD-TC-319 @retry
	Scenario Outline: YWPD-TC-319 - Verify that the user is able to create SWM Rule at Device Level and Rules
	Validation 'Custom', with web small dataset
	The objective of this test case is to ensure that the users can successfully create SWM Rule at Device Level and Rules Validation 'Custom', with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Rules
		When Click on "New SWM Rule" button from SWM Rules window
		When Create SWM Rules window will open and enter name as "<Name>" And description in "General" tab
		When Click the "Input Data Selection" tab and Select level as "<Level>", Rules Validation as "<Rules Validation>"
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select the source device as "<Source Device>" and source probe as (1|M)
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Probe as (1|M) and Target Device as "<Target Device>"
		When Click "Rule Definition" tab And Select rule Type from "<Select Rule Type>" drop down
		When Select one option from Die Exist in Wafers as "<Die Exist in Wafers>"
		When Select Source Wafer Bin as
			| Source Bin   |
			| <Source Bin> |
		When Select Target Wafer Bin as
			| Target Bin   |
			| <Target Bin> |
		When Select "Combine Bin" option from Combine Wafer Bin Details as "<Combine Wafer Bin Details>"
		When Provide Hard Bin Number as "<Hard Bin Number>", Soft Bin Number as "<Soft Bin Number>"
		When Select Bin Flag and other fields data
		When Select Die Type as "<Die Type>"
		When Select the one option from "<Copy Parametric Data (PTR,FTR & MPR) From>"
		When Enable "Copy bin number, probe site, reticle site and die type data as parameters?" checkbox if needed
		When Click "Email Notification" tab
		When Enter valid "Owner Name", "Owner Email Address" And Enter additional emails if needed
		When Click the "Save" button
		Then Verify that the rule will be saved and appear in the SWM Rules window
		"""
		SWMRules table in database, and email will be sent at your given email (s)
		"""

	Examples:
		| Name                              | Level  | Rules Validation | Source Facility   | Source Work Center | Source Device | Target Facility   | Target Work Center | Target Device | Select Rule Type | Die Exist in Wafers                        | Combine Wafer Bin Details | Hard Bin Number | Soft Bin Number | Die Type     | Copy Parametric Data (PTR,FTR & MPR) From | Source Bin   | Target Bin  |
		| 4670-PrePostMerge-P-P             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Passing      | Passing     |
		| 4670-PrePostMerge-P-F             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Passing      | Failing     |
		| 4670-PrePostMerge-F-P             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Source Wafer BIN          | NA              | NA              | NA           | Both                                      | Failing      | Passing     |
		| 4670-PrePostMerge-F-F             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Failing      | Failing     |
		| 4670-PrePostMerge-Missing-Missing | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | None                                      | Missing      | Missing     |
		| 4670-PrePostMerge-P-Missing       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Custom BIN                | 61              | 61              | Probe Die(s) | Both                                      | Missing      | Passing     |
		| 4670-PrePostMerge-Missing-P       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Custom BIN                | 60              | 60              | Probe Die(s) | Both                                      | Passing      | Missing     |
		| 4670-PrePostMerge-F-Missing       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Source Wafer BIN          | NA              | NA              | NA           | Both                                      | Missing      | Failing     |
		| 4670-PrePostMerge-Missing-F       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Failing      | Missing     |
		| 4670-PrePostMerge-P-NA            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Source Wafer             | Custom BIN                | 61              | 61              | Probe Die(s) | Source Wafer                              |              | Passing     |
		| 4670-PrePostMerge-F-NA            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Source Wafer             | Source Wafer BIN          | NA              | NA              | NA           | Source Wafer                              |              | Failing     |
		| 4670-PrePostMerge-NA-P            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Target Wafer             | Custom BIN                | 60              | 60              | Probe Die(s) | Target Wafer                              | Passing      |             |
		| 4670-PrePostMerge-NA-F            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Target Wafer             | Target Wafer BIN          | NA              | NA              | NA           | Target Wafer                              | Failing      |             |