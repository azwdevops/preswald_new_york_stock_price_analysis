📈 NYSE Opening Price Explorer (Preswald App)
This Preswald app showcases an interactive data analysis dashboard for daily NYSE stock prices (2013–2015). It demonstrates filtering, querying, table rendering, and data visualization using Preswald, SQL, and Plotly.

🔍 What the App Does
Loads NYSE stock price data from a CSV file

Filters records where the opening price is between 20 and 50

Displays results in a searchable and scrollable table

Visualizes the filtered opening prices over time

Colors data points based on whether the opening price was above or below $30

🧠 Tech & Tools Used
Preswald — declarative Python data app platform

SQL over CSV — for fast filtering and sorting

Plotly Express — for interactive visualizations

🗂️ Project Structure
bash
Copy
Edit
.
├── app.py              # Main Preswald script
├── data/
│   └── new_york_prices.csv  # Source CSV data
├── preswald.toml       # Preswald config file
└── README.md           # You're here!
🚀 How to Run

You can access the live app here https://preswald.app/pb8256d13

OR 
Login to Preswald

Open https://preswald.com

Upload this repo or paste the code in the editor

Ensure you have the CSV

The file data/new_york_prices.csv should be uploaded alongside your script

Click "Run" or "Publish"

Your dashboard will launch with tables and interactive charts

📊 Sample Visualization
Scatter plot of opening prices by date

Points colored:

🟦 <30

🟥 >30

✅ Skills Demonstrated
Data ingestion and preprocessing

SQL-style querying on local datasets

UI component usage (text, table, chart)

Categorical color mapping using Python logic

Clean, readable, reproducible app design

Feel free to clone or fork this repo to extend this repo add more functionality


