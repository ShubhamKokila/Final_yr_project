# import streamlit as st
# import pandas as pd
# import pickle

# # Load the pickled model
# try:
#     with open('/home/shubham09/final_yr_project/fertlizer_recommedation/classifier.pkl', 'rb') as model_file:
#         model = pickle.load(model_file)
# except FileNotFoundError:
#     st.error("Model file not found. Please ensure that 'classifier.pkl' exists in the specified path.")
#     st.stop()
# except Exception as e:
#     st.error(f"Error loading the model: {e}")
#     st.stop()

# # Function to make fertilizer recommendations
# def make_recommendations(input_features):
#     # Use the loaded model to make predictions
#     predictions = model.predict(input_features)
#     # Perform any post-processing or formatting of predictions as needed
#     return predictions

# # Streamlit UI
# def main():
#     st.title('Fertilizer Recommendation System')
    
#     # Input fields
#     st.sidebar.header('User Input')
#     temperature = st.sidebar.slider('Temperature', 0, 50, 25)
#     humidity = st.sidebar.slider('Humidity', 0, 100, 50)
#     moisture = st.sidebar.slider('Moisture', 0, 100, 50)
#     soil_type = st.sidebar.selectbox('Soil Type', ['0', '1', '2', '3', '4'])
#     crop_type = st.sidebar.selectbox('Crop Type', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#     nitrogen = st.sidebar.slider('Nitrogen', 0, 100, 50)
#     potassium = st.sidebar.slider('Potassium', 0, 100, 50)
#     phosphorous = st.sidebar.slider('Phosphorous', 0, 100, 50)
    
#     # Collect input features
#     input_features = [[temperature, humidity, moisture, soil_type, crop_type, nitrogen, potassium, phosphorous]]
    
#     # Make recommendations when the user clicks the button
#     if st.sidebar.button('Get Recommendations'):
#         recommendations = make_recommendations(input_features)
#         st.write('Based on the input provided, the recommended fertilizer is:', recommendations)

