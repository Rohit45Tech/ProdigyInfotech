def check_password_strength(password):
    score = 0
    feedback = []
    
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True
    
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        score += 25
        feedback.append("Good length!")
    else:
        score += 10
    
    if has_upper:
        score += 15
        feedback.append("Good use of uppercase letters!")
    else:
        feedback.append("Add uppercase letters")
        
    if has_lower:
        score += 15
        feedback.append("Good use of lowercase letters!")
    else:
        feedback.append("Add lowercase letters")
        
    if has_number:
        score += 15
        feedback.append("Good use of numbers!")
    else:
        feedback.append("Add numbers")
        
    if has_special:
        score += 20
        feedback.append("Good use of special characters!")
    else:
        feedback.append("Add special characters")
    
    common_patterns = ["123", "abc", "password", "qwerty"]
    for pattern in common_patterns:
        if pattern in password.lower():
            score -= 20
            feedback.append(f"Avoid common patterns like '{pattern}'")
    
    if score >= 80:
        strength = "Very Strong"
    elif score >= 60:
        strength = "Strong"
    elif score >= 40:
        strength = "Moderate"
    elif score >= 20:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

test_passwords = [
    "password123",
    "SecureP@ss2023",
    "abc123",
    "MyP@ssw0rd!",
    "hello",
]

for password in test_passwords:
    result = check_password_strength(password)
    print("\nPassword:", password)
    print("Strength:", result["strength"])
    print("Score:", result["score"])
    print("Feedback:")
    for feedback in result["feedback"]:
        print("-", feedback)