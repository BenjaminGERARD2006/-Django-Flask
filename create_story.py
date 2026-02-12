import requests

base = "http://127.0.0.1:5000"

# Create story
story = requests.post(f"{base}/stories", json={
    "title": "The Lost Cave",
    "description": "A short adventure in a mysterious cave"
}).json()

story_id = story["id"]
print("Story created:", story_id)

# Start page
p1 = requests.post(f"{base}/stories/{story_id}/pages", json={
    "text": "You stand at the entrance of a dark cave.",
    "is_ending": False
}).json()

# Ending 1
p2 = requests.post(f"{base}/stories/{story_id}/pages", json={
    "text": "You go deeper and find treasure!",
    "is_ending": True,
    "ending_label": "Treasure Ending"
}).json()

# Ending 2
p3 = requests.post(f"{base}/stories/{story_id}/pages", json={
    "text": "You run away safely.",
    "is_ending": True,
    "ending_label": "Safe Ending"
}).json()

# Choices
requests.post(f"{base}/pages/{p1['page_id']}/choices", json={
    "text": "Enter the cave",
    "next_page_id": p2["page_id"]
})

requests.post(f"{base}/pages/{p1['page_id']}/choices", json={
    "text": "Run away",
    "next_page_id": p3["page_id"]
})

# Set start page
requests.put(f"{base}/stories/{story_id}", json={
    "start_page_id": p1["page_id"]
})

print("Story fully created!")
