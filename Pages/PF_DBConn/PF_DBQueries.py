import pyodbc
import json
from decimal import Decimal
from datetime import datetime
from utilities.Exceptions import MyException
from utilities.customLogger import LogGen


class PF_DBQueries:
    logger = LogGen.loggen()

    def __init__(self):
        conn_string = (
                        'DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=192.168.0.4,58840;DATABASE=yw_V4_Automation_4_2_25_0_AhsanMughal;'
                        'UID=sa;PWD=subway3328'
                      )
        self.conn = pyodbc.connect(conn_string)
        self.cursor = self.conn.cursor()

    def dataWaferTable(self, context):
        try:
            # Query to fetch wafer data from database
            query_result = self.cursor.execute("SELECT * FROM WAFER WHERE Wafer_Sequence='1201'").fetchone()

            # Store the result in the context if needed
            context.wafer_details_from_db = query_result

            self.logger.info("Query Wafer executed successfully")

            # Convert the Row object to a dictionary
            if query_result:
                wafer_table_column_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(wafer_table_column_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of Wafer:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            Wafer_Sequence = result_dict.get("Wafer_Sequence", None)
            Lot_Sequence = result_dict.get("Lot_Sequence", None)
            Wafer_ID = result_dict.get("Wafer_ID", None)
            Part_Count = result_dict.get("Part_Count", None)
            Good_Count = result_dict.get("Good_Count", None)
            Probing_Sequence = result_dict.get("Probing_Sequence", None)
            Total_Unique_Dies = result_dict.get("Total_Unique_Dies", None)
            Yield = result_dict.get("Yield", None)

            context.wafer_details_from_db = query_result_dict
            self.logger.info(f"Query Wafer executed successfully {Wafer_Sequence}, {Lot_Sequence}, {Wafer_ID} , {Part_Count}, {Good_Count}, {Probing_Sequence}, {Yield}")

        except Exception as e:
            self.logger.error("Error in testDatabase: %s", e)
            MyException.handle_exception(context, e)

    def dataSWMRule(self, context):
        try:
            # Query SQL Server and retrieve data
            query_result = self.cursor.execute("SELECT * FROM SWMRules ORDER BY 1 DESC").fetchone()

            # Store the result in the context if needed
            context.swm_rules_details_from_db = query_result
            self.logger.info("Query SWM Rule executed successfully")

            # Convert the Row object to a dictionary
            if query_result:
                swm_rule_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(swm_rule_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Rules:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            SWMR_ID = result_dict.get("ID", None)
            SWMR_Name = result_dict.get("Name", None)
            SWMR_Level = result_dict.get("Level", None)
            SWMR_Version = result_dict.get("Version", None)
            SWMR_SourceFacility = result_dict.get("SourceFacility", None)
            SWMR_SourceWorkCenter = result_dict.get("SourceWorkCenter", None)
            SWMR_SourceDevice = result_dict.get("SourceDevice", None)
            SWMR_SourceTestProgram = result_dict.get("SourceTestProgram", None)
            SWMR_SourceProbes = result_dict.get("SourceProbes", None)
            SWMR_TargetFacility = result_dict.get("TargetFacility", None)
            SWMR_TargetWorkCenter = result_dict.get("TargetWorkCenter", None)
            SWMR_TargetDevice = result_dict.get("TargetDevice", None)
            SWMR_TargetTestProgram = result_dict.get("TargetTestProgram", None)
            SWMR_TargetProbes = result_dict.get("TargetProbes", None)

            context.swm_rules_details_from_db = query_result_dict
            self.logger.info(
                f"Query Wafer executed successfully {SWMR_ID}, {SWMR_Name}, {SWMR_Level} , {SWMR_Version}, {SWMR_SourceFacility}, {SWMR_SourceWorkCenter}, {SWMR_SourceDevice}, "
                f"{SWMR_SourceTestProgram}, {SWMR_SourceProbes}, {SWMR_TargetFacility}, {SWMR_TargetWorkCenter}, {SWMR_TargetDevice}, {SWMR_TargetTestProgram}, {SWMR_TargetProbes}")

        except Exception as e:
            MyException.handle_exception(context, e)

    def dataSWMPolicy(self, context):
        try:
            # Query to retrieve SWM Policy Data
            query_result = self.cursor.execute("SELECT * FROM SWMPolicies ORDER BY 1 DESC").fetchone()
            self.logger.info("Query Result of SWM Policy: %s",  query_result)

            # Convert the Row object to a dictionary
            if query_result:
                swm_policy_table_names = [column[0] for column in self.cursor.description]
                swmpolicy_query_result_dict = dict(zip(swm_policy_table_names,  query_result))
            else:
                swmpolicy_query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            swmpolicy_query_result_dict = self.convert_datetimes_and_decimals(swmpolicy_query_result_dict)
            formatted_result = json.dumps(swmpolicy_query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Rules:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            SWMP_ID = result_dict.get("ID", None)
            SWMP_Name = result_dict.get("Name", None)
            SWMP_Level = result_dict.get("Level", None)
            SWMP_Version = result_dict.get("Version", None)
            SWMP_SourceFacility = result_dict.get("SourceFacility", None)
            SWMP_SourceWorkCenter = result_dict.get("SourceWorkCenter", None)
            SWMP_SourceDevice = result_dict.get("SourceDevice", None)
            SWMP_SourceTestProgram = result_dict.get("SourceTestProgram", None)
            SWMP_SourceProbes = result_dict.get("SourceProbes", None)
            SWMP_TargetFacility = result_dict.get("TargetFacility", None)
            SWMP_TargetWorkCenter = result_dict.get("TargetWorkCenter", None)
            SWMP_TargetDevice = result_dict.get("TargetDevice", None)
            SWMP_TargetTestProgram = result_dict.get("TargetTestProgram", None)
            SWMP_TargetProbes = result_dict.get("TargetProbes", None)
            SWMP_MergeFacility = result_dict.get("MergeFacility", None)
            SWMP_MergeWorkCenter = result_dict.get("MergeWorkCenter", None)
            SWMP_MergeDevice = result_dict.get("MergeDevice", None)
            SWMP_MergeTestProgram = result_dict.get("MergeTestProgram", None)
            SWMP_MergeProbes = result_dict.get("MergeProbes", None)
            SWMP_ProceedIfSWaferNotExist = result_dict.get("ProceedIfSWaferNotExist", None)
            SWMP_ProceedIFTWaferNotExist = result_dict.get("ProceedIFTWaferNotExist", None)
            SWMP_SWMDieTypeID = result_dict.get("SWMDieTypeID", None)
            SWMP_IgnoreTestTemperature = result_dict.get("IgnoreTestTemperature", None)
            SWMP_SourceDieTypes = result_dict.get("SourceDieTypes", None)
            SWMP_TargetDieTypes = result_dict.get("TargetDieTypes", None)
            SWMP_ParametricDataCopyID = result_dict.get("ParametricDataCopyID", None)

            context.user_details_from_db = swmpolicy_query_result_dict
            self.logger.info(
                f"Query SWM Policy executed successfully {SWMP_ID}, {SWMP_Name}, {SWMP_Level} , {SWMP_Version}, {SWMP_SourceFacility}, {SWMP_SourceWorkCenter}, {SWMP_SourceDevice}, "
                f"{SWMP_SourceTestProgram}, {SWMP_SourceProbes}, {SWMP_TargetFacility}, {SWMP_TargetWorkCenter}, {SWMP_TargetDevice}, {SWMP_TargetTestProgram}, {SWMP_TargetProbes}, "
                f"{SWMP_MergeFacility}, {SWMP_MergeWorkCenter}, {SWMP_MergeDevice}, {SWMP_MergeTestProgram}, {SWMP_MergeProbes}, {SWMP_ParametricDataCopyID}, {SWMP_ProceedIfSWaferNotExist},"
                f"{SWMP_ProceedIFTWaferNotExist}, {SWMP_SWMDieTypeID}, {SWMP_IgnoreTestTemperature}, {SWMP_SourceDieTypes}, {SWMP_TargetDieTypes}")

        except Exception as e:
            MyException.handle_exception(context, e)

    def dataSwmAutomatedPolicies(self, context):
        try:
            # Query to retrieve data from Automated Policies
            query_result = self.cursor.execute("SELECT * FROM SWMAutomatedPolicies AS sp").fetchone()
            self.logger.info("Query Result of SWM Automated Policies: %s", query_result)

            self.logger.info("Query SWM Automated Policy executed successfully")

            context.user_details_from_db = query_result

            # Convert the Row object to a dictionary
            if query_result:
                swm_policy_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(swm_policy_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Rules:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            SWMAutomate_ID = result_dict.get("SWMAutomateID", None)
            SWMAutomate_PolicyID = result_dict.get("PolicyID", None)
            SWMAutomate_Status = result_dict.get("StatusID", None)
            SWMAutomate_IsAutomated = result_dict.get("IsAutomated", None)

            context.user_details_from_db = query_result_dict
            self.logger.info(f" Query SWM Policy executed successfully {SWMAutomate_ID}, {SWMAutomate_PolicyID}, {SWMAutomate_Status}, {SWMAutomate_IsAutomated} ")

        except Exception as e:
            MyException.handle_exception(context, e)

    def dataLotTableVerification(self, context):

        try:
            # Query to fetch the Lot of Data from database
            query_result = self.cursor.execute("SELECT * FROM lot AS l ORDER BY 1 DESC").fetchone()
            self.logger.info("Query Result of lot table: %s", query_result)

            # Store the result in the context if needed
            context.user_details_from_db = query_result
            context.details_from_db = query_result

            # Convert the Row object to a dictionary
            if query_result:
                lot_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(lot_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Rules:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            Lot_Sequence_Primary = result_dict.get("Lot_Sequence", None)
            Lot_ID = result_dict.get("Lot_ID", None)
            Lot_Program_Name = result_dict.get("Program_Name", None)
            Lot_Work_Center = result_dict.get("Work_Center", None)
            Lot_Facility_ID = result_dict.get("Facility_ID", None)
            Lot_Sublot_ID = result_dict.get("Sublot_ID", None)
            Lot_Device_Name = result_dict.get("Part_Type", None)

            context.user_details_from_db = query_result_dict
            self.logger.info(f"Query Result of Lot Table is: {Lot_Sequence_Primary}, {Lot_ID}, {Lot_Program_Name}, {Lot_Work_Center}, {Lot_Facility_ID}, {Lot_Device_Name}, {Lot_Sublot_ID}")
        except Exception as e:
            MyException.handle_exception(context, e)

    def dataTestParamMapVerification(self, context):
        try:
            # Query to fetch the Data of Test Parameter Map from database
            query_result = self.cursor.execute("SELECT * FROM Test_Param_Map as tpm").fetchone()
            self.logger.info("Query Result of Test Param Map table: %s", query_result)

            # Store the result in the context if needed
            context.user_details_from_db = query_result
            self.logger.info("Query Test Param Map table has been executed successfully")

            # Convert the Row object to a dictionary
            if query_result:
                tpm_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(tpm_table_names))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of Test Param Map:\n%s", formatted_result)

            # Load the JSON String into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            TPM_Lot_Sequence = result_dict.get("Lot_Sequence", None)
            TPM_Test_Number = result_dict.get("Test_Number", None)
            TPM_Test_Name = result_dict.get("Test_Name", None)
            TPM_Column_Name = result_dict.get("Column_Name", None)
            TPM_Program_Name = result_dict.get("Program_Name", None)
            TPM_Table_Name = result_dict.get("Table_Name", None)

            context.user_details_from_db = query_result_dict
            self.logger.info(f"Query Result of Test Param Map is {TPM_Lot_Sequence}, {TPM_Test_Number}, {TPM_Test_Name}, {TPM_Column_Name}, {TPM_Program_Name}, {TPM_Table_Name}")

        except Exception as e:
            MyException.handle_exception(context, e)

    def dataSwmDashboardVerification(self, context):
        try:
            # Query to fetch the Lot Data from database
            swmdashboard_query_result = self.cursor.execute("SELECT * FROM swmDashboard AS sDashboard").fetchone()
            self.logger.info("Query Result of Swm Dashboard table: %s", swmdashboard_query_result)

            # Convert the Row Object to a dictionary
            if swmdashboard_query_result:
                swmdashboard_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(swmdashboard_table_names))
            else:
                query_result_dict = None

            # Store the result in the context if needed
            context.user_details_from_db = swmdashboard_query_result
            self.logger.info("Query Swm Dashboard table has been executed successfully")
        except Exception as e:
            MyException.handle_exception(context, e)

    def convert_datetimes_and_decimals(self, data):
        if isinstance(data, dict):
            return {key: self.convert_datetimes_and_decimals(value) for key, value in data.items()}
        elif isinstance(data, (list, tuple)):
            return [self.convert_datetimes_and_decimals(item) for item in data]
        elif isinstance(data, datetime):
            return str(data)
        elif isinstance(data, Decimal):
            return float(data)
        else:
            return data
