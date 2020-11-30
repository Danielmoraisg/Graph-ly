import streamlit as st 
import pandas as pd
import os
import base64
def app(state):
	st.title('Creating Plots')
	st.write('Click the button below to add your dataset and check if your data is correct')
	upload = st.file_uploader('',accept_multiple_files = False)

	if st.checkbox('Download templates'):
		def get_binary_file_downloader_html(bin_file, file_label='File'):
			with open(bin_file, 'rb') as f:
				data = f.read()
			bin_str = base64.b64encode(data).decode()
			href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
			return(href)
		st.markdown(get_binary_file_downloader_html('template.xlsx', 'Excel template'), unsafe_allow_html=True)
		st.markdown(get_binary_file_downloader_html('template.csv', 'Comma separated values template'), unsafe_allow_html=True)
		st.markdown(get_binary_file_downloader_html('template.txt', 'Text file template'), unsafe_allow_html=True)
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

		