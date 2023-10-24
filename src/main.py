from dash import Dash, html, dcc
from dash import dash_table
import plotly.express as px
import pandas as pd

import config


app = Dash(__name__)

print(config.zipfilename())
print(config.csvfile())
df = config.read_df_zip()

app.layout = dash_table.DataTable(df.to_dict('records'))
                      
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

