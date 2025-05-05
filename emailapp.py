import streamlit as st
import smtplib
import random

def send_email(email,otp):
    sender_email="radheshyamshree1234@gmail.com"
    sender_password="ywfpmhpnkjihrqlf"
    receiver_email=email

    # subject="OTP Received"
    # body="Your otp is "
    message=f"your otp is {otp}"

    try:
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender_email,sender_password)
            server.sendmail(sender_email,receiver_email,message)
            return True
    except Exception as e:
     st.warning("Error",e)


def main():
    st.title("Welcome to the management Portal...")
    name=st.text_input("enter your name")
    email=st.text_input("enter your email")
    if st.button("send otp"):
        otp=random.randint(100000,999999)
        if email:
            if send_email(email,otp):
                st.success("otp sent successfully to ")
            else:
                st.warning("wrong")
        else:
            st.warning("fill all the field")



if __name__=='__main__':
    main()