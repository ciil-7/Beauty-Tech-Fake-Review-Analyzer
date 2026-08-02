import unittest
from analyzer import analyze_review, analyze_ingredients, get_model_evaluation_metrics

class TestBeautyTechAnalyzer(unittest.TestCase):
    
    def test_fake_review_detection(self):
        """اختبار قدرة النموذج على اكتشاف المراجعات المزيفة والمبالغ فيها"""
        fake_text = "MIRACLE product!! Changed my life overnight, 100% cure for everything, buy it NOW!"
        result = analyze_review(fake_text)
        self.assertFalse(result["is_authentic"])
        self.assertGreaterEqual(result["confidence"], 50.0)

    def test_authentic_review_detection(self):
        """اختبار قدرة النموذج على اكتشاف المراجعات الحقيقية والطبيعية"""
        authentic_text = "I've been using this serum with Niacinamide for two weeks and my skin feels hydrated."
        result = analyze_review(authentic_text)
        self.assertTrue(result["is_authentic"])
        self.assertGreaterEqual(result["confidence"], 50.0)

    def test_ingredient_extraction(self):
        """اختبار نجاح استخراج المكونات النشطة من النص"""
        text = "This cream contains Niacinamide and Hyaluronic Acid for daily use."
        ingredients = analyze_ingredients(text)
        self.assertIn("Niacinamide", ingredients)
        self.assertIn("Hyaluronic Acid", ingredients)

    def test_evaluation_metrics(data):
        """اختبار توفر مقاييس تقييم النموذج البرمجية"""
        metrics = get_model_evaluation_metrics()
        self.assertIn("accuracy", metrics)
        self.assertIn("confusion_matrix", metrics)
        self.assertGreater(metrics["accuracy"], 0.0)

if __name__ == "__main__":
    unittest.main()
