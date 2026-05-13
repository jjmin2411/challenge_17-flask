# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r",encoding="utf-8") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="nico")
 
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    
    if not keyword:
        return render_template("search.html", keyword="None", jobs=[])

    search_term = keyword.lower()

    if search_term in db:
        jobs = db[search_term]
    else:
        all_jobs = load_jobs()
        jobs = [] 
        
        for job in all_jobs:
            if (search_term in job["title"].lower() or 
                search_term in job["company_name"].lower() or 
                search_term in job["description"].lower()):
                jobs.append(job)
                
        db[search_term] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run("0.0.0.0")

# /BLUEPRINT