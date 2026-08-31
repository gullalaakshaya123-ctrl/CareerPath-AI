import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def analyze_skill_gap(current_skills, career_goal):
    prompt = f"""
You are the Skill Gap Agent inside CareerPath AI.

Your task is to analyze the student's current skills and compare
them with the skills normally required for the target career.

Student's Current Skills:
{current_skills}

Target Career:
{career_goal}

Provide a practical skill-gap analysis.

Use EXACTLY these sections:

# 📊 Skill Gap Analysis

## ✅ Skills Already Have
List the skills from the student's profile that are useful
for the target career.

## 🔴 High Priority Skill Gaps
List the 3 most important missing skills.

For each skill provide:
- Skill
- Why it is important
- Beginner learning recommendation

## 🟡 Medium Priority Skill Gaps
List 3 useful skills that can be learned after the high-priority skills.

For each skill provide:
- Skill
- Why it is useful
- Learning recommendation

## 🟢 Future Skills
List 2 advanced skills that can be learned later.

## 🎯 Priority Order
Give a numbered list from 1 to 5 showing what the student
should learn first.

IMPORTANT:
- Do not invent skills the student already has.
- Do not assume professional experience.
- Keep recommendations realistic for a student.
- Do not promise employment.
- Keep the response concise and practical.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]