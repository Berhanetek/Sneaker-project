import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from whitenoise import WhiteNoise
#from jupyter_dash import JupyterDash
#from dash_extensions import Lottie       # pip install dash-extensions
#from dashapp import *
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

big_brands = ['Nike', 'Adidas', 'jordan', 'Vans']


# first_row_modified = html.Div([
#     html.Nav([html.Div([
            
#             dbc.Col([
#           html.Img(src = app.get_asset_url('data_science_medium_logo-768x182-removebg-preview.png'),
#                     height = 'auto',
#                     width = 'auto')
#         ], xs=12, sm=12, md=10, lg=6, xl=6),
            
#             ],
#             className = 'col-2',
#             style = {
#                     'align-items': 'center',
#                     'padding-top' : '1%',
#                     'height' : 'auto'})])

        
        
#         ],
        
        
#         className = 'row',
#         style = {'height' : '4%',
#                 }
#         )



# colors = {
#     'background': '#2a434d',
#     'text': '#7FDBFF'
# }
# # style={
# #         'textAlign': 'center',
# #         'color': colors['text']
# #     }

# orig10 = html.Div([dbc.Row([    
#         #+++++++++++++++++++++++++++++#
#         #1st column
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='jordans_02.gif')
#             ],className='mb-2 mw-10 mh-10'), #mb-2 (margin-bottom-2)adds space on the bottom of each row
#             #ketach same column wust lela card binor would have worked
#         ], width=2, xs=12, sm=12, md=10, lg=2, xl=2, className = 'mw-2 mh-2'),
        
#         #+++++++++++++++++++++++++++++#
#         #2nd column
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='data_science_medium_logo-768x182.png')
#             ],className='mb-2'), #mb-2 adds space on the bottom of each row
#         ], width=6, xs=12, sm=12, md=10, lg=6, xl=6),
        
#     ],className='mb-2 mt-2  mw-10 mh-10', justify = 'center')], style={'backgroundColor': colors['background']} )







# orig = dbc.Row([    
#         #+++++++++++++++++++++++++++++#
#         #1st column
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='jordans_02.gif')
#             ],className='mb-2 mw-10 mh-10'), #mb-2 (margin-bottom-2)adds space on the bottom of each row
#             #ketach same column wust lela card binor would have worked
#         ], width=2, xs=12, sm=12, md=10, lg=2, xl=2, className = 'mw-2 mh-2'),
        
#         #+++++++++++++++++++++++++++++#
#         #2nd column
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='data_science_medium_logo-768x182.png')
#             ],className='mb-2'), #mb-2 adds space on the bottom of each row
#         ], width=6, xs=12, sm=12, md=10, lg=6, xl=6),
        
#     ],className='mb-2 mt-2  mw-10 mh-10', justify = 'center')



# orig2 = dbc.Row([
    
#     dbc.Col([
#     dbc.Navbar 
#     ([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='jordans_02.gif')
#             ],className='mb-2 mw-10 mh-10'), #mb-2 (margin-bottom-2)adds space on the bottom of each row
#             #ketach same column wust lela card binor would have worked
#         ], width=2, xs=12, sm=12, md=10, lg=2, xl=2, className = 'ml-5 mw-2 mh-2'),
        
#         #+++++++++++++++++++++++++++++#
#         #2nd column
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='data_science_medium_logo-768x182.png')
#             ],className='mb-2'), #mb-2 adds space on the bottom of each row
#         ], width=6, xs=12, sm=12, md=10, lg=6, xl=6)
        
#     ],
#     color="dark",
#     dark=True,
#     light = False,
#     expand = 'md'
#     ), ], width={'size':12})


# ], justify = 'center')

# orig3 = dbc.Row([
#     dbc.Navbar 
#     ([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='jordans_02.gif')
#             ],className='mb-2 mw-10 mh-10'), #mb-2 (margin-bottom-2)adds space on the bottom of each row
#             #ketach same column wust lela card binor would have worked
#         ], width=2, xs=12, sm=12, md=10, lg=2, xl=2, className = 'mw-2 mh-2'),
        
#         #+++++++++++++++++++++++++++++#
#         #2nd column
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardImg(src='data_science_medium_logo-768x182.png')
#             ],className='mb-2'), #mb-2 adds space on the bottom of each row
#         ], width=6, xs=12, sm=12, md=10, lg=6, xl=6)
        
#     ],
#     color="dark",
#     dark=True,
#     light = False,
#     expand = 'md'
#     )


# ], justify = 'center')


# first_row = html.Div([

#         html.Div([], className = 'col-2'), #Same as img width, allowing to have the title centrally aligned

