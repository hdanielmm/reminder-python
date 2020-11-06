from twilio.rest import Client 
 
account_sid = 'AC9686cd8eec2a2c39f7922727ca7edf40' 
auth_token = 'd0a5679d801144f518bef7ff6749a92f' 
client = Client(account_sid, auth_token) 
 
def my_job():
    message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='Recordatorio para llenar las horas de trabajo',      
        to='whatsapp:+573015628652' 
    ) 
 
    print(message.sid)