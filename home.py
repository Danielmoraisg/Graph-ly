import streamlit as st 
import pandas as pd
def app(state):
	st.title('This is the homepage')
	st.write('Click the button below to add your dataset and check if your data is correct')
	upload = st.file_uploader('',accept_multiple_files = False)
	if upload is not None:
		state.data = pd.read_csv(upload)
		state.name = upload.name
		st.write(state.data.head())
		st.write(state.data.tail())
	#st.write(df.data)

		