#         #html.Div([
#         #    html.H1(children='Performance Dashboard',
#         #            style = {'textAlign' : 'center'}
#         #    )],
#         #    className='col-8',
#         #    style = {'padding-top' : '1%'}
#         #),

#         html.Div([
            
#             dbc.Col([
#           html.Img(src = app.get_asset_url('data_science_medium_logo-768x182-removebg-preview.png'),
#                     height = 'auto',
#                     width = 'auto')
#         ], xs=12, sm=12, md=10, lg=6, xl=6),
            
#             #html.Img(
#             #        src = app.get_asset_url('data_science_medium_logo-768x182-removebg-preview.png'),
#             #        height = 'auto',
#             #        width = 'auto')
#             ],
#             className = 'col-2',
#             style = {
#                     'align-items': 'center',
#                     'padding-top' : '1%',
#                     'height' : 'auto'})
        
        

#         ],
        
        
#         className = 'row',
#         style = {'height' : '4%',
#                 }
#         )
    
# second_row = dbc.Navbar(
#     [
#        dbc.Row([    
#         #+++++++++++++++++++++++++++++#
#         #1st column
#         dbc.Col([
            
#            # dbc.Card([
#            #     #dbc.CardImg(src='/assets/jordans_02.gif')
#            #     html.Img(src = app.get_asset_url('cropped-logo4-removebg-preview.png'),
#            #         height = 'auto',
#            #         width = 'auto')
#            # ],className='mb-2')# mw-10 mh-10'), #mb-2 (margin-bottom-2)adds space on the bottom of each row
#             #ketach same column wust lela card binor would have worked
#         ], xs=12, sm=12, md=10, lg=2, xl=2, className = 'mw-2 mh-2'),
        
#         #+++++++++++++++++++++++++++++#
#         #2nd column
#         dbc.Col([
            
#             html.Img(src = app.get_asset_url('data_science_medium_logo-768x182-removebg-preview.png'),
#                     height = 'auto',
#                     width = 'auto')
            
#             #dbc.Card([
#             #    dbc.CardImg(src='/assets/data_science_medium_logo-768x182-removebg-preview.png')
#             #],className='mb-2'), #mb-2 adds space on the bottom of each row
#         ], xs=12, sm=12, md=10, lg=6, xl=6),
        
#            dbc.Col([
            
#             html.Img(src = app.get_asset_url('giff6.gif'),
#                     height = '36',
#                     width = '36')
            
#             #dbc.Card([
#             #    dbc.CardImg(src='/assets/data_science_medium_logo-768x182-removebg-preview.png')
#             #],className='mb-2'), #mb-2 adds space on the bottom of each row
#         ], xs=12, sm=12, md=10, lg=6, xl=6),
        
#     ],className='mb-2 mt-2', justify = 'center', align = 'center'), 
#     ],
#     color="dark",
#     dark=True,

# )

third = dbc.Row([
        dbc.Col([html.H1("Exploring evolution of Sneaker Design at scale using Contrastive learning", style={ "font-size": 40},
                        className='text-center card-text text-capitalize font-weight-bold mb-4'),
                html.H3("Shaun, Hyunho, Lev, Mia",
                        className='card-text text-center text-capitalize font-weight-bold mb-4'),
                 html.P('our paper for the first time applies data science methods to a new research domain – analysis of product design evolution over a long historical period. Analyzing group interactions (as studied by social science) cannot always explain trends comprehensively: formal and aesthetic features and their evolution allow us to get additional insights about the evolutionary success of a product or cultural artifact, since human or consumer behavior is also shaped by formal taste. In our work, we apply state-of-the-art deep learning methods to a dataset of 23,492 sneakers models from 92 brands released in 2001–2020. To represent the sneaker designs in our dataset, we set up three embedding models with three attributes, shape, color, and segment.' ,className='text-center' ,
        
    )
       ], xs=12, sm=12, md=12, lg=12, xl=10)
        
    ],
    className='mb-2 mt-2', justify = 'center')

fourth = dbc.Row([
        dbc.Col([
            dcc.Graph(id='brightness-plot', figure={}), #style={'width': '60vh', 'height': '60vh'}),
            dcc.Dropdown(id='dropdown-brightness', multi=False, value='Nike',
                         options=[{'label':x, 'value':x}
                                  for x in ['Nike', 'Jordan', 'Adidas']],
                         ),
            
        ], width = 4, xs=12, sm=12, md=12, lg=5, xl=5),
        dbc.Col([
            dcc.Graph(id='comp-plot-1', figure={}),
            dcc.Dropdown(id='dropdown-comp-1', multi=False, value='Hue',
                         options=[{'label':x, 'value':x}
                                  for x in ['Hue', 'Saturation', 'Brightness']],     
                         ),
            dcc.Graph(id='comp-plot-2', figure={}),
            dcc.Dropdown(id='dropdown-comp-2', multi=False, value='HSL',
                         options=[{'label':x, 'value':x}
                                  for x in ['HSL', 'RGB', 'RGBHSL', 'All_color_features']],
                         ),
            
        ], width = 4, xs=12, sm=12, md=12, lg=5, xl=5)
        
    ],className='mb-2 mt-2', justify = 'center')

