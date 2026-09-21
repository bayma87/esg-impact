from django.db import models


class AssessmentResult(models.Model):
    environmental_score = models.IntegerField(default=0)
    social_score = models.IntegerField(default=0)
    governance_score = models.IntegerField(default=0)
    overall_score = models.IntegerField(default=0)
    weakest_pillar = models.CharField(max_length=50, default='Ambiental')
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_scores(self):
        scores = {
            'Ambiental': self.environmental_score,
            'Social': self.social_score,
            'Governança': self.governance_score,
        }
        self.overall_score = self.environmental_score + self.social_score + self.governance_score
        self.weakest_pillar = min(scores, key=scores.get)
        return self

    def __str__(self):
        return f"Resultado ESG {self.overall_score}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
