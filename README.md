<<<<<<< HEAD
# funding-project
CSR funding quiz
=======
# CSR Quiz App

A Vue.js + Flask quiz app using CSR spending data.

## Tech Stack

- Vue.js
- Vite
- Tailwind CSS
- Python Flask
- pandas

Choice of tech stack - 
Since it was a light weight API, a simple python script was writting in flask. 
The data from the csv file was extracted into a dataframe which was used by pandas library to clean and run queries. Since there were only 57000 rows, making it very light, a dataframe could easily handle it.

Since the app was a single page , a light weight simple javascript framework vue.js was used.
The results from the python script were extracted into json format which is javascript friendly.
The frontend was designed and styled using tailwind css.

## Project Structure

```text
backend/   Python Flask API
frontend/  Vue frontend


5453ab7 (Initial CSR quiz app)
