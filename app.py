from flask import Flask, request, render_template
import requests
from config import NEWS_API_KEY



#Create a flask app
app = Flask(__name__)


# Homepage - Route
# Home / About / Contact / Pricing


@app.route("/")
def index():
    query = request.args.get("query","latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    #print(news_data)


    articles = news_data.get('articles', [])
        
    return render_template("index.html", articles=articles)




if __name__ == "__main__":
    app.run(debug=True)