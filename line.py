import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objects import Layout

from plotly.io import write_image
def app(state):
	#configs basicas
    st.title('Line Plot')
    Y = st.selectbox('Column to be mapped on the Y axis',state.data.columns)
    X = st.selectbox('Column to be mapped on the X axis',state.data.columns)
    title = st.text_input("Title",state.name[0:-4])

    #advanced configs
    xtitle = X
    ytitle = Y
    
    if st.checkbox('Advanced'):
    	st.write('Configs avançadas:')
    	ytitle = st.text_input('Y Title', Y)
    	xtitle = st.text_input('X Title', X)



    fig = px.scatter(state.data, x=X, y=Y, title=title,template = 'plotly_white')
    fig.update_traces(mode = 'lines+markers', marker_symbol = 'square')
    fig.update_xaxes(showgrid = True,showline=True, linewidth=2, linecolor='black', title_text = xtitle)
    fig.update_yaxes(showgrid = True,showline=True, linewidth=2, linecolor='black', title_text = ytitle)
    fig.update_layout(title_x=0.5)
    if st.button('WORK IN PROGRESS'):
    	fig.write_html('teste.html')
    else:
    	a = 1
    st.plotly_chart(fig, use_container_width=True)



    #fig = plt.figure()
    #plt.plot(state.data[X],state.data[Y],'b')
    #plt.plot(state.data[X],state.data[Y],'bo')
    #st.pyplot(fig)