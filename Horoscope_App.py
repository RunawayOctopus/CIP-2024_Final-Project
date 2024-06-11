import random

def get_star_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return None

def get_horoscope(star_sign):
    horoscopes = {
        "Capricorn": [
            "Today you will find success in your efforts.",
            "An old friend may reach out to you.",
            "A new opportunity will present itself."
        ],
        "Aquarius": [
            "You will have a pleasant surprise today.",
            "A creative project will bring you joy.",
            "Expect good news in your professional life."
        ],
        "Pisces": [
            "A new opportunity is on the horizon.",
            "You will find peace in solitude.",
            "Your intuition will guide you to success."
        ],
        "Aries": [
            "Your energy levels will be high today.",
            "Take the initiative in your tasks.",
            "A leadership role will come naturally to you."
        ],
        "Taurus": [
            "Focus on your goals and you will achieve them.",
            "A financial opportunity may arise.",
            "Take time to enjoy nature."
        ],
        "Gemini": [
            "Communication is key today.",
            "You will reconnect with an old acquaintance.",
            "New knowledge will enrich your life."
        ],
        "Cancer": [
            "You will find comfort in familiar surroundings.",
            "Family matters will bring you joy.",
            "A home project will be successful."
        ],
        "Leo": [
            "A leadership opportunity will come your way.",
            "Your confidence will attract positive attention.",
            "You will feel inspired to start something new."
        ],
        "Virgo": [
            "Pay attention to the details today.",
            "A work task will require your precision.",
            "Your organizational skills will be rewarded."
        ],
        "Libra": [
            "Balance is important in your endeavors.",
            "A harmonious relationship will bring happiness.",
            "Take time to reflect on your goals."
        ],
        "Scorpio": [
            "Your determination will yield results.",
            "A mystery will be solved in your favor.",
            "You will feel empowered to make changes."
        ],
        "Sagittarius": [
            "Adventure awaits you today.",
            "A travel plan will excite you.",
            "You will meet someone with similar interests."
        ]
    }
    
    if star_sign in horoscopes:
        return random.choice(horoscopes[star_sign])
    else:
        return "Horoscope not available."

def main():
    continue_program = True
    while continue_program:
        birthday = input("Enter your birthday (MM-DD): ")
        month, day = map(int, birthday.split('-'))
        star_sign = get_star_sign(day, month)
        
        if star_sign:
            print(f"Your star sign is: {star_sign}")
            horoscope = get_horoscope(star_sign)
            print(f"Your horoscope: {horoscope}")
        else:
            print("Invalid date entered.")
        
        user_input = input("Would you like to check another horoscope? (yes/no): ").strip().lower()
        if user_input != 'yes':
            continue_program = False

if __name__ == "__main__":
    main()