# if __name__ == '__main__':
#     main()
import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
try:
    with open('/home/shubham09/final_yr_project/fertlizer_recommedation/classifier.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure that 'classifier.pkl' exists in the specified path.")
    st.stop()
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# Function to make fertilizer recommendations
def make_recommendations(input_features):
    # Use the loaded model to make predictions
    predictions = model.predict(input_features)
    # Perform any post-processing or formatting of predictions as needed
    return predictions

def map_to_fertilizer(prediction):
    fertilizer_info = {
       0: {
    "name": "10-26-26",
    "info": "Composition: 10-26-26 fertilizer is a balanced fertilizer suitable for most crops. It contains a balanced ratio of nitrogen, phosphorus, and potassium, providing essential nutrients for plant growth and development.\n"
        
},

1: {
    "name": "14-35-14",
    "info": "Composition: 14-35-14 fertilizer is high in phosphorus, suitable for flowering plants. It contains a high concentration of phosphorus, which promotes strong root development and flowering in plants.\n"
},

2: {
    "name": "17-17-17",
    "info": "Composition: 17-17-17 fertilizer is a balanced fertilizer suitable for general use. It provides a balanced ratio of nitrogen, phosphorus, and potassium, making it suitable for a wide range of crops and soil types.\n"
},

3: {
    "name": "20-20",
    "info": "Composition: 20-20 fertilizer is a balanced fertilizer suitable for general use. It contains equal proportions of nitrogen and potassium, providing essential nutrients for plant growth and development.\n"
},

4: {
    "name": "28-28",
    "info": "Composition: 28-28 fertilizer is a high-nitrogen fertilizer suitable for leafy greens. It contains a high concentration of nitrogen, which promotes lush foliage and green growth in leafy vegetables.\n"
},  

        5: {
    "name": "DAP",
    "info": "Chemical Formula: (NH₄)₂HPO₄\n\n"
            "Chemical Name: Diammonium Phosphate\n\n"
            "Composition: DAP (Diammonium phosphate) is a widely used phosphate fertilizer.\n\n"
            "Usage:\n"
            "DAP is commonly used as a source of phosphorus and nitrogen in agriculture.\n\n"
            "It provides plants with the essential nutrients they need for healthy growth and development.\n\n"
            "Properties:\n"
            "DAP is a white crystalline solid that is highly soluble in water.\n\n"
            "It contains high concentrations of both phosphorus and nitrogen, making it an effective fertilizer for promoting root development and early plant growth."
},
        6: {
    "name": "Urea",
    "info": "Chemical Formula: CO(NH₂)₂\n\n"
            "Chemical Name: Carbamide\n\n"
            "Composition: Urea is a nitrogen-containing organic compound and is the most commonly used nitrogen fertilizer worldwide.\n\n"
            "Usage:\n"
            "Urea is widely used as a nitrogen fertilizer in agriculture to provide plants with the nitrogen they need for growth.\n\n"
            "It's also used in the production of some types of plastics, resins, and adhesives.\n\n"
            "Properties:\n"
            "Urea is a white crystalline solid that is highly soluble in water.\n\n"
            "It has a high nitrogen content, typically around 46% by weight, making it an efficient source of nitrogen for plants."
}
    }
    return fertilizer_info.get(prediction, {"name": "Unknown", "info": "No information available."})

# Streamlit UI
def main():
    st.title('Fertilizer Recommendation System')

    st.image('/home/shubham09/final_yr_project/static/360_F_204287225_4Qn0264AUwyH4RllTK9urzCEOGK14DDy.png', caption='Fertilizer Recommendation System', use_column_width=True)
    
    # Input fields
    st.sidebar.header('User Input')
    temperature = st.sidebar.slider('Temperature', 0, 50, 25)
    humidity = st.sidebar.slider('Humidity', 0, 100, 50)
    moisture = st.sidebar.slider('Moisture', 0, 100, 50)
    soil_type = st.sidebar.selectbox('Soil Type', ['Sandy', 'Loamy', 'Clayey', 'Silty', 'Peaty'])
    crop_type = st.sidebar.selectbox('Crop Type', ['Rice', 'Wheat', 'Maize', 'Barley', 'Oats', 'Potato', 'Sugarcane', 'Cotton', 'Soybean', 'Pulses'])
    nitrogen = st.sidebar.slider('Nitrogen', 0, 100, 50)
    potassium = st.sidebar.slider('Potassium', 0, 100, 50)
    phosphorous = st.sidebar.slider('Phosphorous', 0, 100, 50)
    
    # Convert categorical inputs to numerical representations
    soil_type_mapping = {'Sandy': 0, 'Loamy': 1, 'Clayey': 2, 'Silty': 3, 'Peaty': 4}
    crop_type_mapping = {'Rice': 0, 'Wheat': 1, 'Maize': 2, 'Barley': 3, 'Oats': 4, 'Potato': 5, 'Sugarcane': 6, 'Cotton': 7, 'Soybean': 8, 'Pulses': 9}
    soil_type_numeric = soil_type_mapping[soil_type]
    crop_type_numeric = crop_type_mapping[crop_type]
    
    # Collect input features
    input_features = [[temperature, humidity, moisture, soil_type_numeric, crop_type_numeric, nitrogen, potassium, phosphorous]]
    
    # Make recommendations when the user clicks the button
    if st.sidebar.button('Get Recommendations'):
        predictions = make_recommendations(input_features)
        fertilizer_info = map_to_fertilizer(predictions[0])
        st.markdown(f"Based on the input provided, the recommended fertilizer is    :    **<span style='font-size:xx-large'>{fertilizer_info['name']}</span>**", unsafe_allow_html=True)


        st.write("<h2>Fertilizer Information:</h2>", unsafe_allow_html=True)

        st.write(fertilizer_info["info"])
if __name__ == '__main__':
    main()

