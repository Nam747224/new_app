def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    else:
        return "Béo phì"
