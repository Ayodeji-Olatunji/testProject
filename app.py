import pickle
import streamlit as st

model = pickle.load(open('model.pkl','rb'))

target = {0: 'apple',
 1: 'banana',
 2: 'blackgram',
 3: 'chickpea',
 4: 'coconut',
 5: 'coffee',
 6: 'cotton',
 7: 'grapes',
 8: 'jute',
 9: 'kidneybeans',
 10: 'lentil',
 11: 'maize',
 12: 'mango',
 13: 'mothbeans',
 14: 'mungbean',
 15: 'muskmelon',
 16: 'orange',
 17: 'papaya',
 18: 'pigeonpeas',
 19: 'pomegranate',
 20: 'rice',
 21: 'watermelon'}

def main():
    st.title('Crop Prediction System')
    st.write('This system uses the attributes below to predict the suitable crop for the particular soil.')
    
    Nitrogen = st.text_input('N', placeholder='Nitrogen value')
    Phosphorus = st.text_input('P', placeholder='Phosphorus value')
    Potassium = st.text_input('K', placeholder='Potassium value')
    temp = st.text_input('temperature', placeholder='temperature in degree celsius')
    humidity = st.text_input('humidity', placeholder='relative humidity in %')
    ph = st.text_input('ph', placeholder='pH value of the soil')
    rain = st.text_input('rainfall', placeholder='rainfall in mm')
   

    # Prediction code
    if st.button('Predict'):
        make_prediction = model.predict([[Nitrogen,Phosphorus,Potassium,temp,humidity,ph,rain]])
        output = round(make_prediction[0], 2)
        output = target[output]
        st.success('The suitable crop would be "{}"'.format(output))

if __name__ == '__main__':
    main()