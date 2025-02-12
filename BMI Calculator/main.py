print("Body Mass Index (BMI) Calculator")

body_weight = float(input("Enter your weight in kg: "))
body_height = input("Enter your height (meters or feet, e.g., 1.75 or 5'9): ")

# Convert height to meters if entered in feet and inches
if "'" in body_height:
    feet, inches = map(int, body_height.split("'"))
    body_height = (feet * 0.3048) + (inches * 0.0254)

# Calculate BMI
body_mass = body_weight / (body_height ** 2)

# Determine BMI category
if body_mass < 18.5:
    category = "You are Underweight"
elif 18.5 <= body_mass < 24.9:
    category = "Your BMI is Normal"
elif 24.9 <= body_mass < 29.9:
    category = "You are Overweight"
else:
    category = "Obese"

# Display results
print(f"Your Body Mass Index (BMI) is: {body_mass:.2f}")
print(f"Category: {category}")
