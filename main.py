import streamlit as st
from prep_data import df, X_train, y_train, X, y
from display_func import pred_page, graph_p

# Add sidbar title
st.sidebar.title("Menu")

nav = st.sidebar.radio('Navigator', ('Home', 'Working', 'Prediction', 'Graph', 'Contact Us'))

if nav == 'Prediction':
	st.title("Iris Flower Species Prediction App") 
	pred_page(df, X_train, y_train)

elif nav == 'Home':
    st.image('images/welcome.jpg' , width=500)
    st.title('Welcome to Iris Flower Species Prediction App')
    st.markdown('### This website predicts the species of iris flower with different Machine learning classificaion model on the basis of given data')
    st.subheader('Data Used')
    d_check = st.checkbox('Show data used')
    if d_check:
	    st.dataframe(df, width=1000, height=300)

elif nav == 'Working':
	st.header('Working of This Website')
	st.subheader('Types of Iris Flower Species')
	st.image('images/iris_types.png', width = 500)
	st.subheader('How Species are predicted')
	st.image('images/iris_c.png')

elif nav == 'Graph':
	st.title('Graph for prediction model')
	graph_p(X, y)

else:
	st.balloons()
	st.header('Contact Us')
	st.markdown('''### Name:
	Simran''')
	st.markdown('''### GitHub: [Simran](https://github.com/Simran980?tab=repositories)''')