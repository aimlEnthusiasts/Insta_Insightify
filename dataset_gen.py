import pandas as pd
import random

# Define post types and engagement metrics
post_types = ["Carousel", "Reels", "Static Image"]
engagement_metrics = ["likes", "shares", "comments"]

# Generate dataset
def generate_mock_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "post_id": f"post_{random.randint(1, 10000)}",
            "post_type": random.choice(post_types),
            "likes": random.randint(10, 1000),
            "shares": random.randint(5, 500),
            "comments": random.randint(2, 200)
        }
        data.append(record)
    return data

# Generate 100 records
mock_data = generate_mock_data(100)

# Convert to DataFrame
df = pd.DataFrame(mock_data)

# Save to a valid path on your system
df.to_csv("dataset.csv")
print(f"Mock dataset saved to dataset.csv")