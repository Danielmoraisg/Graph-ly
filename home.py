import streamlit as st 
import pandas as pd
def app(state):
	st.title('Creating Plots')
	st.write('Click the button below to add your dataset and check if your data is correct')
	upload = st.file_uploader('',accept_multiple_files = False)
	if upload is not None:
		state.name = upload.name
		if state.name.split('.')[1] == 'xlsx' or state.name.split('.')[1] == 'xls' :
			#state.data = pd.read_excel(upload)
			data = upload.read()
			state.data = pd.read_excel(data)
			#st.write(pd.read_excel(state.data))
			st.write(state.data.head())
			st.write(state.data.tail())

		elif state.name.split('.')[1] == 'csv' :
			state.data = pd.read_csv(upload)
			st.write(state.data.head())
			st.write(state.data.tail())
		upload.seek(0)
	#st.write(df.data)

		