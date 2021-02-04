import pandas as pd
import unittest
import Project_Zen_Mom


class TestZenMom(unittest.TestCase):
    # I have created 5 test cases for 5 different scenarios in this integration testing file. More info about each scenario is in Readme.md

    def test_scenario_1(self):
        # Creating the expected dataframe named expectedOutputDF to compare in Scenario 1

        expectedOutputData = {'mom_id_x': ['mom_1', 'mom_1'],
                              'session_id': ['session_1', 'session_2'],
                              'Timestamp': ['2020-11-19', '2020-11-20'],
                              'Milk_Volume': [2.0, 4.0],
                              'Question_text': ['Rate your stress level', 'Rate your stress level'],
                              'Accessed_factor': ['stress_level', 'stress_level'],
                              'response_Score': [4.0, 1.0],
                              'factor_label': ['high stress', 'low stress']}

        expectedOutputDF = pd.DataFrame(expectedOutputData, index=[0, 1])

        pumpingSessionFile = "Scenario_1_Pumping_Session.csv"
        surveyQuestionsFile = "Survey_questions.csv"
        momsReponseFile = "Scenario_1_Moms_Response.csv"

        pumpingSessionDF, surveyQuestionsDF, momsResponseDF = Project_Zen_Mom.load_data(pumpingSessionFile,
                                                                                        surveyQuestionsFile,
                                                                                        momsReponseFile)

        outputFile = open("Test_Results_Scenario_1.text", "w")

        print("\n\n ***** ------- Running the test for Scenario 1: -------- ***** \n\n", file=outputFile)

        print("This is the expected output for scenario 1 : \n", file=outputFile)
        print(expectedOutputDF, file=outputFile)

        # Calling the function to cleanse the Pumping session data for junk inputs and NaN

        pumpingSessionCleanDF = Project_Zen_Mom.cleanse_Pumping_Session_data(pumpingSessionDF)

        print("\n\n This is the Pumping session data for scenario 1 : \n", file=outputFile)
        print(pumpingSessionCleanDF, file=outputFile)

        # Calling the function to cleanse the Moms Response data for junk inputs and NaN

        momsResponseCleanDF = Project_Zen_Mom.cleanse_Moms_Response_data(momsResponseDF)

        print("\n\n This is the Moms Response data for scenario 1 : \n", file=outputFile)
        print(momsResponseCleanDF, file=outputFile)

        print("\n\n These are the Survey Questions : \n", file=outputFile)
        print(surveyQuestionsDF, file=outputFile)

        # Merging the three datasets Pumping Session , Moms Response and Survey Question

        mergedDF = Project_Zen_Mom.merge_dataframes(pumpingSessionCleanDF, surveyQuestionsDF, momsResponseCleanDF)

        # Calculating the factor label 

        finalResultDF = Project_Zen_Mom.factor_label_winner_Calculations(mergedDF)

        print("\n\n This is the Final output : \n", file=outputFile)
        print(finalResultDF, file=outputFile)

        # Comparing the final result dataframe with expected dataframe to test

        pd.testing.assert_frame_equal(finalResultDF, expectedOutputDF)

    def test_scenario_2(self):
        # Creating the expected dataframe to compare in Scenario 2

        expectedOutputData = {'mom_id_x': ['mom_1', 'mom_1'],
                              'session_id': ['session_1', 'session_2'],
                              'Timestamp': ['2020-11-19', '2020-11-20'],
                              'Milk_Volume': [2.0, 4.0],
                              'Question_text': ['Rate your stress level', 'Rate your stress level'],
                              'Accessed_factor': ['stress_level', 'stress_level'],
                              'response_Score': [1.0, 3.0],
                              'factor_label': ['low stress', 'medium stress']}

        expectedOutputDF = pd.DataFrame(expectedOutputData, index=[0, 1])

        pumpingSessionFile = "Scenario_2_Pumping_Session.csv"
        surveyQuestionsFile = "Survey_questions.csv"
        momsReponseFile = "Scenario_2_Moms_Response.csv"

        pumpingSessionDF, surveyQuestionsDF, momsResponseDF = Project_Zen_Mom.load_data(pumpingSessionFile,
                                                                                        surveyQuestionsFile,
                                                                                        momsReponseFile)

        outputFile = open("Test_Results_Scenario_2.text", "w")
        print("\n\n ***** ------- Running the test for scenario 2 : -------- ***** \n\n", file=outputFile)

        print("This is the expected output for scenario 2 : \n", file=outputFile)
        print(expectedOutputDF, file=outputFile)

        # Calling the function to cleanse the Pumping session data for junk inputs and NaN

        pumpingSessionCleanDF = Project_Zen_Mom.cleanse_Pumping_Session_data(pumpingSessionDF)

        print("\n\n This is the Pumping session data for scenario 2 : \n", file=outputFile)
        print(pumpingSessionCleanDF, file=outputFile)

        # Calling the function to cleanse the Moms Response data for junk inputs and NaN

        momsResponseCleanDF = Project_Zen_Mom.cleanse_Moms_Response_data(momsResponseDF)

        print("\n\n This is the Moms Response data for scenario 2 : \n", file=outputFile)
        print(momsResponseCleanDF, file=outputFile)

        print("\n\n These are the Survey Questions : \n", file=outputFile)
        print(surveyQuestionsDF, file=outputFile)

        # Merging the three datasets Pumping Session , Moms Response and Survey Question

        mergedDF = Project_Zen_Mom.merge_dataframes(pumpingSessionCleanDF, surveyQuestionsDF, momsResponseCleanDF)

        # Calculating the factor label

        finalResultDF = Project_Zen_Mom.factor_label_winner_Calculations(mergedDF)

        print("\n\n This is the Final output for Scenario 2: \n", file=outputFile)
        print(finalResultDF, file=outputFile)

        # Comparing the final result dataframe with expected dataframe to test

        pd.testing.assert_frame_equal(finalResultDF, expectedOutputDF)

    def test_scenario_3(self):
        # Creating the expected dataframe to compare in Scenario 3

        expectedOutputData = {'mom_id_x': ['mom_1', 'mom_1'],
                              'session_id': ['session_1', 'session_2'],
                              'Timestamp': ['2020-11-19', '2020-11-20'],
                              'Milk_Volume': [2.0, 4.0],
                              'Question_text': ['Rate your stress level', 'Rate your level of positive thoughts'],
                              'Accessed_factor': ['stress_level', 'positivity_level'],
                              'response_Score': [3.0, 5.0],
                              'factor_label': ['medium stress', 'high positivity']}

        expectedOutputDF = pd.DataFrame(expectedOutputData, index=[0, 3])

        pumpingSessionFile = "Scenario_3_Pumping_Session.csv"
        surveyQuestionsFile = "Survey_questions.csv"
        momsReponseFile = "Scenario_3_Moms_Response.csv"

        pumpingSessionDF, surveyQuestionsDF, momsResponseDF = Project_Zen_Mom.load_data(pumpingSessionFile,
                                                                                        surveyQuestionsFile,
                                                                                        momsReponseFile)

        outputFile = open("Test_Results_Scenario_3.text", "w")
        print("\n\n ***** ------- Running the test for scenario 3 : -------- ***** \n\n", file=outputFile)

        print("This is the expected output for Scenario 3 : \n", file=outputFile)
        print(expectedOutputDF, file=outputFile)

        # Calling the function to cleanse the Pumping Session data for junk inputs and NaN

        pumpingSessionCleanDF = Project_Zen_Mom.cleanse_Pumping_Session_data(pumpingSessionDF)

        print("\n\n This is the Pumping session data for scenario 3 : \n", file=outputFile)
        print(pumpingSessionCleanDF, file=outputFile)

        # Calling the function to cleanse the Moms Response data for junk inputs and NaN

        momsResponseCleanDF = Project_Zen_Mom.cleanse_Moms_Response_data(momsResponseDF)

        print("\n\n This is the Moms Response data for scenario 3 : \n", file=outputFile)
        print(momsResponseCleanDF, file=outputFile)

        print("\n\n These are the Survey Questions : \n", file=outputFile)
        print(surveyQuestionsDF, file=outputFile)

        # Merging the three datasets Pumping Session , Moms Response and Survey Question

        mergedDF = Project_Zen_Mom.merge_dataframes(pumpingSessionCleanDF, surveyQuestionsDF, momsResponseCleanDF)

        # Calculating the factor label

        finalResultDF = Project_Zen_Mom.factor_label_winner_Calculations(mergedDF)

        print("\n\n This is the Final output for Scenario 3: \n", file=outputFile)
        print(finalResultDF, file=outputFile)

        # Comparing the final result dataframe with expected dataframe to test

        pd.testing.assert_frame_equal(finalResultDF, expectedOutputDF)

    def test_scenario_4(self):
        # Creating the expected dataframe to compare in Scenario 4

        expectedOutputData = {'mom_id_x': ['mom_1'],
                              'session_id': ['session_2'],
                              'Timestamp': ['2020-11-20'],
                              'Milk_Volume': [4.0],
                              'Question_text': ['Rate your level of tiredness'],
                              'Accessed_factor': ['fatigue_level'],
                              'response_Score': [5.0],
                              'factor_label': ['high fatigue']}

        expectedOutputDF = pd.DataFrame(expectedOutputData, index=[1])

        pumpingSessionFile = "Scenario_4_Pumping_Session.csv"
        surveyQuestionsFile = "Survey_questions.csv"
        momsReponseFile = "Scenario_4_Moms_Response.csv"

        pumpingSessionDF, surveyQuestionsDF, momsResponseDF = Project_Zen_Mom.load_data(pumpingSessionFile,
                                                                                        surveyQuestionsFile,
                                                                                        momsReponseFile)

        outputFile = open("Test_Results_Scenario_4.text", "w")
        print("\n\n ***** ------- Running the test for scenario 4 : -------- ***** \n\n", file=outputFile)

        print("This is the expected output for Scenario 4 : \n", file=outputFile)
        print(expectedOutputDF, file=outputFile)

        # Calling the function to cleanse the Pumping session data for junk inputs and NaN

        pumpingSessionCleanDF = Project_Zen_Mom.cleanse_Pumping_Session_data(pumpingSessionDF)

        print("\n\n This is the Pumping session data for scenario 4 : \n", file=outputFile)
        print(pumpingSessionCleanDF, file=outputFile)

        # Calling the function to cleanse the Moms Response data for junk inputs and NaN

        momsResponseCleanDF = Project_Zen_Mom.cleanse_Moms_Response_data(momsResponseDF)

        print("\n\n This is the Moms Response data for scenario 4 : \n", file=outputFile)
        print(momsResponseCleanDF, file=outputFile)

        print("\n\n These are the Survey Questions : \n", file=outputFile)
        print(surveyQuestionsDF, file=outputFile)

        # Merging the three datasets Pumping Session , Moms Response and Survey Question

        mergedDF = Project_Zen_Mom.merge_dataframes(pumpingSessionCleanDF, surveyQuestionsDF, momsResponseCleanDF)

        # Calculating the factor label

        finalResultDF = Project_Zen_Mom.factor_label_winner_Calculations(mergedDF)

        print(
            "\n\n This is the Final output for Scenario 4 where mom_1 for session_1 does not answer any questions and answers for session_2 only.",
            file=outputFile)
        print("\n Hence we get one row output for session_2 only : \n", file=outputFile)
        print(finalResultDF, file=outputFile)

        # Comparing the final result dataframe with expected dataframe to test

        pd.testing.assert_frame_equal(finalResultDF, expectedOutputDF)

    def test_scenario_5(self):
        # Creating the expected dataframe to compare in Scenario 5

        expectedOutputData = {'mom_id_x': ['mom_1', 'mom_2', 'mom_2', 'mom_2', 'mom_3', 'mom_4'],
                              'session_id': ['session_1', 'session_5', 'session_6', 'session_7', 'session_8',
                                             'session_9'],
                              'Timestamp': ['2020-11-19', '2020-11-22', '2020-11-22', '2020-11-22', '2020-11-22',
                                            '2020-11-22'],
                              'Milk_Volume': [2.0, 3.0, 4.0, 2.0, 4.0, 2.0],
                              'Question_text': ['Rate your level of positive thoughts', 'Rate your stress level',
                                                'Rate your level of tiredness', 'Rate your stress level',
                                                'Rate your level of positive thoughts', 'Rate your stress level'],
                              'Accessed_factor': ['positivity_level', 'stress_level', 'fatigue_level', 'stress_level',
                                                  'positivity_level', 'stress_level'],
                              'response_Score': [4.0, 3.0, 5.0, 5.0, 5.0, 1.0],
                              'factor_label': ['high positivity', 'medium stress', 'high fatigue', 'high stress',
                                               'high positivity', 'low stress']}

        expectedOutputDF = pd.DataFrame(expectedOutputData, index=[12, 1, 8, 3, 16, 5])

        pumpingSessionFile = "Scenario_5_Pumping_Session.csv"
        surveyQuestionsFile = "Survey_questions.csv"
        momsReponseFile = "Scenario_5_Moms_Response.csv"
        pumpingSessionDF, surveyQuestionsDF, momsResponseDF = Project_Zen_Mom.load_data(pumpingSessionFile,
                                                                                        surveyQuestionsFile,
                                                                                        momsReponseFile)

        outputFile = open("Test_Results_Scenario_5.text", "w")
        print("\n\n ***** ------- Running the test for Scenario 5 : -------- ***** \n\n", file=outputFile)

        print("This is the expected output for scenario 5 : \n", file=outputFile)
        print(expectedOutputDF, file=outputFile)

        # Calling the function to cleanse the Pumping session data for junk inputs and NaN

        pumpingSessionCleanDF = Project_Zen_Mom.cleanse_Pumping_Session_data(pumpingSessionDF)

        print("\n\n This is the Pumping session data for scenario 5 : \n", file=outputFile)
        print(pumpingSessionCleanDF, file=outputFile)

        # Calling the function to cleanse the Moms Response data for junk inputs and NaN

        momsResponseCleanDF = Project_Zen_Mom.cleanse_Moms_Response_data(momsResponseDF)

        print("\n\n This is the Moms Response data for scenario 5 : \n", file=outputFile)
        print(momsResponseCleanDF, file=outputFile)

        print("\n\n These are the Survey Questions : \n", file=outputFile)
        print(surveyQuestionsDF, file=outputFile)

        # Merging the three datasets Pumping Session , Moms Response and Survey Question

        mergedDF = Project_Zen_Mom.merge_dataframes(pumpingSessionCleanDF, surveyQuestionsDF, momsResponseCleanDF)

        # Calculating the factor label

        finalResultDF = Project_Zen_Mom.factor_label_winner_Calculations(mergedDF)

        print("\n\n This is the Final output for Scenario 5: \n", file=outputFile)
        print(finalResultDF, file=outputFile)

        # Comparing the final result dataframe with expected dataframe to test

        pd.testing.assert_frame_equal(finalResultDF, expectedOutputDF)
