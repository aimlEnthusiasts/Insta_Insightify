import requests
import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="Chat Interface",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded",
)

# CSS for dark theme, animations, and responsiveness
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #2b2b42, #1e1e2f);
            color: #f0f0f0;
            font-family: "Arial", sans-serif;
        }
        .stButton button {
            background: linear-gradient(90deg, #ff8c00, #ff0080);
            color: white;
            border: none;
            padding: 0.7em 1.8em;
            font-size: 1.1rem;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .stButton button:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        .custom-input {
            background-color: #2c2c3a;
            color: #f0f0f0;
            border: 1px solid #555;
            border-radius: 8px;
            padding: 0.8em;
            width: 100%;
            font-size: 1rem;
        }
        .stTextArea textarea {
            background-color: #2c2c3a;
            color: white;
            border-radius: 8px;
            padding: 1em;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 1em;
        }
        .logo-container img {
            width: 150px;
            height: auto;
            border-radius: 12px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4), 0 4px 8px rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .logo-container img:hover {
            transform: scale(1.1);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.6), 0 6px 12px rgba(255, 255, 255, 0.2);
        }
        .response-box {
            background-color: #23232e;
            border-radius: 10px;
            padding: 1em;
            margin-top: 1em;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .response-box p {
            color: #f0f0f0;
            font-size: 1.1rem;
            line-height: 1.5;
        }
        .sidebar-section {
            padding: 1em;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.05);
            margin-bottom: 1em;
        }
        .custom-subscription-btn {
            background: linear-gradient(90deg, #ff8c00, #ff0080);
            color: white;
            border: none;
            padding: 0.7em 2em;
            font-size: 1.1rem;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: inline-block;
            margin-top: 1em;
            cursor: pointer;
        }
        .custom-subscription-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# API Details
BASE_API_URL = "https://api.langflow.astra.datastax.com"
APPLICATION_TOKEN = "AstraCS:GKjQwrPLWQmawTcEiZWZJBZT:2813212496ccc21fe1bf935fd375a43b702f382495f3f28f1592c448f05120ee"

# Function to run the flow
def run_flow(base_url: str, langflow_id: str, flow_id: str, endpoint: str, message: str, token: str) -> dict:
    api_url = f"{base_url}/lf/{langflow_id}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Main function
def main():
    add_custom_css()
     # Logo section
    st.markdown(
        """
        <div class="logo-container">
            <img src="logo.png" alt="BRO CODE Logo">
        </div>
        """,
        unsafe_allow_html=True,
    )

    
    # Sidebar for flow configuration
    st.sidebar.header("🔧 Flow Configuration")
    st.sidebar.markdown("Configure the API and flow settings below:")
    
    with st.sidebar.container():
        with st.expander("Configuration Settings", expanded=True):
            base_api_url = st.text_input("Base API URL", BASE_API_URL, help="Enter the base API URL")
            langflow_id = st.text_input("Langflow ID", "90035930-fb33-4d1b-b12e-0c18d786f06b", help="Enter the Langflow ID")
            flow_id = st.text_input("Flow ID", "9a5d963f-7938-477a-98b1-aa3e1e567946", help="Enter the Flow ID")
            endpoint = st.text_input("Endpoint", "II", help="Enter the endpoint name")

    st.sidebar.markdown("---")
    
    # Section for API token configuration
    st.sidebar.header("🔐 API Token Configuration")
    token = st.sidebar.text_input("API Token", APPLICATION_TOKEN, type="password", help="Enter your API token")

    # Save configuration button
    if st.sidebar.button("Save Configuration"):
        try:
            with open("config.txt", "w") as config_file:
                config_file.write(f"BASE_API_URL={base_api_url}\n")
                config_file.write(f"LANGFLOW_ID={langflow_id}\n")
                config_file.write(f"FLOW_ID={flow_id}\n")
                config_file.write(f"ENDPOINT={endpoint}\n")
                config_file.write(f"APPLICATION_TOKEN={token}\n")
            st.sidebar.success("Configuration saved successfully!")
        except Exception as e:
            st.sidebar.error(f"Error saving configuration: {str(e)}")

    # Input area for chat
    st.markdown("---")
    st.header("💬 Chat with Us")
    message = st.text_area(
        "Your Message", "", placeholder="Type your query here...", key="message_input", help="Enter your message."
    )

    # Run flow button
    if st.button("🚀 Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return

        try:
            with st.spinner("Executing flow..."):
                response = run_flow(base_api_url, langflow_id, flow_id, endpoint, message, token)
                output_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]

                st.markdown(
                    """
                    <div class="response-box">
                        <p><strong>Response:</strong> {}</p>
                    </div>
                    """.format(output_text),
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Subscription Plans Section (appears after clicking the button)
    if st.button("🌟 View Subscription Plans"):
        plan_type = "Free"  # Default to Free plan
        st.markdown(
            """
            <div class="response-box">
                <h3>Subscription Plans</h3>
                <p><strong>Basic Plan:</strong> Free access with limited queries per day.</p>
                <p><strong>Premium Plan:</strong> Unlimited queries, advanced features, and priority support.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Show pricing and options
        st.markdown(
            """
            <div class="response-box">
                <h4>Choose Your Plan</h4>
                <p><strong>Free Plan:</strong> Free</p>
                <button class="custom-subscription-btn">🎉 Free</button>
                <p><strong>Premium Plan:</strong> ₹299</p>
                <button class="custom-subscription-btn">💳 Pay ₹299</button>
            </div>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
