def otpcheck():
    from twilio.rest import Client
    import datetime as dt 
    import sqlite3 as sq
    conn=sq.connect("pancard.db")
    cursor=conn.execute("SELECT max(OTP) FROM OTP")
    for i in cursor:    
        new_otp=int(i[0])+1         
    number='+917507483508'
    account_sid = 'AC9ca57309561dff05e457f51f0d40370a'
    auth_token = 'd5a27293ea20119e6a61f540983efb30'
    client = Client(account_sid, auth_token)
    body1="your otp number is {0}"
    body2=body1.format(new_otp)
    message = client.messages.create(
                  body=body2,
                  from_='+17065100684',
                  to=number,
                )
    t1=dt.datetime.today()
    t11=(t1.hour*3600+ t1.minute*60 + t1.second)
    verify_otp=int(input("enter your otp received on your registered mobile number which is valid for only 2 minutes : "))
    t2=dt.datetime.today()
    t22=(t2.hour*3600+ t2.minute*60 + t2.second)
    t3=t22-t11
    query1="INSERT INTO OTP (OTP,USED) VALUES({0},'Y')"
    query2=query1.format(new_otp)
    cursor=conn.execute(query2)
    conn.commit()
    conn.close()
    if t3 <=120:  # setting 120 seconds of otp vaidity
        if int(verify_otp)==int(new_otp):
            return 1  # proceed with aadhar regsitration/ pan card registration
        else:
            return 2   # invalid user due to otp/no otp  mismatch
    else:
        return 3    #OTP time out
    