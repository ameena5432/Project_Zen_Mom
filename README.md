#### The problem to solve

Need to build a feature that helps Moms understand if and how their lifestyle is impacting pumped milk volume. We need to build a tool to find a factor that could contribute to milk volume and report the most influential factor for a given session.

#### Problem Background

Each time Mom finishes pumping to assess her current state/mood for that session she is given a survey in the app,
which asks them to rate multiple questions on a scale of 1 to 5.

Example questions -
- What is your stress level during this pump session?
- If you are tired from strenuous physical work, rate the level of tiredness?
- Rate your positive thoughts?

#### The solution

1) Using 3 CSV files i.e., Pumping_Session.CSV , Survey_Questions.CSV and Moms_Reponse.CSV
2) Creating a factor label based on response score for 3 questions given to Mom after each session with an option to rate on scale of 1 to 5
3) This factor label helps us to access the user experience of moms after each pumping session

#### Files included in the project:

##### Source Code :

1) Project_Zen_Mom.py 

###### Test Code:

1) test_project_zen_mom.py

###### CSV Files:

1. Scenario_1_Pumping_Session.csv
2. Scenario_1_Moms_Response.csv
3. Survey_Questions.csv
4. Scenario_2_Pumping_Session.csv
5. Scenario_2_Moms_Response.csv
6. Scenario_3_Pumping_Session.csv
7. Scenario_3_Moms_Response.csv
8. Scenario_4_Pumping_Session.csv
9. Scenario_4_Moms_Response.csv
10. Scenario_5_Pumping_Session.csv
11. Scenario_5_Moms_Response.csv


#### Pre-requistes to run the project :

Python 3 (install python3 and up on your machine)

Pandas   (If you do not have pandas then run command : pip3 install pandas in your command prompt)

#### Instructions to run the project

1) Go to terminal on mac or command-line interpreter in windows and navigate to the Project_Zen_Mom folder.
2) Run the following command to run the test cases :

      python3 -m unittest test_project_zen_mom.py
      
###### Expected Results : 

        ----------------------------------------------------------------------
        Ran 5 tests in 0.654s


### A summary presentation of the testing scenarios can be found below : 

###### Here we are testing for 5 scenarios :

  - Below are the list of Survey Questions provided to Moms after her pumping session to rate in every scenario discussed below:

      - ![image](https://user-images.githubusercontent.com/11728248/106683761-f7562c00-6579-11eb-88f6-a6916bc9ec14.png)
  
* Scenario 1: If there is just one greater precedence scale factor use only that

    - Below is the Mom's Response data captured after her pumping session for demonstrating Scenario 1 :

       ![image](https://user-images.githubusercontent.com/11728248/106683331-29b35980-6579-11eb-8ab9-99106e354c3f.png)

        ###### Expected Output : High Stress , Medium Fatigue ( If there is just one greater precedence scale factor use only that )

         ![image](https://user-images.githubusercontent.com/11728248/106683627-b8c07180-6579-11eb-80c0-29c8409d6f47.png)


* Scenario 2: If there are multiple labels of the same scale then use the first one in the list of questions

    - Below is the Mom's Response data captured after her pumping session for demonstrating Scenario 2 :

         ![image](https://user-images.githubusercontent.com/11728248/106684209-e2c66380-657a-11eb-8013-5c6672e05668.png)

      ###### Expected Output : Low Stress , Medium Stress ( If there are multiple labels of the same scale then use the first question)

         ![image](https://user-images.githubusercontent.com/11728248/106683120-c0334b00-6578-11eb-9c9b-498d31e39939.png)


* Scenario 3: If Mom does not answer a question from that session's survey

    - Below is the Mom's Response data captured after her pumping session for demonstrating Scenario 3:

         ![image](https://user-images.githubusercontent.com/11728248/106688867-ca0e7b80-6583-11eb-8dad-2cb983d9ca09.png)
  
     ###### Expected Output : Medium Stress , High Positivity ( If Mom does not answer a question from that session's survey ):

     Here I'm demonstrating following things :

     - 1) I have assumed that some characters like '?' , '&' have come as junk inputs in our data. I have converted them to NaN (Not a Number) and  
                 calculated the factor label

     - 2) I have cleansed the rows with NaN(Not a Number) from Moms_Response.csv and then calculated the factor label.

    - 3) Hence from the Moms_Response file , Survery Response Id : srv_res_1 , Mom_Id : mom_1 and Session_id :  session_1 has answered only 2 questions
            and out of the 2 questions answered, question 1 has highest score of 3 from that survey. Therefore we see "medium stress" as the most influencial 
            factor for this Mom's Session.

     ![image](https://user-images.githubusercontent.com/11728248/106689111-4acd7780-6584-11eb-9567-25fe29e17267.png)


* Scenario 4: If a Mom does not answer any question in the survey then we will not consider that session to calculate the factor label

    - Below is the Mom's Response data captured after her pumping session for demonstrating Scenario 4:

         ![image](https://user-images.githubusercontent.com/11728248/106689899-a2b8ae00-6585-11eb-86fb-0e486f083ad0.png)
  
        ###### Expected Output : high fatigue from Session 2 of Mom_1 and Session 1 is completely ignored because no questions were answered.
  
         ![image](https://user-images.githubusercontent.com/11728248/106690665-13ac9580-6587-11eb-98cd-226b6e8a473a.png)
  
* Scenario 5 : 

    - Below is the Mom's Response data captured after her pumping session for demonstrating Scenario 5:

         ![image](https://user-images.githubusercontent.com/11728248/106698419-9a686f00-6595-11eb-9b25-7e20d2ed8276.png)


        ###### Expected Output : high positivity , medium stress , high fatigue , high stress , high positivity , low stress

         ![image](https://user-images.githubusercontent.com/11728248/106698111-fe3e6800-6594-11eb-9509-ff61e75df312.png)

  
Future Enhancements :

   1) I would like to further enhance my code by following the enhnacement driven development practices and 
      make sure additional scenarios can be handled without any code changes
      
      For example : If in future we add more survey questions or decide to increase the options in the rating scale and so on.
      
TODO Comments :

   1) Adding unit test cases.
   2) Handling more edge cases
   3) Checking for a larger dataset
   4) Avoiding creating multiple dataframes when cleansed and insted save storage space.
   5) Tring to make the code faster with bigger dataset.
   
   
  
