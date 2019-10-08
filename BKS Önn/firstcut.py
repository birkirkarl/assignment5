has_ball_str= input("Does the lead team have the ball (Yes or no) : ")
if has_ball_str == "Yes":
    lead_calculation_float = lead_calculation_float + 0.5
else:
    lead_calculation_float = lead_calculation_float - 0.5   

if lead_calculation_float < 0:
    lead_calculation_float = 0
    lead_calculation_float = lead_calculation_float ** 2
    seconds_remaining_int = int(input("Enter the number of seconds remaining: "))
    if lead_calculation_float > seconds_remaining_int:
        print ("Lead is safe")
    else:
        print("Lead is not safe")         