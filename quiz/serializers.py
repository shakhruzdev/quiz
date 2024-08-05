from .models import Subject, Quiz, Question
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = instance.get_name_display()
        return data


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'subject']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['subject'] = instance.subject.get_name_display()
        return data


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_number', 'quiz', 'subject', 'A', 'B', 'C', 'D', 'correct_answer')
        extra_kwargs = {
            'correct_answer': {'write_only': True}
        }
