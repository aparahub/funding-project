import pandas as pd

df = pd.read_csv("csr_fy_2018_19.csv")

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

df["amount_spent"] = pd.to_numeric(df["amount_spent"], errors="coerce")
df["project_amount_outlay"] = pd.to_numeric(df["project_amount_outlay"], errors="coerce")

# 1
answer1 = df[
    (df["development_sector"].str.lower() == "education") &
    (df["state"].str.lower() == "karnataka")
].loc[lambda x: x["amount_spent"].idxmax(), "company_name"]

# 2
answer2 = df.loc[df["amount_spent"].idxmax(), "company_name"]

# 3
answer3 = df[df["state"].str.lower() == "maharashtra"] \
    .groupby("development_sector")["amount_spent"].sum().idxmax()

# 4
df["utilisation_rate"] = df["amount_spent"] / df["project_amount_outlay"]
answer4 = df.loc[df["utilisation_rate"].idxmax(), "company_name"]

# 5
answer5 = df[df["development_sector"].str.lower() == "sanitation"] \
    .groupby("state")["amount_spent"].sum().idxmax()

# 6
answer6 = len(df[df["development_sector"].str.lower() == "education"])

# 7
answer7 = df[df["company_name"].str.lower() == "infosys limited"]["amount_spent"].sum()

# 8
answer8 = df[df["state"].str.lower() == "kerala"] \
    .loc[lambda x: x["amount_spent"].idxmax(), "company_name"]

# 9
answer9 = df.groupby("state")["amount_spent"].sum().idxmin()

# 10
answer10 = df[df["state"].str.lower() == "odisha"] \
    .loc[lambda x: x["amount_spent"].idxmax(), "company_name"]

print(answer1)
print(answer2)
print(answer3)
print(answer4)
print(answer5)
print(answer6)
print(answer7)
print(answer8)
print(answer9)
print(answer10)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
