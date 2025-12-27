# Variables
name = "Sayan"
age = 20
is_dev = True

# List
skills = ["JS", "TS", "React", "Next.js"]
skills.append("Python")

# Dictionary
profile = {
    "name": name,
    "age": age,
    "skills": skills
}

# Function
def describe(profile):
    return f"{profile['name']} is {profile['age']} years old and learning {profile['skills'][-1]}"

print(describe(profile))
