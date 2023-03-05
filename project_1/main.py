from flask import Flask, render_template, request
from utilits import get_candidate, get_candidates_by_name, get_candidates_by_skill, open_file

app = Flask(__name__)


@app.route("/")
def candidates():
    list_candidates = open_file()
    return render_template('list.html', items=list_candidates)


@app.route("/candidate/<int:x>")
def candidates_info(x):
    list_candidates_info = get_candidate(x)
    return render_template('card.html', item=list_candidates_info)


@app.route("/search/<candidate_name>")
def search_candidate(candidate_name):
    list_search = get_candidates_by_name(candidate_name)
    return render_template('search.html', items=list_search, count=len(list_search))


@app.route("/skill/<skill_name>")
def search_skill(skill_name):
    list_search = get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=list_search, count=len(list_search), skill=skill_name)


app.run()
