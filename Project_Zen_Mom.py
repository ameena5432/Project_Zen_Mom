import pandas as pd
import numpy as np


#Reads 3 csv files into dataframes: 
# Pumping_Session 
# Survey_Question
# Moms_Reponse 
def load_data(pumping_session, survey_question, mom_response):
	pumpingSessionDF = pd.read_csv(pumping_session)
	surveyQuestionsDF = pd.read_csv(survey_question)
	surveyQuestionsDF.dropna(how='all',inplace=True) #data cleansing
	momsResponseDF = pd.read_csv(mom_response)

	return pumpingSessionDF, surveyQuestionsDF , momsResponseDF


# This function cleanses the pumping session data by removing rows with junk characters and NaN
# We should clean the junk values after validating the data. 

def cleanse_Pumping_Session_data(pumpingSessionDF):
	nonNullDF = pumpingSessionDF.dropna(axis=0, how="any", thresh=None, subset=None, inplace=False)
	pumping_Session_CLEAN = nonNullDF[nonNullDF.mom_id.str.startswith("mom_")]
	cleansedDF = pumping_Session_CLEAN[pumping_Session_CLEAN.session_id.str.startswith("session_")]
	return cleansedDF


# This function cleanses the moms response data by removing rows with junk characters and NaN
# We should clean the junk values after validating the data. 

def cleanse_Moms_Response_data(momsResponseDF):


	momsResponseDF.dropna(subset=["survey_response_id","mom_id","session_id","question_id","response_Score"],inplace=True)
	momCleansedDF = momsResponseDF[momsResponseDF.mom_id.str.startswith("mom_")]
	sessionCleansedDF = momCleansedDF[momCleansedDF.session_id.str.startswith("session_")]
	return sessionCleansedDF

# This function merges the 3 cleansed dataframes into 1 dataframe called query_answers
def merge_dataframes(pumpingSessionDF, surveyQuestionsDF, momsResponseDF):

	pumpingResponse = pd.merge(pumpingSessionDF, momsResponseDF, left_on=['session_id'],right_on=['session_id'])
	pumpingResponseSurvey = pd.merge(pumpingResponse, surveyQuestionsDF, left_on='question_id',right_on='Question_id')
	queryAnswers = pumpingResponseSurvey[['mom_id_x','session_id','Timestamp','Milk_Volume','Question_text','Accessed_factor','response_Score']]
	return queryAnswers

# In this function we will be calculating the factor_label using query_answers dataframe
# First we group by session_id and then find max of response_Score in each of those groups

def factor_label_winner_Calculations(queryAnswers):
	
	grouped = queryAnswers.loc[queryAnswers.groupby('session_id')['response_Score'].idxmax(),:]

	# we then set the conditions to create the factor label
	
	conditions = [
	(grouped['response_Score'] > 0.0) & (grouped['response_Score'] < 3.0),
	(grouped['response_Score'] > 2.0) & (grouped['response_Score'] < 4.0),
	(grouped['response_Score'] > 3.0)
	]

	#These will be the values of the factor_label when the above conditions are met respectively
	# We are splitting the Accessed_factor attribute on '_' and picking first word
	# Then we concat the word from accessed factor with severity ( low , medium , high)
	
	# Ex : If Accessed Factor = Fatigue_level then we pick "Fatigue" and concat with low if it's response score is 2
	
	values = ['low '+grouped['Accessed_factor'].str.split('_',expand=True)[0], 'medium '+grouped['Accessed_factor'].str.split('_',expand=True)[0],'high '+grouped['Accessed_factor'].str.split('_',expand=True)[0]]

	# We use numpy to map the conditions and values using select function
	grouped['factor_label'] = np.select(conditions, values)

	return grouped