fifth =  dbc.Row([
        html.Br(),
        dbc.Col([
                 html.P('We tested the quality of clustering via visualizing the embedding on a reduced 2-dim UMAP plane after clustering (see Figure 2). The red dots are detected centroids by clusters; the corresponding sneaker images demonstrate that the sneaker models are well separated after embedding, i.e., for each centroid sneaker model, it represents low/high in shape, light/dark in color, and unique functional category like soccer shoes. We also qualitatively confirmed, by manually examining the sneakers belonging to each cluster, that similar color distribution and complexity of the segmentation had been captured for the samples within each cluster. We then run a k-means clustering and test the quality of clustering via visualizing the embedding on a reduced two-dimensional UMAP plane after clustering. We qualitatively investigate images within clusters and confirm that the sneaker models are successfully clustered based on their shape, color, and segmentation patterns. ' ,className='text-center' ,  
        
    )
       ], xs=12, sm=12, md=12, lg=12, xl=10),
       
       html.Br(),
        
    ],
    className='mb-2 mt-2', justify = 'center')

sixth = dbc.Row([
        dbc.Col([dbc.Card([
            
                dbc.CardHeader([html.H1("2D UMAP of sneaker models",
                        className='text-center text-capitalize font-weight-bold mb-4')],),


                dbc.CardBody([
                    dcc.Graph(id='umap-2d', figure={}),
                ])
            ],),], width = 4, xs=12, sm=12, md=12, lg=5, xl=5),
        
        
        dbc.Col([dbc.Card([
                
                #maybe use multiple tabs to display 2d and 3d here.
                dbc.CardHeader([html.H1("3D UMAP of sneaker models",
                        className='text-center text-capitalize font-weight-bold mb-4')],),

                dbc.CardBody([
                    dcc.Graph(id='umap-3d', figure={}),
                ])
            ]),], width = 4, xs=12, sm=12, md=12, lg=5, xl=5)
        
        
    ],className='mb-2 mt-2', justify = 'center')


button_group = html.Div(
    [
        dbc.RadioItems(
            id="radios",
            className="btn-group",
            labelClassName="btn btn-secondary",
            labelCheckedClassName="active",
            options=[
                {"label": "2D UMAP", "value": 'umap_2d_df'},
                {"label": "3D UMAP", "value": 'umap_3d_df'},
                #{"label": "Option 3", "value": 3},
            ],
            value='umap_2d_df',
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)


sixth_2 = dbc.Row([
        dbc.Col([button_group, 
                dbc.Card([
            
                dbc.CardHeader([html.H1("Sneakers' shape embeddings",
                        className='text-center text-capitalize font-weight-bold mb-4')],),


                dbc.CardBody([
                    dcc.Graph(id='umAp-2d', figure={}),
                ])
            ],), ], width = 4, xs=12, sm=12, md=12, lg=5, xl=5),

        
    ],className='mb-2 mt-2', justify = 'center')


#app_tabs = dbc.Tabs(
#            [
#                dbc.Tab(label="2D UMAP", tab_id="2D_UMAP", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
#                dbc.Tab(label="3D UMAP", tab_id="3D_UMAP", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
#                
#            ],
#            id="tabs",
#            active_tab="2D_UMAP",
#        )


#seventh = dbc.Row([dbc.Col([app_tabs], width=12)], className="mb-3"),


# cardz = dbc.Card(
#     [
#         dbc.CardHeader(
#             dbc.Tabs(
#                 [
#                     dbc.Tab(label="Tab 1", tab_id="tab-1"),
#                     dbc.Tab(label="Tab 2", tab_id="tab-2"),
#                 ],
#                 id="card-tabs",
#                 card=True,
#                 active_tab="tab-1",
#             )
#         ),
#         dbc.CardBody(html.P(id="cardz-content", className="card-text")),
#     ]
# )




# #eighth = dbc.Row(dbc.Col(cardz, width=12), className="mb-3"),

# ninth = html.Div([cardz], className = 'col-2',
#             style = {
#                     'align-items': 'center',
#                     'padding-top' : '1%',
#                     'height' : 'auto'})