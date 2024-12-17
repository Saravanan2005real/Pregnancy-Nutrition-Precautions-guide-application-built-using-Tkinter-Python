import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Pregnancy Nutrition & Precautions")
root.geometry("650x850")  # Adjust the window size as needed
root.configure(bg="#f7f3e9")  # Add a soft background color

# Set a nice font style
HEADING_FONT = ("Helvetica", 18, "bold")
SUBHEADING_FONT = ("Helvetica", 14, "bold")
BODY_FONT = ("Helvetica", 12)

# Heading label
heading_label = ttk.Label(
    root,
    text="Pregnancy Nutrition & Precautions",
    font=HEADING_FONT,
    background="#f7f3e9",
    foreground="#4b2c70"
)
heading_label.pack(pady=20)

# Dropdown menu label
dropdown_label = ttk.Label(
    root,
    text="Select your current week range:",
    font=SUBHEADING_FONT,
    background="#f7f3e9",
    foreground="#4b2c70"
)
dropdown_label.pack(pady=10)

# Create the dropdown menu (Combobox)
week_options = [
    "Week 1 to 4", "Week 5 to 8", "Week 9 to 12",
    "Week 13 to 16", "Week 17 to 20", "Week 21 to 24",
    "Week 25 to 28", "Week 29 to 32", "Week 33 to 36", "Week 37 to 40"
]
b = ttk.Combobox(root, values=week_options, state="readonly", font=BODY_FONT, width=25)
b.pack(pady=10)

# Label to display the message
nutrition_label = tk.Label(
    root,
    text="",
    wraplength=600,
    justify="left",
    font=("Verdana", 12, "italic"),  # Professional font with italic style
    bg="#f7f3e9",  # Matches the background color for consistency
    fg="#2c3e50",  # Professional dark gray color for text
    anchor="w",  # Align text to the left
    padx=10,  # Add padding for a clean look
    pady=10,  # Add padding for a clean look
    relief="groove",  # Adds a subtle border for separation
    borderwidth=2  # Border thickness for clarity
)
nutrition_label.pack(pady=20)

# Label for educational resources
education_label = tk.Label(
    root,
    text="",
    wraplength=600,
    justify="left",
    font=("Verdana", 12, "italic"),
    bg="#f7f3e9",
    fg="#2c3e50",
    anchor="w",
    padx=10,
    pady=10,
    relief="groove",
    borderwidth=2
)
education_label.pack(pady=10)

