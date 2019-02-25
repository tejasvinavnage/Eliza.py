#eliza.py
#Developed by:
#    Tejasvi Navnage
#    Hui Zheng
#    Rahul Kulkarni
#    Team Tuesday    
#    AIT 690 - NLP Natural Language Processing
#
#
#Steps
#Step 1:
#    Introduction and asking for user name
#Step 2:
#    Check for continuation of conversation
#Step 3:
#    Create continue_conversation function to handle the continuation of converastion
#Step 4:
#    Transformation of sentence from reflexive pronouns and words
#Step 5:
#    Checking if the response is present in the corpus qadict and selecting valid response
#------------------------------------------------------------------------
import random
import re

#Welcome message
print("="*75)
print("Hi this is Eliza, your therapist for the day")
print("="*75)
print("What is your name?")
name = input('~')

#Step 1
#validating if the username is in characters
if(re.search('[A-Z]|[a-z]+', name)):
    print("Hi, "+name+". How may I help you today?")
    
else:
    print(name+"! Is that a real name. Can you enter the real name?")
    name = input('>')
    
response = ''

#list to check for exit words
exit_words = ['bye', 'goodbye', 'exit', 'tata', 'Goodbye', 'Bye', 'Exit']

#dictionary Q & A,
#key: regular expression
#value: List of possible replies from Eliza
#Conversion used
#We decided on dividing the topic for conversation in following categories based on 
#estimating what would be the common topic for conversation
#Generic topic:
#Verbs: want, need, like, love, hurt, depress, tired
#Feelings: I'm, I am, I am feeling, I feel, I would, I will, I would like, I am going to, I gonna, I am gonna, I think 
#Family: mother, father, child, brother, sister
#School: 
#Friend:
#Homework:
#Computer: 
#technology:
#car, dog
#Food:
#Probabilities and questions: 
  
