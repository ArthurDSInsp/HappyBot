#New version updated to new API SLACK STANDARD https://python-slackclient.readthedocs.io/en/1.0.7/
#Update impactante: plus de statut presence_change communiqué par l'API via rtm.start

# -*- coding: cp1252 -*-
import os
import time
from slackclient import SlackClient

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("HAPPY_ID")
arthurds_id = os.environ.get("arthurds_id")
cho = os.environ.get("thuthuy_id")



# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('HAPPY_BOT_TOKEN'))

user_list = {arthurds_id:"arthur", cho:"Thu-Thuy"}
user_id_list = [arthurds_id]


message_sent={}
for user in user_id_list:
    message_sent[user] = 0
    print (message_sent[arthurds_id])

#--------------------------------------------------------------------------
#detect that a message was sent to happy and send it to the CHO

def parse_slack_useranswer(output_list):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and len(output['text'])>0:
                 #return text after the @ mention, whitespace removed
                return output['text'], output['user'], output['channel']
    return None, None, None
#--------------------------------------------------------------------------------
#Send to the CHO the answer of the user

def cho_feedback(msg, user):
    feedback = "Hey TT! "+ user +" sent "+ "'"+ msg +"'"
    slack_client.api_call(
        "chat.postMessage",
        channel=cho,
        text=feedback,
        as_user=True
        )
#--------------------------------------------------------------------------------------


def welcome(user): 
    #print(user) #test
    if user in user_id_list:
        if message_sent[user] < 1:
            response = "Hey " + user +"! How are you today?"
            slack_client.api_call(
                "chat.postMessage",
                channel=user,
                text=response,
                as_user=True
                )
            message_sent[user] = 1
            print (message_sent[user]) #test
            time.sleep(READ_WEBSOCKET_DELAY)
#-----------------------------------------------------------------------------------------


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
        
            slackinput_list = slack_client.rtm_read()
            welcome(user)
            print (slackinput_list) #test
            if slackinput_list and len(slackinput_list)>0:
                            user_answer, user_id, channel = parse_slack_useranswer(slackinput_list)
                            print(user_answer,user_id)#test
                            if user_answer and user_id and user_id!='U7GRT34H3':
                                cho_feedback(user_answer, user_id)
            #print(presence, user, user_answer)
            
                
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")




