from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv("csr_fy_2018_19.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

df["amount_spent"] = pd.to_numeric(df["amount_spent"], errors="coerce")
df["project_amount_outlay"] = pd.to_numeric(df["project_amount_outlay"], errors="coerce")

@app.route("/")
def home():
    return "Backend running"

@app.route("/answers")
def answers():
    df["utilisation_rate"] = df["amount_spent"] / df["project_amount_outlay"]

    answer1 = df[
        (df["development_sector"].str.lower() == "education") &
        (df["state"].str.lower() == "karnataka")
    ].loc[lambda x: x["amount_spent"].idxmax(), "company_name"]

    answer2 = df.loc[df["amount_spent"].idxmax(), "company_name"]

    answer3 = df[df["state"].str.lower() == "maharashtra"] \
        .groupby("development_sector")["amount_spent"].sum().idxmax()

    answer4 = df.loc[df["utilisation_rate"].idxmax(), "company_name"]

    answer5 = df[df["development_sector"].str.lower() == "sanitation"] \
        .groupby("state")["amount_spent"].sum().idxmax()

    answer6 = len(df[df["development_sector"].str.lower() == "education"])

    answer7 = df[df["company_name"].str.lower() == "infosys limited"]["amount_spent"].sum()

    answer8 = df[df["state"].str.lower() == "kerala"] \
        .loc[lambda x: x["amount_spent"].idxmax(), "company_name"]

    answer9 = df.groupby("state")["amount_spent"].sum().idxmin()

    answer10 = df[df["state"].str.lower() == "odisha"] \
        .loc[lambda x: x["amount_spent"].idxmax(), "company_name"]

    return jsonify({
        "answer1": str(answer1),
        "answer2": str(answer2),
        "answer3": str(answer3),
        "answer4": str(answer4),
        "answer5": str(answer5),
        "answer6": int(answer6),
        "answer7": float(answer7),
        "answer8": str(answer8),
        "answer9": str(answer9),
        "answer10": str(answer10),
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
