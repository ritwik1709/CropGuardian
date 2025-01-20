import streamlit as st
import openai
css = """
<style>
   @import url('https://fonts.googleapis.com/css2?family=Jersey+10&display=swap');
   @import url('https://fonts.googleapis.com/css2?family=Macondo&display=swap');
   @import url('https://fonts.googleapis.com/css2?family=Pirata+One&display=swap');

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
    }
    input[type="number"] {
            width: calc(100% - 2rem);
            padding: 10px 25px;
            border-radius: 4px;
            font-size: 1rem;
        }
    .streamlit-expanderHeader {
        font-size: 1.5rem;
        font-weight: bold;
    }
    .css-1v3fvcr {
        margin-bottom: 1rem;
    }
    h1{
     font-family: "Pirata One", sans-serif;
    }
    .stButton button {
        background-color: #03b403;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #008000;
        color:#fff;
    }
    .css-1l02rfh {
        margin: 0;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)
# Set your OpenAI API key
openai.api_key = "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"

# Initialize the session state for conversation history
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful agriculture expert who assists in suggesting fertilizers."}
    ]

# Function to generate fertilizer suggestion
def generate_fertilizer_suggestion(N, P, K, ph, crop):
    prompt = f"""
    You are an expert in agriculture and soil science. Based on the following soil and crop characteristics, recommend the most suitable fertilizer and provide a detailed explanation in these 4 steps and one final step that is to suggest a fertiliser to purchase and use:

    Based on the following soil and crop characteristics, recommend the most suitable fertilizer:
    Nitrogen (N) content = {N},
    Phosphorus (P) content = {P},
    Potassium (K) content = {K},
    Soil pH level = {ph},
    Crop type = {crop}.
    
    Provide a detailed explanation for your recommendation in 4 steps:
    1. Comment on the Nitrogen content.
    2. Comment on the Phosphorus content.
    3. Comment on the Potassium content.
    4. Comment on the pH content.
    5. Suggest which common fertiliser to purchase or use considering the descriptions and the former 4 steps at the best of your knowledge in 2 lines
    
    Suggest any additional measures such as organic matter or other amendments such as suggesting a fertiliser that a person can buy also considering the input features and the specific requirements.

    Example 1:
    Nitrogen (N) content = 101
    Phosphorus (P) content = 17
    Potassium (K) content = 47
    Soil pH level = 6.18
    Crop = muskmelon
    Fertilizer Suggestion:
    1. **Nitrogen Content**: The soil's high nitrogen content of 101 indicates a good supply for plant growth. However, muskmelons have high nitrogen requirements, especially during the vegetative growth stage. To further enhance nitrogen availability, consider incorporating organic matter like compost or well-rotted manure into the soil. This will provide a slow-release nitrogen source, promoting steady growth and fruit development. Excessive nitrogen can lead to lush foliage at the expense of fruit production, so monitoring plant growth is crucial.
    2. **Phosphorus Content**: The soil's phosphorus content of 17 is moderate. Phosphorus is essential for root development and fruit formation in muskmelons. To boost phosphorus levels, consider adding phosphorus-rich organic fertilizers like bone meal or rock phosphate. Additionally, planting cover crops like legumes can help fix atmospheric phosphorus in the soil. However, excessive phosphorus can lead to nutrient imbalances and environmental pollution, so it's important to apply phosphorus based on soil test recommendations.
    3. **Potassium Content**: The soil's potassium content of 47 is adequate for muskmelon growth. Potassium plays a crucial role in fruit development, disease resistance, and overall plant health. To maintain potassium levels, consider using potassium-rich fertilizers like potassium sulfate or potassium chloride. Green manure crops like clover can also enhance potassium availability. However, excessive potassium can interfere with magnesium and calcium uptake, so it's important to maintain a balanced nutrient ratio.
    4. **pH Content**: The soil's pH level of 6.18 is slightly acidic, which is suitable for muskmelons as they prefer a pH range of 6.0-6.8. To further optimize pH levels, consider incorporating lime to raise pH if necessary. Additionally, planting pH-adjusting cover crops like buckwheat can help regulate soil acidity. However, extreme pH levels can lead to nutrient deficiencies or toxicities, affecting plant growth and fruit quality. Regular soil testing and monitoring are essential to ensure optimal pH levels for muskmelon cultivation.
    Consider using a balanced N-P-K fertilizer like a 10-10-10 mix, or a slow-release fertilizer like Osmocote, which can provide consistent nutrient release throughout the growing season.
    Example 2:
    Nitrogen (N) content = 98
    Phosphorus (P) content = 8
    Potassium (K) content = 51
    Soil pH level = 6.26
    Crop = watermelon
    Fertilizer Suggestion:
    1. **Nitrogen Content:** The soil's high nitrogen content of 98 indicates that there is already an abundant supply of nitrogen available for the watermelon crop. Watermelons require a significant amount of nitrogen for healthy growth, especially during the early stages and fruit development. To improve nitrogen availability further, you can consider incorporating organic matter such as compost or manure into the soil. However, excessive nitrogen can lead to excessive vegetative growth at the expense of fruit production.
    2. **Phosphorus Content:** The soil's phosphorus content of 8 is relatively low for watermelon cultivation. Phosphorus is crucial for root development, flowering, and fruit set in watermelon plants. To enhance phosphorus levels, you may need to apply a phosphorus-rich fertilizer, such as superphosphate, during planting. Additionally, incorporating bone meal or rock phosphate into the soil can provide a slow-release source of phosphorus. However, excessive phosphorus can lead to nutrient imbalances and environmental pollution.
    3. **Potassium Content:** The soil's potassium content of 51 is at a moderate level, which is beneficial for watermelon growth. Potassium plays a vital role in overall plant health, fruit development, and disease resistance. To maintain optimal potassium levels, you can use potassium-rich fertilizers like potassium sulfate or potassium chloride. Green manure crops like clover or vetch can also help increase potassium levels naturally. Excessive potassium can interfere with calcium and magnesium uptake in plants.
    4. **pH Content:** The soil's slightly acidic pH level of 6.25 is generally suitable for watermelon cultivation, as watermelons prefer a pH range of 6.0-6.8. To adjust the pH, you can incorporate lime to raise the pH or elemental sulfur to lower it, depending on the specific requirements of watermelon plants. Regular soil testing is essential to monitor and maintain the pH within the optimal range. However, drastic pH fluctuations can impact nutrient availability and plant growth negatively.
    A fertilizer with an N-P-K ratio like 10-20-20 or 15-15-30 is suitable for watermelons, or consider using a watermelon-specific fertilizer like Jobe’s Organics Watermelon Fertilizer Spikes.
    Now, given the following soil and crop characteristics that you've received from the input, please provide a detailed fertilizer recommendation in accordance to the instructions:
    """

    st.session_state['messages'].append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages'],
        max_tokens=400,
        temperature=0.5
    )
    
    st.session_state['messages'].append({"role": "assistant", "content": response['choices'][0]['message']['content'].strip()})
    return st.session_state['messages'][-1]['content']

# Streamlit UI
st.title("CropGuardian: Fertilizer Recommendation👨‍🌾")

st.write("Enter the soil and crop characteristics to get a fertilizer suggestion.")

# Input fields for the soil and crop characteristics
N = st.number_input("Nitrogen (N) content", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P) content", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K) content", min_value=0.0, step=1.0)
ph = st.number_input("Soil pH level", min_value=0.0, step=0.1)
crop = st.text_input("Crop type")

if st.button("Get Fertilizer Suggestion"):
    if crop:
        suggestion = generate_fertilizer_suggestion(N, P, K, ph, crop)
        st.write("### Fertilizer Suggestion")
        st.write(suggestion)

if 'messages' in st.session_state:
    for message in st.session_state['messages']:
        if message['role'] == 'user' and "Crop type" not in message['content']:
            st.write(f"**You:** {message['content']}")
        elif message['role'] == 'assistant':
            st.write(f"**Chatbot:** {message['content']}")

st.write("### Continue the Conversation")
conversation_input = st.text_input("Ask more about this suggestion or related topics:")
if conversation_input:
    st.session_state['messages'].append({"role": "user", "content": conversation_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages'],
        max_tokens=320,
        temperature=0.5
    )
    st.session_state['messages'].append({"role": "assistant", "content": response['choices'][0]['message']['content'].strip()})
    st.write(response['choices'][0]['message']['content'].strip())