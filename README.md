# Cyber-Activity-Risk-Analyzer
**Scenario**
The university IT department is analyzing student login activity patterns to detect
suspicious behavior. Each login session generates a list of activity intensity scores (integer
values). Your task is to design a Cyber Activity Risk Analyzer that:
1. Cleans the data
2. Categorizes risk levels
3. Applies a personalized security filter
4. Generates a final security report


**Problem Statement**
Write a Python program that:
1. Accepts a list of integer activity scores
2. Uses a for loop to process each score
3. Builds separate lists based on risk category
4. Applies personalized filtering logic
5. Displays a final risk summary


**Methodology:**
Firstly, I have taken the integer variable and assigned it with my last 3 digits of my registration number. I have taken a list (scores) to initially get the activity intensity scores from the user. Initialized four empty lists namely low_risk, medium_risk, high_risk and critical_risk. I have initialized four integer variables to zero namely low, critical, valid and ignored. Using a for loop I have concatenated the scores to their respective lists using the given conditions. Coming to the personalized logic, I have used conditional statements to deal with that. If the last digit of my registration number is a odd, I removed the elements from critical_list, otherwise I will remove elements from the low_risk.
Finally, I displayed the number of valid, ignored scores and number of scores deleted due to personalization.
The personalization depends on the last digit of my registration number. And it is 9 which is odd. The logic I used here is if (Register_number%10)%2!=0, then I emptied critical_risk list. If the above condition fails then I have emptied low_risk list.
•	Last digit of Register Number = 9
•	Hence, I applied the above mentioned logic.


**Sample Output:**
[12,-15, 18, 69, 123, 79, 45]
Last digit of Registration Number: 9 

-15 is Invalid score.
Low Risk: [12, 18]
Medium Risk: [45]
High Risk: [69, 79]
Critical Risk: [123] 

After Personalized Filtering:
Low Risk: [12, 18]
Medium Risk: [45]
High Risk: [69, 79]
Critical Risk: [] 

Total Valid Entries: 6
Ignored Entries: 1
Removed due to Personalization: 1



