import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def analyze_resume(resume_text, career_goal):

    prompt = f"""
You are the Resume Analysis Agent inside CareerPath AI.

Analyze the student's resume against their target career.

TARGET CAREER:
{career_goal}

RESUME:
{resume_text}

Your job is to identify strengths, missing skills, resume weaknesses,
and practical improvements.

IMPORTANT RULES:
1. Only use information actually present in the resume.
2. Do not invent education, skills, projects, or experience.
3. Do not guarantee employment.
4. Keep recommendations realistic for a student.
5. Focus on relevance to the target career.

FORMAT YOUR RESPONSE EXACTLY:

# 📄 Resume Analysis

## ✅ Resume Strengths

List the strongest parts of the resume.

## 🎯 Career Relevance

Explain how well the resume matches the target career.

## 🔴 Missing or Weak Skills

List important skills that are missing or not clearly demonstrated.

## 🛠️ Resume Improvements

Give 5 specific improvements.

## 📊 Project Suggestions

Suggest up to 3 project improvements that would strengthen the resume.

## 💼 Experience & Internship Suggestions

Explain what types of experience the student should try to gain.

## ✍️ Resume Checklist

Give exactly 5 final checks the student should complete.

Keep the response concise, practical, and student-friendly.
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