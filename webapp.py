import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#from jupyter_dash import JupyterDash
from dash_extensions import Lottie       # pip install dash-extensions
from outline import *
#from dashapp import *
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from whitenoise import WhiteNoise


from scipy.spatial import distance_matrix
from scipy.spatial.distance import cdist

#cluster_label_df = pd.read_csv(r'assets\cluster_label_df.csv')

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.LUX], meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
#server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

df = pd.read_csv('August23_32.csv')
df = df[df['year'] >= 2015]
df = df.reset_index(drop = True)
df = df.drop(df[df['release_date'] == 'Release: 01/01/1970'].index)
df = df.reset_index(drop = True)

df.drop(df.index[df['release_date'] == "Release: N/A"], inplace = True)
df = df[pd.notnull(df['release_date'])]
df = df.reset_index(drop = True)

umap_2d_df = pd.read_csv('data/projct_2d.csv')
umap_3d_df = pd.read_csv('data/projct_3d.csv')


df['biannual'] = ''
df['triannual'] = ''
df['monthly'] = ''
#for i, row in df.iterrows():
#    month, data, year_value = row['release_date'].split()[1].split('/')
#    if month in ['01','02','03','04','05','06']:
#        monthly_date = '{}-{}'.format(year_value, month)
#        biannual_date = '{}-{}'.format(year_value, '01')
#        if month in ['01','02','03']:
#            triannual_date = '{}-{}'.format(year_value, '01')
#        else:
#            triannual_date = '{}-{}'.format(year_value, '03')
#    else:
#        monthly_date = '{}-{}'.format(year_value, month)
#        biannual_date = '{}-{}'.format(year_value, '06')
#        if month in ['07','08','09']:
#            triannual_date = '{}-{}'.format(year_value, '06')
#        else:
#            triannual_date = '{}-{}'.format(year_value, '09')
#        
#    
#    df.at[i, 'biannual'] = biannual_date
#    df.at[i, 'triannual'] = triannual_date
for i, row in df.iterrows():
    try: 
        month, data, year_value = row['release_date'].split()[1].split('/')
        if month in ['01','02','03','04','05','06']:
            monthly_date = '{}-{}'.format(year_value, month)
            biannual_date = '{}-{}'.format(year_value, '01')
            if month in ['01','02','03']:
                triannual_date = '{}-{}'.format(year_value, '01')
            else:
                triannual_date = '{}-{}'.format(year_value, '03')
        else:
            monthly_date = '{}-{}'.format(year_value, month)
            biannual_date = '{}-{}'.format(year_value, '06')
            if month in ['07','08','09']:
                triannual_date = '{}-{}'.format(year_value, '06')
            else:
                triannual_date = '{}-{}'.format(year_value, '09')
            #new_date = int(new_date)
    except:
        biannual_date = row['release_date']
        triannual_date = row['release_date']
        
    finally:
        df.at[i, 'biannual'] = biannual_date
        df.at[i, 'triannual'] = triannual_date
        df.at[i, 'monthly'] = monthly_date

df_grouped = df.groupby('triannual')
per_year = df_grouped['image_fileName'].count()
per_year_mean = df_grouped['image_fileName'].count().mean()
per_year_std = df_grouped['image_fileName'].count().std()
per_year_max = df_grouped['image_fileName'].count().max()


filtered_total = df.groupby('triannual').filter(lambda x: x['image_fileName'].count() > per_year_max - 3.5*per_year_std)
filtered_total.reset_index(drop=True, inplace=True) # reset index
filtered_grouped_total = filtered_total.groupby('triannual')

nike_df = df[df["brand"] == "Nike"]
adidas_df = df[df["brand"] == "adidas"]
jordan_df = df[df["brand"] == "Jordan"]

grouped_nike = nike_df.groupby(['triannual'])
grouped_adidas = adidas_df.groupby(['triannual'])
grouped_jordan = jordan_df.groupby(['triannual'])

