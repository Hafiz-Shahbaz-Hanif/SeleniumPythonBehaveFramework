Feature: SWM Rules Bin Type

	@YWPD-TC-1207 @retry
	Scenario Outline: YWPD-TC-1207 - Verify that user is able to create & save SWM Bin Type Rules
		Given The user has successfully launched Web Application and logged in
		When Clicks on SWM Dropdown from the menu displayed on left side
		When Click on SWM Rules
		When Click "New SWM Rule" button from SWM Rules window
		When Enter a Rule Name and Description in the "General" tab
		When Select the "Input Data Selection" Tab
		When Select "<Source/Target Data Set Size>", "<Source/Target Probe>"
		When Then select "<Level>", "<Bin Type>", "<Rule Validation>"
		When Click on "Rule Definition" tab
		When After that select the "<Rule Type>", "<Bin Rule Detail>", "<Combine Wafer Bin>"
	    When Enter the "<Hard Bin Number / Name>", "<Soft Bin Number / Name>"
		When After that select "<Bin Flag / Other Fields Data>", "<Die Type>", "<Copy Parametric Data From>"
		When Click "Email Notification" tab
		When Enter valid "Owner Name", "Owner Email Address"
		When Enter "Additional emails" if needed
		When Click the "Save" button
		Then Verify that the rule has been saved successfully

	Examples:
		| Source/Target Data Set Size | Source/Target Probe | Level  | Bin Type | Rule Validation | Rule Type | Bin Rule Detail | Combine Wafer Bin | Hard Bin Number / Name | Soft Bin Number / Name | Bin Flag / Other Fields Data | Die Type     | Copy Parametric Data From |
		| Web Small Dataset           | 1M/1M               | Device | Hard Bin | All             | Bin Rule  |Both,Any,Any     | Custom BIN        | 30 / Rule 1H           | 30 / Rule 1S           | Fail, Source Wafer           | Probe Die(s) | None                      |