qadict = {
            "(.*)":
         ["Please tell me more.",
        "Can you elaborate on that?",
        "Why do you say that %1?",
        "I see.",
        "Very interesting.",
        "I see. And what does that tell you?",
        "How does that make you feel?"],
          
    "I want (.*)":
        ["Why do you want %1?",
        "What will do after you finish %1?"],
    
    "I need (.*)":
        ["Why do you need %1?",
          "Could you tell me the reason why you need %1?",
          "Are you sure that you need %1?"],
      
    "I would like (.*)":
        ["Why would you like %1?",
        "Could tell me the reason why you would like %1?",
        "When would you like %1?",
        "Where would you like %1?"],
       
    "I love(.*)":
        ["Why do you love %1?",
        "Tell me more about your love",
        "Does it make you happy to be in love with %1?"],
     
    "I hate(.*)":
        ["Why do you hate %1?",
         "Why do you have so much hatered towards %1?",
         "Hatered causes only anger, hope you stop hating %1."],
    
    "I am (.*)":
        ["Why are you %1?",
        "How %1 are you?",
        "How do you feel about being %1?"],
    
    "I'm (.*)":
        ["Why are you %1?",
        "How %1 are you?",
        "How do you feel about being %1?"],
     
    "I am feeling(.*)":
        ["Why are you feeling %1?",
        "What made you feel %1?",
        "Are you still feeling %1?",
        "Do you feel the same always?",
        "How are you felling now?"],
     
    "I feel(.*)":
        ["Why are you feeling %1?",
        "What made you feel %1?",
        "Are you still feeling %1?",
        "Do you feel the same always?",
        "How are you felling now?"],
    
    "(.*) hurt (.*)":
        ["What is hurting you?",
        "Can you talk about it?",
        ],
     
    "I'm hurting(.*)":
        ["What is hurting you?",
        "Can you talk about it?",
        ],
    
    "(.*) depressed (.*)":
        ["What is the cause of your depression?",
        "How long have you been in depression?",
        ],
    
     
    "I think (.*)":
        ["Why do you think %1?",
        "Could you tell me the reason why you think %1?",
        "Are sure that %1?",
        "Do you really think so?" ],
     
    "I would (.*)":
          [ "Why would you %1?",
        "When would you %1?",
        "Could please tell more details about how would you %1?"],
    
    "I will (.*)":
          [ "Why will you %1?",
        "When will you %1?",
        "Could please tell more details about how will you %1?"],
    
    "I am going to (.*)":
        ["Why are you going to %1?",
        "When are you going to%1?",
        "By what means, you  are going to %1?"],
    
    "I gonna (.*)":
        [ "Why are you gonna %1?",
        "When are you gonna%1?",
        "How are you gonna %1?"],
     
     "I'm gonna (.*)":
        [ "Why are you gonna %1?",
        "When are you gonna%1?",
        "How are you gonna %1?"],
    
    "I am tired(.*)":
        ["What is tirying you?",
        "Are you always tired?",
        "What do you do to relieve stress?"], 
    
    "Because (.*)":
          [  "Is that the real reason?",
        "What other reasons come to mind?",
        "Does that reason apply to anything else?",
        "If %1, what else must be true?"],
    
    "What (.*)":
        ["Why do you ask?",
        "How would an answer to that help you?",
        "What do you think?"],
     
     "How (.*)":
          ["How do you suppose?",
        "Perhaps you can answer your own question.",
        "What is it you're really asking?"],
     
    "(.*) mother(.*)":
        ["Tell me more about your mother.",
        "What was your relationship with your mother like?",
        "How do you feel about your mother?",
        "How does this relate to your feelings today?",
        "Good family relations are important."],
    
    "(.*) father(.*)":
        ["Tell me more about your father.",
        "How did your father make you feel?",
        "How do you feel about your father?",
        "Does your relationship with your father relate to your feelings today?",
        "Do you have trouble showing affection with your family?"],
         
         "(.*) brother(.*)":
        ["Tell me more about your brother.",
        "How did your brother make you feel?",
        "How do you feel about your brother?",
        "Does your relationship with your brother relate to your feelings today?"],
         
         "(.*) sister(.*)":
        ["Tell me more about your sister.",
        "How did your sister make you feel?",
        "How do you feel about your sister?",
        "Does your relationship with your sister relate to your feelings today?"],
    
    "(.*) child(.*)":
        ["Did you have close friends as a child?",
        "What is your favorite childhood memory?",
        "Do you remember any dreams or nightmares from childhood?",
        "Did the other children sometimes tease you?",
        "How do you think your childhood experiences relate to your feelings today?"],
     
    "(.*) family(.*)":
        ["Tell me more about your family.",
        "How did your family make you feel?",
        "How do you feel about your family?",
        "Does your relationship with your family relate to your feelings today?",
        "Do you have trouble showing affection with your family?"],
     
    "(.*) home(.*)":
        ["How many people stay in your home?",
           "How many bedrooms are there in your home?",
           "How far is your home from US?",
           "Do you miss your home?",
           "When are you planning to visit your home?"],
    
    "(.*) school(.*)":
        ["Do you miss your school now?",
         "Were you in any of your school's sport team?",
         "What time did go to school everyday?",
         "How many students were there in your school?",
         "Have you recently visited your school recently"],
    
     "(.*) friend(.*)":
        ["What is the importance of a friend in your life?",
         "What is the fond memories which you remember with your friend?",
         "Do you go trekking with your friend?",
         "Do you miss your college friends?",
         "Are you planning to have a reunion with your friend?"],
        
     "(.*) assignment(.*)":
        ["Do you always do your assignment on time?",
         "Do you have assignment every week?",
         "Have you maintained a timetable to do your assignment?",
         "Does your assignment carry lot of weightage for your final grade?",
         "When is your next assignment due?"],
     
    "(.*) absurd(.*)":
        ["What do you think it is absurd?",
         "Absurdity is the result of unreasonable choices."],
    
    "(.*) sleep(.*)":
          ["Have a nice sleep",
           "Goodnight"],
    
    "(.*) woke (.*)":
          ["What did you do after waking up?",
           "Do you like to wake up early?",],
      
    "(.*) book(.*)":
          ["Do you like reading book?",
        "What is your favorite book?",
        "When do you read book?"
        ],
     
    "(.*) food(.*)":
        ["Do you really like food",
        "What type of food do you like?",
        "Do you know to cook good food?",
        "Do you think of home when you think of food",
        "Do you eat veg or non-veg food?"],
    
    "(.*) technology(.*)":
        ["Are you fond of technology?",
         "Do you always keep yourself updated with technology?",
         "Do you own gadgets with latest technology?",
         "Do you think technology is impacting human interaction?",
         "Are gadgets with latest technology better than humans?",
         "How can we use technology to protect our environment?"],
    
    "It is (.*)":
        [ "You seem very certain.",
        "If I told you that it probably isn't %1, what would you feel?"],
     
    "(.*)maybe (.*)":
        [ "You seem very certain.",
        "If I told you that it probably isn't %1, what would you feel?"],
     
    "(.*) car(.*)":
        ["Do you have driving license to drive a car?",
         "Do you own a car?",
         "Which is your dream car?",
         "When are you planning to buy a car?",
         "Have you violated any traffic rules while driving a car?"],
    
    "(.*) dog(.*)":
        ["Do you have a dog?",
         "Do you think dogs are man's best friend?",
         "Do you have more than one dog?",
         "Do you take to your dog to the vet regularly",
         "Who takes care of your dog when you not at home?"],
     
}