nike_count_per_year_mean = grouped_nike['image_fileName'].count().mean()
nike_count_per_year_std = grouped_nike['image_fileName'].count().std()
nike_count_per_year_max = grouped_nike['image_fileName'].count().max()

adidas_count_per_year_mean = grouped_adidas['image_fileName'].count().mean()
adidas_count_per_year_std = grouped_adidas['image_fileName'].count().std()
adidas_count_per_year_max = grouped_adidas['image_fileName'].count().max()

jordan_count_per_year_mean = grouped_jordan['image_fileName'].count().mean()
jordan_count_per_year_std = grouped_jordan['image_fileName'].count().std()
jordan_count_per_year_max = grouped_jordan['image_fileName'].count().max()

filtered_nike = nike_df.groupby('triannual').filter(lambda x: x['image_fileName'].count() > nike_count_per_year_max - 3.25*nike_count_per_year_std)
filtered_nike.reset_index(drop=True, inplace=True) # reset index
filtered_grouped_nike = filtered_nike.groupby('triannual')

filtered_jordan = jordan_df.groupby('triannual').filter(lambda x: x['image_fileName'].count() > jordan_count_per_year_max - 3.2*jordan_count_per_year_std)
filtered_jordan.reset_index(drop=True, inplace=True) # reset index
filtered_grouped_jordan = filtered_jordan.groupby('triannual')


filtered_adidas = adidas_df.groupby('triannual').filter(lambda x: x['image_fileName'].count() > adidas_count_per_year_max - 2.7*adidas_count_per_year_std)
filtered_adidas.reset_index(drop=True, inplace=True) # reset index
filtered_grouped_adidas = filtered_adidas.groupby('triannual')







#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheet=[dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets = [dbc.themes.LUX], meta_tags=[{'name': 'viewport',
#                            'content': 'width=device-width, initial-scale=1.0'}])

biggest_brands = ['Nike', 'Adidas', 'jordan']

app.layout = dbc.Container([
    
#first_row,
#first_row_modified,


#orig10, #best one


#orig,
#orig2,
#orig3,

#second_row,

html.Hr(),

third,
fourth,
html.Hr(),
fifth,
sixth_2,
#seventh,
#eightz,
#cardz,
#ninth,
   
], fluid=True)


@app.callback(
    Output('brightness-plot','figure'),
    Input('dropdown-brightness','value'),
    #prevent_initial_call=True
)
def update_my_graph(value):
    #dff = df[df["brand"].isin(list(value))]
    if value == "Nike":
        df_to_use = filtered_grouped_nike['mean_v'].median()
    elif value == "Jordan":
        df_to_use = filtered_grouped_jordan['mean_v'].median()
    elif value == "Adidas":
        df_to_use = filtered_grouped_adidas['mean_v'].median()
    

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.01)

    fig.append_trace(go.Scatter(
        x=df_to_use.index,
        y=df_to_use,
        mode='lines+markers',
    ), row=1, col=1)

    fig.append_trace(go.Scatter(
        x=filtered_grouped_total['mean_v'].median().index,
        y=filtered_grouped_total['mean_v'].median(),
        mode='lines+markers',
    ), row=2, col=1)


    fig.update_yaxes(title_text=value, row=1, col=1)
    fig.update_yaxes(title_text="All_Brands", row=2, col=1)
    #fig.update_yaxes(title_text="Adidas", row=3, col=1)
    #fig.update_yaxes(title_text="All-Brands", row=4, col=1)
    fig.update_layout(showlegend= False, title_text="Seasonal variations in {0}".format(value), template='plotly_white', title_x=0.5)



    return fig

# def update_my_graph(value):
#     #dff = df[df["brand"].isin(list(value))]
#     if value == "Brightness":
#         feature = 'mean_v'
#     elif value == "Hue":
#         feature = 'mean_h'
#     elif value == "Saturation":
#         feature = 'mean_s'
    

#     fig = make_subplots(rows=4, cols=1, shared_xaxes=True,
#                         vertical_spacing=0.01, print_grid=True)

