from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Fruits": ["Apples", "Oranges", "Bananas", "Grapes"],
    "Amount": [10, 15, 7, 20],
    "City": ["New York", "Los Angeles", "Chicago", "Neuchâtel"]
})

# Initialize the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Fruit Sales Dashboard", style={"textAlign": "center"}),

    dcc.Dropdown(
        id='city-dropdown',
        options=[{"label": city, "value": city} for city in df["City"].unique()],
        value="New York",
        placeholder="Select a City",
        style={"width": "50%"}
    ),

    dcc.Graph(id="bar-chart")
])

@app.callback(
    Output("bar-chart", "figure"),
    [Input("city-dropdown", "value")]
)
def update_chart(selected_city):
    filtered_df = df[df["City"] == selected_city]
    fig = px.bar(filtered_df, x="Fruits", y="Amount", title=f"Fruit Sales in {selected_city}")
    return fig

# Run the app
server = app.server  # Expose the server to Render

if __name__ == '__main__':
    app.run_server(debug=True)
