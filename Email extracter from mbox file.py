import mailbox

def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets
def handleerror(errmsg, emailmsg, cs):
    print("==")
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])
def getbodyfromemail(msg):
    body = 'no_text'
    body_html = 'no_html'
    #Walk through the parts of the email to find the text body.    
    if msg.is_multipart():    
        for part in msg.walk():

            # If part is multipart, walk through the subparts.            
            if part.is_multipart(): 

                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        # Get the subpart payload (i.e the message body)
                        body = subpart.get_payload(decode=True) 
                        #charset = subpart.get_charset()
                    elif subpart.get_content_type() == 'html':
                        body_html = subpart.get_payload(decode=True)
                        #body_html = subpart.get_payload(decode=True)

            # Part isn't multipart so get the email body
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                #charset = part.get_charset()

    # If this isn't a multi-part message then get the payload (i.e the message body)
    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True) 

   # No checking done to match the charset with the correct part. 
    for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.",msg,charset)
        except AttributeError:
             handleerror("AttributeError: encountered" ,msg,charset)
    return body, body_html  

mboxfile = 'Inbox.mbox'
body = []
body_html = []
for thisemail in mailbox.mbox(mboxfile):
    body.append(getbodyfromemail(thisemail)[0])
    body_html.append(getbodyfromemail(thisemail)[1])
    print(body_html)
  
