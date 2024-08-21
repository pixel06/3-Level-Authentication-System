import random
import string
import time
from getpass import getpass

def biometric_auth():
    print("Simulating biometric authentication (e.g., fingerprint scan)...")
    time.sleep(2)
    return True

def behavioral_auth():
    print("Please retype the following phrase as quickly as possible: 'Secure Authentication'")
    phrase = "Secure Authentication"
    start_time = time.time()
    user_input = input("Retype here: ")
    end_time = time.time()
    
    if user_input == phrase and (end_time - start_time) < 10: 
        return True
    else:
        return False

def captcha_verification():
    captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    print(f"CAPTCHA: {captcha}")
    user_input = input("Please enter the CAPTCHA: ")
    
    if user_input == captcha:
        return True
    else:
        return False

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def otp_verification():
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
    user_input = input("Enter the OTP sent to your phone: ")
    
    if user_input == otp:
        return True
    else:
        return False

def hybrid_auth_system():
    print("Starting Hybrid Authentication System...\n")
    
    if biometric_auth():
        print("Biometric Authentication Successful!\n")
    else:
        print("Biometric Authentication Failed!")
        return False
    
    if behavioral_auth():
        print("Behavioral Authentication Successful!\n")
    else:
        print("Behavioral Authentication Failed!")
        return False
    
    if captcha_verification():
        print("CAPTCHA Verification Successful!\n")
    else:
        print("CAPTCHA Verification Failed!")
        return False
    
    if otp_verification():
        print("Two-Factor Authentication Successful!\n")
        print("Access Granted! Welcome to the system.")
        return True
    else:
        print("Two-Factor Authentication Failed!")
        return False

if __name__ == "__main__":
    if hybrid_auth_system():
        print("Authentication successful, system access granted.")
    else:
        print("Authentication failed, access denied.")
