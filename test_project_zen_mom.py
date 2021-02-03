import pandas as pd
import unittest
import Project_Zen_Mom

class TestZenMom(unittest.TestCase):

	# I have created 5 test cases for 5 different scenarios in this integration testing file
	
    def  test_scenario_1(self):
		
		#Creating the expected dataframe named df to compare in Scenario 1
		
        data = {'mom_id_x':['mom_1', 'mom_1'],
        'session_id':['session_1', 'session_2'],
        'Timestamp':['2020-11-19','2020-11-20'],
        'Milk_Volume':[2.0,4.0],
        'Question_text':['Rate your stress level','Rate your stress level'],
        'Accessed_factor':['stress_level','stress_level'],
        'response_Score':[4.0,1.0],
        'factor_label':['high stress','low stress']}

        df = pd.DataFrame(data,index=[0,1])
    
        
        path_pumping_Session= "Scenario_1_Pumping_Session.csv"
        path_survey_QUestions= "Survey_questions.csv"
        path_moms_reponse= "Scenario_1_Moms_Response.csv"
        pumping_session , survey_question , mom_response = Project_Zen_Mom.load_data(path_pumping_Session,path_survey_QUestions,path_moms_reponse)
        
        o=open("Test_Results_Scenraio_1.text","w")
        
        print("\n\n ***** ------- Running the test for Scenario 1: -------- ***** \n\n",file=o)
        
        print("This is the expected output for scenario 1 : \n",file=o)
        print(df,file=o)

		# Calling the function to cleanse the Pumping session data for junk inputs and NaN
		
        pumping_Session_CLEAN = Project_Zen_Mom.cleanse_Pumping_Session_data(pumping_session)
        
        print("\n\n This is the Pumping session data for scenario 1 : \n",file=o)
        print(pumping_Session_CLEAN,file=o)

		# Calling the function to cleanse the Moms Response data for junk inputs and NaN
		
        Moms_Response_CLEAN = Project_Zen_Mom.cleanse_Moms_Response_data(mom_response)
        
        print("\n\n This is the Moms Response data for scenario 1 : \n",file=o)
        print(Moms_Response_CLEAN,file=o)
        
        print("\n\n These are the Survey Questions : \n",file=o)
        print(survey_question,file=o)
        
        # Merging the three datasets Pumping Session , Moms Response and Survey Question

        query_answers = Project_Zen_Mom.merge_dataframes(pumping_Session_CLEAN , survey_question ,Moms_Response_CLEAN)
        
        # Calculating the factor label 
        		
        final_result = Project_Zen_Mom.factor_label_winner_Calculations(query_answers)
        print("\n\n This is the Final output : \n",file=o)
        print(final_result,file=o)
        
        # Comparing the final result dataframe with expected dataframe to test
        
        pd.testing.assert_frame_equal(final_result,df)
        
        
    def  test_scenario_2(self):
		
		#Creating the expected dataframe to compare in Scenario 2
		
        data = {'mom_id_x':['mom_1', 'mom_1'],
        'session_id':['session_1', 'session_2'],
        'Timestamp':['2020-11-19','2020-11-20'],
        'Milk_Volume':[2.0,4.0],
        'Question_text':['Rate your stress level','Rate your stress level'],
        'Accessed_factor':['stress_level','stress_level'],
        'response_Score':[1.0,3.0],
        'factor_label':['low stress','medium stress']}

        df = pd.DataFrame(data,index=[0,1])
        
        path_pumping_Session= "Scenario_2_Pumping_Session.csv"
        path_survey_QUestions= "Survey_questions.csv"
        path_moms_reponse= "Scenario_2_Moms_Response.csv"
        pumping_session , survey_question , mom_response = Project_Zen_Mom.load_data(path_pumping_Session,path_survey_QUestions,path_moms_reponse)
        
        o=open("Test_Results_Scenario_2.text","w")
        print("\n\n ***** ------- Running the test for scenario 2 : -------- ***** \n\n",file=o)
        
        print("This is the expected output for scenario 2 : \n",file=o)
        print(df,file=o)

		# Calling the function to cleanse the Pumping session data for junk inputs and NaN

        pumping_Session_CLEAN = Project_Zen_Mom.cleanse_Pumping_Session_data(pumping_session)
        
        print("\n\n This is the Pumping session data for scenario 2 : \n",file=o)
        print(pumping_Session_CLEAN,file=o)

		# Calling the function to cleanse the Moms Response data for junk inputs and NaN

        Moms_Response_CLEAN = Project_Zen_Mom.cleanse_Moms_Response_data(mom_response)

        print("\n\n This is the Moms Response data for scenario 2 : \n",file=o)
        print(Moms_Response_CLEAN,file=o)
        
        print("\n\n These are the Survey Questions : \n",file=o)
        print(survey_question,file=o)
  
        # Merging the three datasets Pumping Session , Moms Response and Survey Question
              
        query_answers = Project_Zen_Mom.merge_dataframes(pumping_Session_CLEAN , survey_question ,Moms_Response_CLEAN)

		# Calculating the factor label
		
        final_result = Project_Zen_Mom.factor_label_winner_Calculations(query_answers)

        print("\n\n This is the Final output for Scenario 2: \n",file=o)
        print(final_result,file=o)
		
		# Comparing the final result dataframe with expected dataframe to test
		
        pd.testing.assert_frame_equal(final_result,df)
        
        
        
    def  test_scenario_3(self):
		
		#Creating the expected dataframe to compare in Scenario 3
		
        data = {'mom_id_x':['mom_1', 'mom_1'],
        'session_id':['session_1', 'session_2'],
        'Timestamp':['2020-11-19','2020-11-20'],
        'Milk_Volume':[2.0,4.0],
        'Question_text':['Rate your stress level','Rate your level of positive thoughts'],
        'Accessed_factor':['stress_level','positivity_level'],
        'response_Score':[3.0,5.0],
        'factor_label':['medium stress','high positivity']}

        df = pd.DataFrame(data,index=[0,3])
        
        path_pumping_Session= "Scenario_3_Pumping_Session.csv"
        path_survey_QUestions= "Survey_questions.csv"
        path_moms_reponse= "Scenario_3_Moms_Response.csv"
        pumping_session , survey_question , mom_response = Project_Zen_Mom.load_data(path_pumping_Session,path_survey_QUestions,path_moms_reponse)

        o=open("Test_Results_Scenario_3.text","w")
        print("\n\n ***** ------- Running the test for scenario 3 : -------- ***** \n\n",file=o)
        
        print("This is the expected output for scenario 3 : \n",file=o)
        print(df,file=o)
        
        # Calling the function to cleanse the Pumping Session data for junk inputs and NaN
        
        pumping_Session_CLEAN = Project_Zen_Mom.cleanse_Pumping_Session_data(pumping_session)

        print("\n\n This is the Pumping session data for scenario 3 : \n",file=o)
        print(pumping_Session_CLEAN,file=o)

		# Calling the function to cleanse the Moms Response data for junk inputs and NaN
		
        Moms_Response_CLEAN = Project_Zen_Mom.cleanse_Moms_Response_data(mom_response)

        print("\n\n This is the Moms Response data for scenario 3 : \n",file=o)
        print(Moms_Response_CLEAN,file=o)
        
        print("\n\n These are the Survey Questions : \n",file=o)
        print(survey_question,file=o)
        
        # Merging the three datasets Pumping Session , Moms Response and Survey Question
        
        query_answers = Project_Zen_Mom.merge_dataframes(pumping_Session_CLEAN , survey_question ,Moms_Response_CLEAN)

		#Calculating the factor label
		
        final_result = Project_Zen_Mom.factor_label_winner_Calculations(query_answers)

        print("\n\n This is the Final output for Scenario 3: \n",file=o)
        print(final_result,file=o)
        
        # Comparing the final result dataframe with expected dataframe to test
        
        pd.testing.assert_frame_equal(final_result,df)
        
        
    def  test_scenario_4(self):
		
		#Creating the expected dataframe to compare in Scenario 4
		
        data = {'mom_id_x':['mom_1'],
        'session_id':['session_2'],
        'Timestamp':['2020-11-20'],
        'Milk_Volume':[4.0],
        'Question_text':['Rate your level of tiredness'],
        'Accessed_factor':['fatigue_level'],
        'response_Score':[5.0],
        'factor_label':['high fatigue']}

        df = pd.DataFrame(data,index=[1])
        
        path_pumping_Session= "Scenario_4_Pumping_Session.csv"
        path_survey_QUestions= "Survey_questions.csv"
        path_moms_reponse= "Scenario_4_Moms_Response.csv"
        pumping_session , survey_question , mom_response = Project_Zen_Mom.load_data(path_pumping_Session,path_survey_QUestions,path_moms_reponse)


        o=open("Test_Results_Scenario_4.text","w")
        print("\n\n ***** ------- Running the test for scenario 4 : -------- ***** \n\n",file=o)
        
        print("This is the expected output for scenario 4 : \n",file=o)
        print(df,file=o)
        
		# Calling the function to cleanse the Pumping session data for junk inputs and NaN
		
        pumping_Session_CLEAN = Project_Zen_Mom.cleanse_Pumping_Session_data(pumping_session)
        
        print("\n\n This is the Pumping session data for scenario 4 : \n",file=o)
        print(pumping_Session_CLEAN,file=o)

		# Calling the function to cleanse the Moms Response data for junk inputs and NaN
		
        Moms_Response_CLEAN = Project_Zen_Mom.cleanse_Moms_Response_data(mom_response)
        
        print("\n\n This is the Moms Response data for scenario 4 : \n",file=o)
        print(Moms_Response_CLEAN,file=o)
        
        print("\n\n These are the Survey Questions : \n",file=o)
        print(survey_question,file=o)

		# Merging the three datasets Pumping Session , Moms Response and Survey Question
		
        query_answers = Project_Zen_Mom.merge_dataframes(pumping_Session_CLEAN , survey_question ,Moms_Response_CLEAN)

		# Calculating the factor label
		
        final_result = Project_Zen_Mom.factor_label_winner_Calculations(query_answers)
        
        print("\n\n This is the Final output for Scenario 4 where mom_1 for session_1 does not answer any questions and answers for session_2 only.",file=o)
        print("\n Hence we get one row output for session_2 only : \n",file=o)
        print(final_result,file=o)

		# Comparing the final result dataframe with expected dataframe to test
		
        pd.testing.assert_frame_equal(final_result,df)
        
        
    def  test_scenario_5(self):
		
		#Creating the expected dataframe to compare in Scenario 5
		
        data = {'mom_id_x':['mom_1','mom_2','mom_2','mom_2','mom_3','mom_4'],
        'session_id':['session_1','session_5','session_6','session_7','session_8','session_9'],
        'Timestamp':['2020-11-19','2020-11-22','2020-11-22','2020-11-22','2020-11-22','2020-11-22'],
        'Milk_Volume':[2.0,3.0,4.0,2.0,4.0,2.0],
        'Question_text':['Rate your level of positive thoughts','Rate your stress level','Rate your level of tiredness','Rate your stress level','Rate your level of positive thoughts','Rate your stress level'],
        'Accessed_factor':['positivity_level','stress_level','fatigue_level','stress_level','positivity_level','stress_level'],
        'response_Score':[4.0,3.0,5.0,5.0,5.0,1.0],
        'factor_label':['high positivity','medium stress','high fatigue','high stress','high positivity','low stress']}

        df = pd.DataFrame(data,index=[12,1,8,3,16,5])
        
        path_pumping_Session= "Scenario_5_Pumping_Session.csv"
        path_survey_QUestions= "Survey_questions.csv"
        path_moms_reponse= "Scenario_5_Moms_Response.csv"
        pumping_session , survey_question , mom_response = Project_Zen_Mom.load_data(path_pumping_Session,path_survey_QUestions,path_moms_reponse)

        o=open("Test_Results_Scenario_5.text","w")
        print("\n\n ***** ------- Running the test for scenario 5 : -------- ***** \n\n",file=o)
        
        print("This is the expected output for scenario 5 : \n",file=o)
        print(df,file=o)
        
        # Calling the function to cleanse the Pumping session data for junk inputs and NaN
        
        pumping_Session_CLEAN = Project_Zen_Mom.cleanse_Pumping_Session_data(pumping_session)
        
        print("\n\n This is the Pumping session data for scenario 5 : \n",file=o)
        print(pumping_Session_CLEAN,file=o)

		# Calling the function to cleanse the Moms Response data for junk inputs and NaN
		
        Moms_Response_CLEAN = Project_Zen_Mom.cleanse_Moms_Response_data(mom_response)

        print("\n\n This is the Moms Response data for scenario 5 : \n",file=o)
        print(Moms_Response_CLEAN,file=o)
        
        print("\n\n These are the Survey Questions : \n",file=o)
        print(survey_question,file=o)
        
        # Merging the three datasets Pumping Session , Moms Response and Survey Question
        
        query_answers = Project_Zen_Mom.merge_dataframes(pumping_Session_CLEAN , survey_question ,Moms_Response_CLEAN)

		# Calculating the factor label
		
        final_result = Project_Zen_Mom.factor_label_winner_Calculations(query_answers)

        print("\n\n This is the Final output for Scenario 5: \n",file=o)
        print(final_result,file=o)

		# Comparing the final result dataframe with expected dataframe to test
		
        pd.testing.assert_frame_equal(final_result,df)

    		
    

			       

