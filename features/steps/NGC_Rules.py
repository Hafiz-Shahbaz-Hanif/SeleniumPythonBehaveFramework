from behave import *

from Logs.LoginPage import LoginClass
from Pages.NGC_Rules import swmNgcSiliconClass
from Pages.PAT import PATClass
from Pages.PF_SWM.PF_MunualSWM import ManualSWM
from Pages.SWM import SWMClass
from utilities.customLogger import LogGen

lg = LoginClass()
pt = PATClass()
ngc = swmNgcSiliconClass()
swm = SWMClass()
logger = LogGen.loggen()
manualSWM = ManualSWM()


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-Missing-F')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_Missing_F(context)


@when(u'Select Rules Validation Custom')
def step_impl(context):
    ngc.selectCustomRules(context)


@when(u'Select SILICON Source Facility')
def step_impl(context):
    ngc.selectSourceFacility(context)


@when(u'Select SILICON Target Facility')
def step_impl(context):
    ngc.selectTargetFacility(context)


@when(u'Select 4670 Source Device')
def step_impl(context):
    ngc.selectSourceDevice(context)


@when(u'Select 4670 Target Device')
def step_impl(context):
    ngc.selectTargetDevice(context)


@when(u'Select Missing Source Wafer Bin In Bin Rule Details')
def step_impl(context):
    ngc.missingSourceBinRuleDetails(context)


@when(u'Select Failing Target Wafer Bin In Bin Rule Details')
def step_impl(context):
    ngc.failingTargetBinRuleDetails(context)


@when(u'Select Target Wafer Bin In Combine Wafer Bin Details')
def step_impl(context):
    ngc.targetWaferBinInCombineWaferBin(context)


@when(u'Select Both In Copy Parametric Data')
def step_impl(context):
    ngc.bothInCopyParametricData(context)


@when(u'Click Save')
def step_impl(context):
    swm.saveButton(context)


# ****************** 2nd Rule 4670-PrePostMerge-F-Missing ****************************

@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-F-Missing')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_F_Missing(context)


@when(u'Select Missing Target Wafer Bin In Bin Rule Details')
def step_impl(context):
    ngc.missingTargetBinRuleDetails(context)


@when(u'Select Failing Source Wafer Bin In Bin Rule Details')
def step_impl(context):
    ngc.failingSourceBinRuleDetails(context)


@when(u'Select Source Wafer Bin In Combine Wafer Bin Details')
def step_impl(context):
    ngc.sourceWaferBinInCombineWaferBin(context)


# **************** 3rd Rule 4670-PrePostMerge-Missing-P

@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-Missing-P')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_Missing_P(context)


@when(u'Select Passing Target Wafer Bin In Bin Rule Details')
def step_impl(context):
    ngc.passingTargetBinRuleDetails(context)


@when(u'Select Custom Bin In Combine Wafer Bin Details')
def step_impl(context):
    ngc.customInCombineWaferBin(context)


@when(u'Enter Bin Number 60 & Name')
def step_impl(context):
    ngc.enter60BinNumberName(context)


@when(u'Select Probe Dies form Die Type')
def step_impl(context):
    ngc.selectDieType(context)


@when(u'Select Target Wafer In Other Fields Data')
def step_impl(context):
    ngc.targetInOtherFieldsData(context)


# **************** 4rd Rule 4670-PrePostMerge-P-Missing

@when(u'Enter Bin Number 61 & Name')
def step_impl(context):
    ngc.enter61BinNumberName(context)


# @when(u'Select Probe Dies form Die Type')
# def step_impl(context):
#     ngc.selectDieType(context)

@when(u'Select Source Wafer In Other Fileds Data')
def step_impl(context):
    ngc.sourceInOtherFieldsData(context)


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-P-Missing')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_P_Missing(context)


@when(u'Select Passing Source Wafer Bin In Bin Rule Details')
def step_impl(context):
    ngc.passingSourceBinRuleDetails(context)


# **************** 5th Rule 4670-PrePostMerge-Missing-Missing

@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-Missing-Missing')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_Missing_Missing(context)


# **************** 6th Rule 4670-PrePostMerge-NA-F

@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-NA-F')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_NA_F(context)


@when(u'Select Target In Copy Parametric Data')
def step_impl(context):
    ngc.targetInCopyParametricData(context)


@when(u'Select If Die Exist IN Only Target Wafer')
def step_impl(context):
    ngc.ifDieExistINOnlyTargetWafer(context)


# **************** 7th Rule 4670-PrePostMerge-F-NA


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-F-NA')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_F_NA(context)


@when(u'Select If Die Exist IN Only Source Wafer')
def step_impl(context):
    ngc.ifDieExistINOnlySourceWafer(context)


@when(u'Select Source In Copy Parametric Data')
def step_impl(context):
    ngc.sourceInCopyParametricData(context)


# **************** 8th Rule 4670-PrePostMerge-NA-P


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-NA-P')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_NA_P(context)


# **************** 9th 4670-PrePostMerge-P-NA


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-P-NA')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_P_NA(context)


