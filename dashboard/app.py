import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


from dash import dcc, html
from data_loader import DataLoader
from layout import serve_layout


data_loader = DataLoader("../etl_output.csv")
df = data_loader.load_data()

fig_hist = px.histogram(
    df, 
    x="activity_count",
    nbins=50,
    title="Distribution of Activity Counts",
    labels={"activity_count": "Activity Count"},
    template="plotly_white"
)
fig_hist.update_traces(marker_color="#86c5da")
fig_hist.update_layout(xaxis_title="Activity Count", yaxis_title="Frequency")

perf_counts = df["performance_bracket"].value_counts().reset_index()
perf_counts.columns = ["performance_bracket", "num_learners"]
fig_bar = px.bar(
    perf_counts,
    x="performance_bracket",
    y="num_learners",
    title="Learners by Performance Bracket",
    labels={"performance_bracket": "Performance Bracket", "num_learners": "Number of Learners"},
    template="plotly_white",
    color="performance_bracket"
)
fig_bar.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': ['top 1%','top 5%','top 10%','top 25%','others']})

fig_scatter = px.scatter(
    df,
    x="login_count",
    y="average_activity",
    color="performance_bracket",
    title="Average Activity per Login vs. Login Count",
    labels={"login_count": "Login Count", "average_activity": "Average Activity"},
    template="plotly_white"
)
fig_scatter.update_traces(marker=dict(size=8, line=dict(width=1, color='white')))

fig_box = px.box(
    df,
    y="activity_count",
    points="all",
    title="Activity Count",
    labels={"activity_count": "Activity Count"},
    template="plotly_white"
)

fig_violin = px.violin(
    df,
    y="login_count",
    box=True,
    points="all",
    title="Login Count",
    labels={"login_count": "Login Count"},
    template="plotly_white"
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server 
app.layout = serve_layout(fig_hist, fig_bar, fig_scatter, fig_box, fig_violin)

if __name__ == "__main__":
    app.run(debug=True)
