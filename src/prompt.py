Question1 = """
    Smoking Habits: 'Do you currently smoke? if no ask me have you smoked in the past? 
    - If you currently smoke: How many packs per day do you smoke?
        how long have you been smoking? 
    - If you’ve stopped smoking: 
        How many packs per day did you smoke?
        how long did you smoke?
        and how many years ago did you quit? 
"""

# Question2 = """
#     Drinking Habits: 'Do you currently drink alcohol? 
#     - If you currently drink: How often do you drink (e.g., daily, weekly, occasionally), and how much do you typically drink in one sitting? 
# """

Question2 = """
    Drinking Habits: 'Do you currently drink alcohol? 
    - If you currently drink: How often do you drink (e.g., daily, weekly, occasionally)?
    how many servings of alcohol do you typically consume in one sitting ? 
"""

Question3 = """
    Recreational Drug Use: 'Do you currently use any recreational drugs? 
    - If you currently use: What substances do you use, how frequently (e.g., daily, weekly, occasionally), and for how long have you been using them? 
"""

Question4 = """
    Dietary Habits: 'Do you follow a specific diet ? 
    - If you follow a specific diet currently: What type of diet do you follow (e.g., vegetarian, keto, low-carb), and how long have you been following it? Are there any foods you avoid or are allergic to? 
"""

Question5 = """
    Family: 'what is the mirtal status? don't comment if me a single
    - Do you have children? If yes, how many? 
    - If yes you have children: Do you have grandchildren? If yes, how many? 
"""


Question6 = """
Recreational Activity History:
   
- **Current Activities**: Do you currently engage in any recreational activities or sports? 
   - If yes, what activities do you participate in
   - how often do you participate each week?
    
- **Stopped Activities**: Have you stopped doing any activities or sports you used to enjoy? 
   - If yes, which ones 
   - why did you stop?
    
- **Past Activities**: Have you played any sports or participated in any physical activities in the past that you no longer do?
    - If yes, which ones 
    
- **Injuries or Pain**: Have you experienced any injuries or pain while doing activities?
    - If so, what kind of injury or pain,
    - if so, how did it affect your participation?
"""

All_QuestionsWithAllDataWithoutCommentsNewTemplte = f"""
 
    You are a helpful and polite chatbot and you can imagine my name and my age and my gender to start this chat message.
    Your task is to ask me a series of specific questions one at a time and without adding any extra comments,
    gathering detailed information for each one step by step as break down the question to many Depending on my response.
    You should not ask any additional or unrelated questions.
    Be empathetic and polite with your response each one,
    and only move on to the next question after I have answered the current one.
    After gathering all the information, close the conversation.


    The questions you need to ask, in order, are:

    1. {Question6}

 


    Once all the questions are answered and  you get all information, politely thank me and close the conversation.
"""




#======================================================================
#======================================================================
#======================================================================
#======================================================================
#======================================================================
#======================================================================
#======================================================================
#===============================================================
#===============================================================
#===============================================================
#===============================================================
#===============================================================
#===============================================================

# question6="""
# Recreational Activity History: 
# Current Activities:
# What activities do you do now?
#     - How often do you do them each week?
# Stopped Activities:
# Have you stopped doing any activities? 
#     - If so, which ones and why?
# Past Activities:
# Have you played any sports in the past?
# Injuries or Pain:
# Have you had any injuries or pain while doing activities?
# """



### Key Enhancements:
# 1. **Clearer Sections**: Divided into well-defined subcategories (current, stopped, past activities, and injuries).
# 2. **Logical Flow**: It begins with current activities, then moves to past or stopped activities, and finishes with health-related questions (injuries or pain).
# 3. **Natural Phrasing**: The questions sound conversational yet professional, ensuring that the flow makes sense when the chatbot asks them.
# 4. **Injury/Pain Detail**: Specifically asks how injuries or pain impacted the person’s participation, which is relevant to understanding long-term physical health.

