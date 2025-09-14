from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Load the CSV data
    df = pd.read_csv('crimes_against_women_2001-2014.csv')  # Replace with your CSV file path
    
    # Example plot
    fig = px.bar(df, x='State', y='Crime Count', title='Crime in Indian States')
    graph_html = fig.to_html(full_html=False)

    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