# Define the function
def display_nutrition_advice(*args):
    # Get the selected week range from the combobox
    selected_week = b.get()

    # Determine the appropriate message based on the selected week range
    if selected_week in ["Week 1 to 4", "Week 5 to 8", "Week 9 to 12"]:
        message = ("Trimester 1\n\n"
                   "Nutrition Advice:\n"
                   "• Folate-Rich Foods: Consume foods high in folate, such as leafy greens, citrus fruits, beans, and fortified cereals, to help prevent neural tube defects.\n"
                   "• Hydration: Drink plenty of water to stay hydrated and support healthy blood flow to the placenta.\n"
                   "• Small, Frequent Meals: Eat small, frequent meals to help alleviate nausea and maintain steady blood sugar levels.\n"
                   "• Lean Proteins: Include lean proteins like poultry, fish, eggs, and legumes to support fetal growth and development.\n"
                   "• Limit Caffeine: Reduce caffeine intake to no more than 200 milligrams per day to minimize the risk of miscarriage.\n\n"
                   "Precautions:\n"
                   "• Avoid Raw or Undercooked Foods: Steer clear of raw fish, unpasteurized dairy products, and undercooked meats to prevent foodborne illnesses.\n"
                   "• Limit Certain Fish: Limit intake of high-mercury fish like swordfish, shark, king mackerel, and tilefish, as they can harm fetal development.\n"
                   "• Stay Away from Alcohol and Smoking: Completely avoid alcohol and smoking, as they can lead to birth defects and other complications.")
        education_message = ("Recommended Educational Website:\n"
                             "• Visit [www.pregnancy.com](https://www.pregnancy.com) for more tips on nutrition and early pregnancy care.")
    elif selected_week in ["Week 13 to 16", "Week 17 to 20", "Week 21 to 24"]:
        message = ("Trimester 2\n\n"
                   "Nutrition Advice:\n"
                   "• Iron-Rich Foods: Increase intake of iron-rich foods like lean red meat, poultry, fish, beans, and fortified cereals to support the increased blood volume and prevent anemia.\n"
                   "• Calcium: Consume calcium-rich foods such as dairy products, leafy greens, tofu, and almonds to support fetal bone development.\n"
                   "• Healthy Fats: Incorporate sources of healthy fats like avocados, nuts, seeds, and olive oil to promote brain development in the baby.\n"
                   "• Fiber: Include fiber-rich foods like fruits, vegetables, whole grains, and legumes to prevent constipation.\n"
                   "• Prenatal Supplements: Continue taking prenatal vitamins as recommended by your healthcare provider.\n\n"
                   "Precautions:\n"
                   "• Avoid Certain Deli Meats and Unpasteurized Cheese: Steer clear of deli meats and soft cheeses like brie and feta, as they may contain harmful bacteria.\n"
                   "• Limit Processed Foods: Reduce intake of processed foods high in added sugars, sodium, and unhealthy fats, as they provide little nutritional value.\n"
                   "• Monitor Weight Gain: Keep track of weight gain and discuss any concerns with your healthcare provider to ensure it's within a healthy range.")
        education_message = ("Recommended Educational Website:\n"
                             "• Visit [www.babycenter.com](https://www.babycenter.com) for comprehensive pregnancy advice and information.")
    elif selected_week in ["Week 25 to 28", "Week 29 to 32", "Week 33 to 36", "Week 37 to 40"]:
        message = ("Trimester 3\n\n"
                   "Nutrition Advice:\n"
                   "• Omega-3 Fatty Acids: Include omega-3 fatty acids from sources like fatty fish (e.g., salmon, sardines), walnuts, flaxseeds, and chia seeds to support fetal brain and eye development.\n"
                   "• Protein: Maintain adequate protein intake to support fetal growth and development, aiming for about 71 grams per day.\n"
                   "• Complex Carbohydrates: Choose complex carbohydrates like whole grains, fruits, and vegetables to provide sustained energy and fiber.\n"
                   "• Fluid Intake: Continue to drink plenty of water to stay hydrated, especially as the due date approaches.\n"
                   "• Iron-Rich Foods: Ensure sufficient iron intake to prevent iron deficiency anemia and support red blood cell production.\n\n"
                   "Precautions:\n"
                   "• Watch for Signs of Preeclampsia: Monitor blood pressure and watch for symptoms like swelling, sudden weight gain, and headaches, which could indicate preeclampsia.\n"
                   "• Pelvic Rest: If advised by your healthcare provider, avoid activities that put pressure on the pelvis, such as heavy lifting or strenuous exercise, to prevent complications like preterm labor.\n"
                   "• Monitor Gestational Diabetes Risk: Stay mindful of gestational diabetes risk factors and discuss any concerns with your healthcare provider, especially if you have a family history or other risk factors.")
        education_message = ("Recommended Educational Website:\n"
                             "• Visit [www.webmd.com/pregnancy](https://www.webmd.com/pregnancy) for expert medical advice on pregnancy care and health.")

    else:
        message = "Invalid week range selected."
        education_message = ""

    # Display the messages in the labels
    nutrition_label.config(text=message)
    education_label.config(text=education_message)

# Bind the function to the Combobox selection event
b.bind("<<ComboboxSelected>>", display_nutrition_advice)

# Run the Tkinter main loop
root.mainloop()
