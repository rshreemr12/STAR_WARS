import requests
import json
from os import path as osp
import streamlit as st
import constants as cnst
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# About page 
def renderAbout():
    """
    renderAbout() --> takes no arguments 
    
    """
    st.markdown(f"""
    <h2>
    <style>About:
    </style> 
    </h2>
    <img src="https://lumiere-a.akamaihd.net/v1/images/bringhomethebounty_motionhero_dekstop_delivery_992a529b.jpeg?region=0,0,2300,520&width=1536">
    <p> This page uses web based Public <a href="https://swapi.dev/">API</a> </p>
    
    """, unsafe_allow_html=True)
    st.markdown('This streamlit app is developed by Ramyashree (https://www.linkedin.com/in/ramyashree-manchenahalli-rajgopal-1399a9165/)')

    #  alt="starwars.com" style="float:center;width:990px;height:200px;>

def renderForms():
    st.markdown(f"""<h3>Contact for more information: </h3>""", unsafe_allow_html = True)
    username = st.text_input('Name (*)')
    password = st.text_input('Email (*)')
    query = st.text_area("Query")
    st.button('Submit')

# @st.cache(allow_output_mutation = True)
class GetData:
    def __init__(self, url):
        self.url = url
    @property
    def get_data(self):
        frames = []
        while True:
            # Make an API call and store the response in a variable
            response = requests.get(self.url, headers=cnst.headers)
            
            if response.status_code == 200 :
                json_data = response.json()
                print("Next request:", json_data["next"])
                
                if json_data["next"] != None :
                    df1 = pd.DataFrame(json_data["results"])

                    if 'height' in df1.columns:
                        df1.loc[df1[df1.height == 'unknown'].index , 'height'] = 0

                    # Add the frame to the list
                    frames.append(df1)
                    self.url = json_data["next"]
                    
                else:
                    # Combine the list of DataFrames into a single DataFrame
                    single = pd.concat(frames)
                    return single
                
            else:
                return False


# @st.cache()

# class Analysis(GetData):
#     def __init__(self, url):
#         super().__init__(url)
        
#     def data_parsing(self):
#         # accessing member of the other class
#         response = self.get_data()
#         return response
        # if response:
        #     # st.write(response)
        #     print("Successful !")
        #     # return pd.DataFrame(response["results"])
        # else:
        #     st.write("Some Error ocuured while data ")
        #     return False


def people_analysis():
    """ 
    people_analysis() --> takes no arguments 

    """
    selected_analysis = st.selectbox("", cnst.Analysis_types) 
        
    if selected_analysis == "People":
        st.write("List All Charachters")
        
        # with st.spinner(text='In progress'):
        resultdf = GetData(cnst.people_url).get_data
        # resultdf = Analysis(cnst.people_url).data_parsing()

        resultdf.loc[resultdf[resultdf.height == 'unknown'].index , 'average_height'] = None
        resultdf.reset_index(inplace=True)


        resultdf['height'] = resultdf['height'].astype('int32').sort_values()
        
        if st.checkbox("Table view"):
            st.write(resultdf)

        if st.checkbox("Height Analysis"):
            selected_x_axis = st.selectbox("Select Y axis", list(resultdf.columns))
            # Take the results from the API get request above and pass them to streamlit   
    
            st.header("Height Alanysis:")   
            fig = px.bar(resultdf, x=selected_x_axis, y='height', width=960)
            st.plotly_chart(fig)

        if st.checkbox("Visualization"):
            resultdf['height'] = resultdf['height'].astype('str')
            cols = ["name","hair_color","height"]
            fig = px.line(resultdf, x='name', y=cols, width= 960)
            st.plotly_chart(fig)

        if st.checkbox("Guess the Charachter"):
            st.write("What do you know about your favorite charachter ?")
            hair_colour = st.text_area("hair colour?")
            skin_colour = st.text_area("Skin colour?")
            eye_colour  = st.text_area("eye colour?")

            if any( [hair_colour, skin_colour, eye_colour] ):
                resultdf.loc 
                df = resultdf[ (resultdf["hair_color"] == hair_colour) | (resultdf["skin_color"] == skin_colour) | (resultdf["eye_color"] == eye_colour)]

                st.write(df)

# def parse_people():
#     # url = cnst.url+'/people/schema/'
#     url = "https://swapi.dev/api/people/1/"
#     response = Analysis(url).data_parsing()
#     if response.status_code == 200 :
#         return response.json()
#     else:
#         return False

    if selected_analysis == "species":

        def species_analysis():
            """
            species_analysis() --> Take no arguments
            
            """
            resultdf = GetData(cnst.species_url).get_data
            st.write(resultdf)
            return resultdf
        resultdf = species_analysis()

        if st.checkbox("Line chart"):
            # resultdf['average_height'] = resultdf['height'].astype('str')
            cols = ["average_height", "name", "hair_color"]
            fig = px.line(resultdf, x="name", y=["average_height"], width= 960)
            st.plotly_chart(fig)