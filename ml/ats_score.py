def calculate_ats_score(extracted_skills, required_skills):

    extracted = set(skill.lower() for skill in extracted_skills)
    required = set(skill.lower() for skill in required_skills)

    matched = extracted.intersection(required)
    missing = required.difference(extracted)

    score = int((len(matched) / len(required)) * 100)

    return {
        "ats_score": score,
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing))
    }