#dictionary for reflective pronouns
#    The list is used to transform 1st person statement syntax to 2nd person statement syntax
reflections = {
    "am" : "are",
    "i" : "you",
    "me" : "you",
    "was" : "were",
    "my" : "your",
    "you" : "I",
    "are" : "am",
    "your" : "my",
    "yours" : "mine",
    "mine" : "yours",
    "i'd"  : "you would",
    "i've"  : "you have",
    "i'll"  : "you will",
    "i'm"  : "you are",
    "you'd" : "I would",
    "you've" : "I have",
    "you'll"  : "I will",
    "you're"  : "I am"
        }


#replace function is used for replacing the 1st person pronoun and other reflective
#words and return a transformed word
#old_word: word to be replace
#reflections: dictionary for getting the corresponding replace word for old_word
def replace(old_word, reflections):
#loop through the keys in dictionary reflections
    for key in reflections.keys():
#if key matched to old_word
        if old_word == key:
#return the value of the key
            return reflections.get(key)
    return old_word

#transformation function uses the words replaced by replace function and puts
#them together in the sentence
def transformation(old_str):
#remove punctuation marks
    old_str= remove_punc(old_str)
#convert the sentence to lower case
    old_str= old_str.lower()
#split the sentence to words
    words=re.split(r'[\s\t\n]+', old_str)
    new_words=[]
    for word in words:
        new_words.append(replace(word, reflections))
        
    transformed = ' '.join(new_words)
    return transformed

#punctuation is used to identify the punctuation marks in the sentence and remove them
#so that the sentence passed for transformation is punctuation free
def remove_punc(ostr):
#remove punctuation at end of input, if it has one
    if ostr.endswith('?'):
        ostr = ostr[:-1]
    elif ostr.endswith('.'):
        ostr = ostr[:-1] 
    return ostr
   
#respond function is used to get the sententence from the user, search the pattern in 
#qadict and respond accordingly by choosing random reply    
def respond(ques, qalist):
    answer="Can you tell more about it?"#default answer
    
#Check if the user is replying in simple Yes,No,Maybe probabilities.
    if re.match(r'Yes|yes', ques):
        answer = "You seem quite sure. Elaborate please."
        
    elif re.match(r'No|no', ques):
        answer = "Why do you deny? Elaborate please."
            
    elif re.match(r'Maybe|maybe', ques):
        answer = "What's the reason for the uncertainity?"               
            
#loop through the keys(question pattern RegEx) in dictionary: qadict            
    else:
        for x in qalist: 
#match the question pattern using regular expression     
            xl = re.compile(x, re.IGNORECASE)
            is_match = re.match(xl, ques)
            if is_match:
#choose the random reply from dict qadict corresponding to the ques
                answer = random.choice(qalist[x])
#find the position of % placeholder to replace it with main subject word from the ques 
                position = answer.find('%')
                while position > -1:
                    count = int(answer[position+1:position+2])
#transform the corresponding part of the question and put it the % in the reply
                    answer = answer[:position] + \
                    transformation(is_match.group(count)) + \
                    answer[position+2:]
                    position = answer.find('%')
                 
    return answer

#continue_conversation handles if the user is entering a response or statig any words from
#exit_words to exit from the program
def continue_conversation(response):
    if response in exit_words:
        print("It was nice talking to you, bye!")
    else:
#get the transformation reply by passing response as parameter
        re = transformation(response)
#get the response from the respond function by passing response and qadict as parameter
        strReply=respond(response, qadict)
        print("Oh! "+re+". "+strReply)
    return

#to check if the user is continuing the conversation
while response not in exit_words:
    try:
        response = input("~")
        continue_conversation(response)        
    except EOFError:
        print("Bye")
        exit()
