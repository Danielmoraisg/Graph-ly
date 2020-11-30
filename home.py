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
			excel = pd.ExcelFile(data)
			sheet = st.selectbox('Sheet from excel file to be used',excel.sheet_names)
			state.data = pd.read_excel(data, sheet_name = sheet)
			#st.write(pd.read_excel(state.data))
			st.write(state.data.head())
			st.write(state.data.tail())

		elif state.name.split('.')[1] == 'csv' :
			state.data = pd.read_csv(upload)
			st.write(state.data.head())
			st.write(state.data.tail())
		upload.seek(0)
	#st.write(df.data)

		