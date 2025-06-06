# 1. Load the dataset
from preswald import connect, get_df, table

connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/new_york_prices.csv")  # Load data

# 2. Query or manipulate the data
from preswald import query

# we get the date, open, and close columns from our financial data, limiting to 500 to avoid to much overload currently

# we cast the open to ensure the > comparison can be done
sql = "SELECT date, open, close FROM data/new_york_prices.csv WHERE CAST(open as REAL) BETWEEN 20 AND 50 ORDER BY date LIMIT 500"

filtered_df = query(sql, "data/new_york_prices.csv")


# 3. Build an interactive UI
from preswald import table, text

text("# 2013 - 2015 NYSE daily stock prices where opening price was between 20 and 50, showing 500 results")

# we show the table of the filtered data
table(filtered_df, title="Filtered Data")

# 4. Create a visualization
from preswald import plotly
import plotly.express as px

# we want to color the prices differently for example those below 30 one color and those above 30 a different color
def get_range_label(value):
    if value < 30:
        return "<30"
    else:
        return ">30"
        
# we apply the range here
filtered_df["open_range"] = filtered_df["open"].astype(float).apply(get_range_label)

fig = px.scatter(filtered_df, x="date", y="open", title='NYSE opening stock prices (2013 - 2015) where  opening prices was between 20 and 50', color='open_range')
plotly(fig)