#     fig.append_trace(go.Scatter(
#         x=filtered_grouped_nike[feature].median().index,
#         y=filtered_grouped_nike[feature].median(),
#         mode='lines+markers',
#     ), row=1, col=1)

#     fig.append_trace(go.Scatter(
#         x=filtered_grouped_jordan[feature].median().index,
#         y=filtered_grouped_jordan[feature].median(),
#         mode='lines+markers',
#     ), row=2, col=1)

#     fig.append_trace(go.Scatter(
#         x=filtered_grouped_adidas[feature].median().index,
#         y=filtered_grouped_adidas[feature].median(),
#         mode='lines+markers',
#     ), row=3, col=1)

#     fig.append_trace(go.Scatter(
#         x=filtered_grouped_total[feature].median().index,
#         y=filtered_grouped_total[feature].median(),
#         mode='lines+markers',
#     ), row=4, col=1)

#     fig.update_yaxes(title_text="Nike", row=1, col=1)
#     fig.update_yaxes(title_text="Jordan", row=2, col=1)
#     fig.update_yaxes(title_text="Adidas", row=3, col=1)
#     fig.update_yaxes(title_text="All-Brands", row=4, col=1)
#     fig.update_layout(showlegend= False, title_text="Seasonal variations in {0}".format(value), template='plotly_white', title_x=0.5)



#     return fig


#UMAP
@app.callback(
    Output('umAp-2d','figure'),
    Input('radios','value'),
    #prevent_initial_call=True
)



#@app.callback
#(
#   Output('comp-plot-1','figure'),
#   Input('radios','value') 
#)
def update_umap(value):
    #print(type(value))
    if value == 'umap_2d_df':
        umap_fig_2d = px.scatter(umap_2d_df, x='0', y='1',
        #title='2d_UMAP 100D -> 2D',
        width=800,                  # figure width in pixels
        height=800,
        color=umap_2d_df['cl_label'],
        color_discrete_sequence=px.colors.qualitative.Plotly,
        #color_continuous_scale=px.colors.sequential.Viridis
        template='plotly_white',
        opacity = 0.7)
        
        umap_fig_2d.update_traces(marker_size=1.8)
        return umap_fig_2d
    
    elif value == 'umap_3d_df':
        umap_fig_3d = px.scatter_3d(umap_3d_df, x='0', y='1', z='2',
        color=umap_3d_df['cl_label'], 
        #labels={'color': 'cluster_label'},
        width = 800, height = 800,
        color_discrete_sequence=px.colors.qualitative.Plotly, 
        template='plotly_white',)
        umap_fig_3d.update_traces(marker_size=1.7)
        return umap_fig_3d




#HSV cosine distance between men and women shoes
@app.callback(
    Output('comp-plot-1', 'figure'),
    Input('dropdown-comp-1', 'value')
)
def update_HSV_cosine_distance(value):
    
    #df = df[df['gender'].isin(['men', 'women'])]
    nike_df1 = nike_df.loc[:, 'mean_b':'ent_grey']
    nike_df1 = nike_df1.apply(pd.to_numeric, errors = 'raise')

    nike_df2 = nike_df.loc[:, 'B_hist_0':'R_hist_31'] #127
    nike_df2 = nike_df2.apply(pd.to_numeric, errors = 'raise')

    dff = pd.concat([nike_df1, nike_df2], axis=1, join='inner')

    dff['brand'] = nike_df['brand']
    dff['year'] = nike_df['year']
    dff['release_date'] = nike_df['release_date']
    dff['gender'] = nike_df['gender']
    dff['biannual'] = nike_df['biannual']
    dff['triannual'] = nike_df['triannual']
    dff['monthly'] = nike_df['monthly']

    if value == 'Brightness':
        features_to_use = ['mean_v','std_v']
    elif value =='Hue':
        features_to_use = ['mean_h','std_h']
    elif value =='Saturation':
        features_to_use = ['mean_s','std_s']
    
    result = dff.groupby(['triannual']).apply(lambda x: pairwise_average_distance(x, features_to_use))

    fig_2 = make_subplots(rows=1, cols=1, vertical_spacing=0.01)

    fig_2.append_trace(go.Scatter(
        x=result.index,
        y=result,
        mode='lines+markers',
    ), row=1, col=1)
    fig_2.append_trace(go.Scatter(
        x=result.rolling(window=4, min_periods=3).mean().index,
        y=result.rolling(window=4, min_periods=3).mean(),
        mode='lines+markers',
    ), row=1, col=1)
    
    fig_2.update_yaxes(title_text="Euclidean Distance", row=1, col=1)
    fig_2.update_layout(showlegend= False, title_text="Mean gap in men and women sneakers({0})".format(value), template='plotly_white', title_x=0.5)



    return fig_2