# **************** 10th 4670-PrePostMerge-F-F


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-F-F')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_F_F(context)


# **************** 11th 4670-PrePostMerge-F-P


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-F-P')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_F_P(context)


# **************** 12th 4670-PrePostMerge-P-F


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-P-F')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_P_F(context)


# **************** 13th 4670-PrePostMerge-P-P


@when(u'Enter the SWM Rule Name as 4670-PrePostMerge-P-P')
def step_impl(context):
    ngc.enterName4670_PrePostMerge_P_P(context)


# **************** 14th 4670-Delta Merge


@when(u'Enter the SWM Rule Name as 4670-Delta Merge')
def step_impl(context):
    ngc.enterName4670_DeltaMerge(context)


@when(u'Select Bin Rule Type Bin & Parametric Rule')
def step_impl(context):
    ngc.binRuleTypeBinParametricRule(context)


@when(u'Select Source Parameter 62 idd Post Stress mA')
def step_impl(context):
    ngc.sourceParameter62_iddPostStress_mA(context)


@when(u'Select Target Parameter 3 idd Post Bake mA')
def step_impl(context):
    ngc.targetParameter3_iddPostBake_mA(context)


@when(u'Select Delta Parameter 500 idd Delta Post Bake mA')
def step_impl(context):
    ngc.deltaParameter500_iddDeltaPostBake_mA(context)


@when(u'Enter test value 10 & delta value 0')
def step_impl(context):
    ngc.enterTestDeltaValues(context)


@when(u'Enter Bin Number 41 & Name')
def step_impl(context):
    ngc.enter41BinNumberName(context)


@when(u'Click on Combine Wafer Bin 2 Details')
def step_impl(context):
    ngc.clickCombineWaferBin2Details(context)


@when(u'Select Custom Bin In Combine Wafer Bin Details For 2nd')
def step_impl(context):
    ngc.customInCombineWaferBin2(context)


@when(u'Enter Bin Number 40 & Name For 2nd')
def step_impl(context):
    ngc.enter40BinNumberName(context)


@when(u'Select Target Wafer In Other Fields Data For 2nd')
def step_impl(context):
    ngc.targetInOtherFieldsData2(context)


@when(u'Selected Probe Dies From Die Type For 2nd')
def step_impl(context):
    ngc.selectDieTypeD2(context)


@when(u'Select Both In Copy Parametric Data For 2nd')
def step_impl(context):
    ngc.bothInCopyParametricData2(context)


# **************** 15th 4670-Delta1 Merge


@when(u'Enter the SWM Rule Name as 4670-Delta1 Merge')
def step_impl(context):
    ngc.enterName4670_Delta1Merge(context)


@when(u'Select Target Parameter 2 idd Post Bake mA')
def step_impl(context):
    ngc.targetParameter2_iddPostBake_mA(context)


@when(u'Select Delta Parameter 501 idd Delta Post Bake mA')
def step_impl(context):
    ngc.deltaParameter501_Delta1(context)


@when(u'Enter Bin Number 51 & Name')
def step_impl(context):
    ngc.enter51BinNumberName(context)


@when(u'Enter Bin Number 50 & Name For 2nd')
def step_impl(context):
    ngc.enter50BinNumberName(context)


@when(u'Click on Test Program Options radio button Custom')
def step_impl(context):
    ngc.testProgramOptionAsCustom(context)


@when(u'Click on Manage Test Program')
def step_impl(context):
    ngc.clickManageTestProgram(context)


@when(u'Select Test Program Mapping')
def step_impl(context):
    ngc.selectTestProgramMapping(context)
    ngc.clickApplyButton(context)


@when(u'Select & order rules')
def step_impl(context):
    ngc.giveOrder(context)
    ngc.selectAllRules(context)


@when(u'Click on Merge Work Center, Clear it and And Wafer Sort into the Merge Work Center Field')
def step_impl(context):
    ngc.mergeWorkCenterInputField(context)


@when(u'Selected all from Die Type Details from Source and Target Wafer')
def step_impl(context):
    ngc.selectDieTypesDetailOutputTab(context)


#     Automate the Policy

@when(u'Click on Automate SWM Policies from dropdown')
def step_impl(context):
    ngc.clickAutomatePolicyDropdown(context)


@when(u'Click on Automate SWM Policy Button')
def step_impl(context):
    ngc.automateSWMPolicyBtn(context)


@when(u'Select the created Policy')
def step_impl(context):
    ngc.createdPolicySelect(context)


@when(u'Click on Save Button')
def step_impl(context):
    ngc.saveAutomatePolicy(context)


@when(u'Click on Checkbox to automate the policy')
def step_impl(context):
    ngc.automatePolicyCheckbox(context)


@when(u'Click on Yes from Confirmation Required Pop-up Window')
def step_impl(context):
    ngc.automateConfirmation(context)


@when(u'Verify Confirmation Message')
def step_impl(context):
    ngc.automateSuccessConfirmation(context)

