import spacy
from ml.skills_db import SKILLS

nlp = spacy.load("en_core_web_sm")


def extract_skills(text):

    doc = nlp(text.lower())

    found_skills = set()

    for skill in SKILLS:

        if skill.lower() in doc.text:
            found_skills.add(skill)

    return sorted(list(found_skills))