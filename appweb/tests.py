from django.test import TestCase

from appweb.models import AssessmentResult


class AssessmentResultTests(TestCase):
    def test_calcula_pontuacao_e_pilar_critico(self):
        result = AssessmentResult(
            environmental_score=6,
            social_score=8,
            governance_score=5,
            overall_score=19,
        )

        result.calculate_scores()

        self.assertEqual(result.environmental_score, 6)
        self.assertEqual(result.social_score, 8)
        self.assertEqual(result.governance_score, 5)
        self.assertEqual(result.overall_score, 19)
        self.assertEqual(result.weakest_pillar, 'Governança')
