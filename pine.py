def deaf_grandma(you):
    REPLY_HUH = "HUH?! SPEAK UP, SONNY!"
    REPLY_NOT_SINCE = "NO, NOT SINCE 1938!"
    REPLY_OK_BYE = "OK, BYE!"
    ENDING_PHRASE = "BYE"  

    grandma_replies = []
    conversation_ended = False  

    for sentence in you:
        if conversation_ended:
            break

        if sentence == ENDING_PHRASE:
            grandma_replies.append(REPLY_OK_BYE)
            conversation_ended = True  
    
        elif sentence.isupper():

            grandma_replies.append(REPLY_NOT_SINCE)
            
        else:
            grandma_replies.append(REPLY_HUH)
            
    return grandma_replies
