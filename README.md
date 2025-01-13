# Social Media Performance Analysis Tool - Insta Insightify

## 📋 **Overview**
The **Insta Insightify** is designed to analyze social media engagement data, providing actionable insights to improve content strategies. This project was developed as part of a pre-hackathon assignment for the Level Supermind Hackathon.

The tool includes:
- A dataset simulating social media engagement metrics.
- Python scripts for dataset generation and basic analytics.
- Langflow workflows for querying data and generating insights.
- Integration with DataStax Astra DB for efficient data storage and retrieval.
- Website code for visualization and interaction.

*Note: Kindly add your api key in flow
---

## 🗂 **Project Structure**
```
🗁 Insta Insightify
   🗋   Insta_Insightify_tool.py             # Main python script of tool.
   🗋  Insta_Insightify_version_01.json      # Initial version of the analysis tool.
   🗋  Insta_Insightify_version_02.json      # Enhanced version of the analysis tool.
   🗋  Insta_Insightify_version_03.json      # Upgraded version with edge case handling.
   🗋   README.md                            # Project documentation.
   🗋   config.txt                           # configuration credentials.
   🗋   dataset.csv                          # Mock dataset of social media engagement.
   🗋   dataset_gen.py                       # Python script to generate the dataset.
   🗋   requirements.txt                     # Python dependencies.
```

---

## 🛠️ **Features**
1. **Dataset Generation**:
   - A Python script (`generate_dataset.py`) generates a mock dataset simulating engagement metrics (e.g., likes, shares, comments, post types).

2. **Data Storage**:
   - Utilizes **DataStax Astra DB** for storing and querying the dataset.

3. **Performance Analysis**:
   - Leverages **Langflow** to:
     - Query average engagement metrics by post type (Carousel, Reels, Static Images).
     - Generate insights using GPT integration.

4. **Interactive Website**:
   - A user-friendly interface to visualize engagement metrics and insights.

5. **Modular Versions**:
   - **Version 01**: Basic functionality.
   - **Version 02**: Enhanced features and improved analysis.
   - **Version 03**: Edge cases handled.
  
---

## 🚀 **How to Run Insta Insightify Tool**
### Prerequisites
- Python 3.8+
- DataStax Astra DB account

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/TeamBroC0de/Insta_Insightify.git
   cd Insta_Insightify
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Command:
   ```bash
   streamlit run .\Insta_Insightify_tool.py
   ```

4. Testing tool:
   - Case 1 (Post Type in Input): <br>
           e.g: Reels <br>
           output: Returns detailed Insights.<br>
           e.g: Carousal<br>
           output: Returns detailed Insights.<br><br>
     
   - Case 2 (Missing Post Type in Input):<br>
           e.g: Hello<br>
           output: Error: Missing 'post_type' field in dataset. Please ensure all entries have a valid post type<br>
           e.g: How are you<br>
           output: Error: Missing 'post_type' field in dataset. Please ensure all entries have a valid post type<br><br>

---

## 🚀 **How to Run Tool on Langflow workflow**

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/TeamBroC0de/Insta_Insightify.git
   cd Insta_Insightify
   ```

2. Open [Langflow](https://www.langflow.org/).
   - Create blank workflow.
   - Import "Insta_Insightify_version_02" or "Insta_Insightify_version_03"
   - Give dataset.csv as input in workflow (Optional)

3.  Testing tool:
   - Case 1 (Post Type in Input): <br>
           e.g: Reels <br>
           output: Returns detailed Insights.<br>
           e.g: Carousal<br>
           output: Returns detailed Insights.<br><br>
     
   - Case 2 (Missing Post Type in Input):<br>
           e.g: Hello<br>
           output: Error: Missing 'post_type' field in dataset. Please ensure all entries have a valid post type<br>
           e.g: How are you<br>
           output: Error: Missing 'post_type' field in dataset. Please ensure all entries have a valid post type<br><br>

---

## 📊 **Insights**
Example outputs from the tool:
- Carousel posts have 20% higher engagement than static posts.
- Reels drive 2x more comments compared to other formats.

---

## 🎥 **Demo Video**
A video showcasing the tool's features is available [here](https://www.youtube.com/watch?v=PPokMwolnBo).

---

## 📧 **Contact**
For questions or feedback, please reach out to the discussions.
