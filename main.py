import pandas as pd
import altair as alt

from data_processing import derive_vars

fname_blood = 'data/Blood sugars - Data.csv'

# Get data
df = pd.read_csv(fname_blood)

# Derived variables
df = derive_vars(df)


brush = alt.selection(type='interval', encodings=['x'])
single_nearest = alt.selection_single(on='mouseover', nearest=True)

tooltip = ['datetime_:Q', alt.Tooltip('notes')]

base = alt.Chart(df).mark_line().encode(
    x = 'date:T',
    y = 'level:Q',

).properties(width=800)

upper = base.encode(
    x = alt.X('date:T', scale=alt.Scale(domain=brush)),
    tooltip=tooltip


).add_selection(single_nearest)

lower = base.properties(
    height=60
).add_selection(brush)

full_chart = upper & lower
full_chart.show()