def build_dynamic_prompt(user_data):
    """
    Builds a full prompt string for GPT based on user profile and answers.
    """

    age = user_data.get("age")
    gender = user_data.get("gender")
    height = user_data.get("height_cm")
    weight = user_data.get("weight_kg")
    bmi = user_data.get("bmi")
    goal = user_data.get("goal")
    meals_per_day = user_data.get("meals_per_day")
    workout_freq = user_data.get("workout_frequency")
    workout_type = user_data.get("workout_type")
    gain_goal = user_data.get("weight_gain_goal")
    gain_amount = user_data.get("weight_gain_amount")
    activity_level = user_data.get("activity_level")
    beverage_pref = user_data.get("beverage_preference")
    dessert_freq = user_data.get("dessert_frequency")
    protein_choices = user_data.get("protein_choices", [])
    carb_choices = user_data.get("carb_choices", [])
    vegetable_choices = user_data.get("vegetable_choices", [])
    fruit_choices = user_data.get("fruit_choices", [])
    grain_choices = user_data.get("grain_choices", [])
    seafood_choices = user_data.get("seafood_choices", [])
    fats_choices = user_data.get("fats_choices", [])
    cooking_styles = user_data.get("cooking_styles", [])
    allergies = user_data.get("allergies", [])

    prompt = f"""
You are a certified nutritionist.

Create a 7-day structured meal plan for the following user:

Age: {age}
Gender: {gender}
Height: {height} cm
Weight: {weight} kg
BMI: {bmi}
Goal: {goal}
Weight Gain Goal: {gain_goal} (Target gain: {gain_amount})
Workout Frequency: {workout_freq}
Workout Type: {workout_type}
Daily Activity Level: {activity_level}
Meals Per Day: {meals_per_day}
Preferred Cooking Styles: {", ".join(cooking_styles)}
Protein Sources: {", ".join(protein_choices)}
Carbohydrates: {", ".join(carb_choices)}
Vegetables: {", ".join(vegetable_choices)}
Fruits: {", ".join(fruit_choices)}
Grains: {", ".join(grain_choices)}
Seafood: {", ".join(seafood_choices)}
Fats & Oils: {", ".join(fats_choices)}
Beverages: {beverage_pref}
Dessert/Sweet Frequency: {dessert_freq}
Allergies or Intolerances: {", ".join(allergies) if allergies else "None"}

Instructions:
1. Generate a realistic, practical meal plan based strictly on the user preferences above.
2. Each day must include {meals_per_day}, following user-selected meals/snacks style.
3. Every meal must include estimated **calories, protein, carbohydrates, and fats**.
4. At the top, show the user's **daily macronutrient & calorie requirement** based on BMI, weight, activity.
5. At the end, give a summary of total weekly intake of calories, protein, carbs, and fats.
6. Only suggest food the user selected, and avoid ingredients from the allergies list.
7. Include daily exercise recommendation based on user goal and type of workout.

Be accurate and use real dietitian logic.
"""
    return prompt