@app.callback(
    Output('comp-plot-2', 'figure'),
    Input('dropdown-comp-2', 'value')
)
def update_HSVRGB_cosine_distance(value):
    
    #df = df[df['gender'].isin(['men', 'women'])]
    nike_df1 = nike_df.loc[:, 'mean_b':'ent_grey']
    nike_df1 = nike_df1.apply(pd.to_numeric, errors = 'raise')

    nike_df2 = nike_df.loc[:, 'B_hist_0':'R_hist_31']#127
    nike_df2 = nike_df2.apply(pd.to_numeric, errors = 'raise')

    dff = pd.concat([nike_df1, nike_df2], axis=1, join='inner')

    dff['brand'] = nike_df['brand']
    dff['year'] = nike_df['year']
    dff['release_date'] = nike_df['release_date']
    dff['gender'] = nike_df['gender']
    dff['biannual'] = nike_df['biannual']
    dff['triannual'] = nike_df['triannual']
    dff['monthly'] = nike_df['monthly']

    'HSL', 'RGB', 'RGBHSL'
    if value == 'HSL':
        features_to_use = ['mean_h', 'std_v']
    elif value =='RGB':
        features_to_use = ['mean_b','std_r']
    elif value =='RGBHSL':
        features_to_use = ['mean_b','std_v']
    elif value =='All_color_features':
        features_to_use = ['mean_b', 'R_hist_31'] #127
    
    result = dff.groupby(['triannual']).apply(lambda x: pairwise_cosine_distance(x, features_to_use))

    fig_3 = make_subplots(rows=1, cols=1, vertical_spacing=0.01)

    fig_3.append_trace(go.Scatter(
        x=result.index,
        y=result,
        mode='lines+markers',
    ), row=1, col=1)
    fig_3.append_trace(go.Scatter(
        x=result.rolling(window=4, min_periods=3).mean().index,
        y=result.rolling(window=4, min_periods=3).mean(),
        mode='lines+markers',
    ), row=1, col=1)
    
    fig_3.update_yaxes(title_text="Cosine Distance", row=1, col=1)
    fig_3.update_layout(showlegend= True, title_text="Mean gap in men and women sneakers({0})".format(value), template='plotly_white', title_x=0.5)



    return fig_3





def pairwise_cosine_distance(gr,features_to_use):

    men_df = gr[gr['gender']=='men']
    men_df = men_df.loc[:,features_to_use[0]:features_to_use[-1]]
    #men_df = men_df[features_to_use]
    #print(men_df)
    
    
    women_df = gr[gr['gender']=='women']
    women_df = men_df.loc[:,features_to_use[0]:features_to_use[-1]]
    #women_df = women_df.loc[:,'mean_b':'std_r']
    #women_df = women_df[features_to_use]

    res = cdist(men_df, women_df, metric = 'cosine').mean()
    return res

def pairwise_average_distance(gr, features_to_use):
    men_df = gr[gr['gender']=='men']
    #men_df = men_df.loc[:,'mean_b':'std_r']
    men_df = men_df[features_to_use]


    women_df = gr[gr['gender']=='women']
    #women_df = women_df.loc[:,'mean_b':'std_r']
    women_df = women_df[features_to_use]
    
    res = distance_matrix(men_df, women_df, p=2).mean()
    #didtances.append(res)
    return res


if __name__=='__main__':
    app.run_server()
