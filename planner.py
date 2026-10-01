# ================================
# DAILY ACTIVITY PLANNER
# ================================

# ---------- PART 1: homework time ----------
homework_minutes = int(input("How many minutes do you have for homework? "))
# Ask for the homework time in minutes.
# Turn the answer into a whole number with int().

# ---------- PART 2: choose a plan ----------
if homework_minutes > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

# ---------- PART 3: free time ----------
# YOUR CODE HERE
free_time = input("Is there free time after homework? (yes/no) ")
if free_time == "yes":
    print("Remember to pick a hobby!")


# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
print(f"Homework time: {homework_minutes} minutes")
print(f"Plan: {plan}")
print(f"Free time: {free_time}")