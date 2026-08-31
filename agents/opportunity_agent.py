import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def analyze_opportunities(career_goal, education, skills, location):

    prompt = f"""
You are the Opportunity Agent inside CareerPath AI.

Your job is to help a student understand what types of
internships and entry-level opportunities they should target.

STUDENT PROFILE
---------------
Education: {education}
Current Skills: {skills}
Target Career: {career_goal}
Preferred Location: {location}

IMPORTANT RULES
---------------
1. Do not invent specific job openings.
2. Do not claim that a company is currently hiring.
3. Do not guarantee an internship or job.
4. Recommend realistic opportunity types for a student.
5. Consider the student's current skills.
6. Prioritize opportunities that match the target career.
7. Give practical application advice.

FORMAT YOUR RESPONSE EXACTLY:

# 💼 Opportunity Analysis

## 🎯 Recommended Opportunity Types

List exactly 5 suitable internship or entry-level role types.

For each one include:
- Role
- Why it matches the student
- Skills usually expected

## 📍 Location Strategy

Explain how the student can search based on the
preferred location.

Include:
- Local opportunities
- Remote opportunities
- India-wide opportunities

## 🔎 Where to Search

Recommend useful platforms and explain what to search for.

Do not claim that a specific opening currently exists.

## 📝 Application Strategy

Give 5 practical steps for applying effectively.

## 📄 Resume Focus

List the most important skills, projects, and achievements
the student should highlight on a resume.

## 🎤 Interview Preparation

List 5 important areas the student should prepare for.

## ✅ Opportunity Action Plan

Give exactly 5 actions the student should take next.

Keep the answer practical, concise, and student-friendly.
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