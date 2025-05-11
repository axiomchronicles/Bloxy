import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        return False
    
    local_part, domain_part = email.split('@')
    
    if len(local_part) > 64 or len(domain_part) > 255 or len(email) > 320:
        return False
    
    if '..' in local_part or '..' in domain_part:
        return False
    
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    
    if domain_part.startswith('-') or domain_part.endswith('-'):
        return False
    
    if not re.match(r'^[a-zA-Z0-9_.+-]+$', local_part):
        return False
    
    if not re.match(r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', domain_part):
        return False
    
    return True

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    if len(password) > 64:
        return False, "Password must be no more than 64 characters long."
    
    if re.search(r'\s', password):
        return False, "Password must not contain spaces."
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    
    common_passwords = [
        "password", "123456", "12345678", "123456789", "12345", "1234567", "1234567890", "qwerty", "abc123", "football"
    ]
    
    if password.lower() in common_passwords:
        return False, "Password is too common and insecure. Please choose a different password."
    
    return True, "Password is valid."