"""
Script to add initial survey questions to the database.
Run this after migrations: python add_survey_questions.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SiriusMain.settings')
django.setup()

from surveys.models import SurveyQuestion

questions_data = [
    {'text': 'Ваши логические умозаключения чаще всего обоснованны и правильны?', 'order': 1},
    {'text': 'Влияет ли чужое мнение на ваше мышление?', 'order': 2},
    {'text': 'Вы строите свою жизнь на основе обдуманных решений?', 'order': 3},
    {'text': 'Вы доверяете логическим умозаключениям?', 'order': 4},
    {'text': 'Появление оригинальной сильной идеи доставляет вам радость?', 'order': 5},
    {'text': 'Во время дискуссий вы чувствуете себя уверенно?', 'order': 6},
    {'text': 'Вас можно назвать вдумчивым человеком?', 'order': 7},
    {'text': 'Вас можно назвать эмоциональным человеком?', 'order': 8},
    {'text': 'Вы верите астрологам?', 'order': 9},
    {'text': 'Вас можно назвать суеверным человеком?', 'order': 10},
    {'text': 'Ваши чувства и эмоции управляют вами?', 'order': 11},
    {'text': 'Вы склонны к резкой смене настроения?', 'order': 12},
    {'text': 'Вы стремитесь обладать чем-либо или кем-либо единолично и безраздельно?', 'order': 13},
    {'text': 'Вас можно назвать скупым человеком?', 'order': 14},
    {'text': 'Вас можно назвать ответственным человеком?', 'order': 15},
    {'text': 'Вам легко дается руководить деятельностью других людей?', 'order': 16},
    {'text': 'Вас можно назвать независимым человеком?', 'order': 17},
    {'text': 'Способны ли вы самостоятельно и своевременно принимать ответственные решения?', 'order': 18},
    {'text': 'Свое поведение вы держите под контролем?', 'order': 19},
    {'text': 'Можно ли вас назвать настойчивым человеком?', 'order': 20},
    {'text': 'Начатые дела вы доводите до конца?', 'order': 21},
    {'text': 'Обладаете ли вы волевыми качествами?', 'order': 22},
    {'text': 'Вы можете вести за собой других людей?', 'order': 23}
]

def add_questions():
    """Add survey questions to the database."""
    print("Adding survey questions...")
    
    for question_data in questions_data:
        # Check if question already exists
        existing = SurveyQuestion.objects.filter(text=question_data['text']).first()
        if existing:
            print(f"  ✓ Question {question_data['order']} already exists: {question_data['text'][:50]}...")
            continue
        
        # Create new question
        SurveyQuestion.objects.create(**question_data)
        print(f"  + Added question {question_data['order']}: {question_data['text'][:50]}...")
    
    total = SurveyQuestion.objects.count()
    print(f"\n✓ Total questions in database: {total}")

if __name__ == '__main__':
    add_questions()
