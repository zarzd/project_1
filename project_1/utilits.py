import json


def open_file():
    with open("candidates.json", encoding="utf-8") as file:
        python_file = json.load(file)
    return python_file


def load_candidates_from_json():
    with open("candidates.json", encoding="utf-8") as file:
        python_file = json.load(file)
    list_candidates = []
    for i in range(len(python_file)):
        list_candidates.append(python_file[i]["name"])
    return list_candidates


def get_candidate(candidate_id):
    file = open_file()
    return open_file()[int(candidate_id) - 1]


def get_candidates_by_name(candidate_name):
    file = open_file()
    list_names_skills = []
    for i in file:
        if candidate_name.lower() in i["name"].lower():
            list_names_skills.append(i)
    return list_names_skills


def get_candidates_by_skill(skill_name):
    list_names_to_skills = []
    for i in open_file():
        if skill_name.lower() in i["skills"].lower().split(", "):
            list_names_to_skills.append(i)
    return list_names_to_skills



