# -*- coding: utf-8 -*-
"""
Module Name : <app.py>
author      : <'Ramyashree M R'>
use         : <streamlit run app.py>
Module Description : <This module will import supporting modules to run the application 
on the web browser.  >
"""


import utilities as utils
import constants as cnst
import streamlit as st


#set application name
st.set_page_config(page_title="Star Wars",layout='wide')

# background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()}

# set the background gif
st.markdown(
         f"""
         <style>
         .reportview-container {{
             background: url("https://media0.giphy.com/media/l3q2RgN7WUjeUUXm0/giphy.gif?cid=ecf05e47hgzhm88ddae9svsotzaasxglpbqu7eyx56r1pw7e&rid=giphy.gif&ct=g")
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


# Set Title of the page
st.markdown(
    f"""
    <h1 style='text-align: center; 
    color: White; padding-top: 0px; 
    font-size:60px; 
    font-family: Avenir-Roman,sans-serif;
    box-shadow: 5px 5px blue, 10px 10px red, 15px 15px green;
    '>STAR WARS</h1>"""
    , unsafe_allow_html=True)


# Functionality code starts from here
if __name__ == "__main__":
    st.sidebar.button("Home")
    selectType = st.sidebar.selectbox("Select ", cnst.portfolioTypes)

    if selectType == "About":
        utils.renderAbout()

    elif selectType == "Contact":
        utils.renderForms()

    elif selectType == "Analysis":
        st.markdown(f"""
        <h4 style='text-align: center;
        border: 3px 3px blue; 
        font-size:20px; '>
        A People resource is an individual person or character within the Star Wars universe
        </h4>""", unsafe_allow_html=True)
        utils.people_analysis()





