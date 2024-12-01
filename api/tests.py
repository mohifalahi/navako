from django.test import TestCase
from django.urls import reverse


class HealthCheckViewTest(TestCase):
    def test_healthcheck_success(self):
        response = self.client.get(reverse("health-check"))
        json_response = response.json()
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["status"], "ok")

    def test_healthcheck_fail_mehtod_not_allowed(self):
        response = self.client.post(reverse("health-check"))
        json_response = response.json()
        self.assertEqual(response.status_code, 405)
        self.assertEqual(json_response["detail"], 'Method "POST" not allowed.')


class PredictviewTest(TestCase):
    def test_predict_success(self):
        response = self.client.post(reverse("predict"), data={"text": "سلام"})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        label = json_response[0]["label"]
        score = json_response[0]["score"]
        self.assertIn(label, ["recommended", "no_idea", "not_recommended"])
        self.assertLess(score, 1)

    def test_predict_success_case_1(self):
        response = self.client.post(reverse("predict"), data={"text": "عاشقتم"})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        label = json_response[0]["label"]
        score = json_response[0]["score"]
        self.assertEqual(label, "recommended")
        self.assertLess(score, 1)

    def test_predict_success_case_2(self):
        response = self.client.post(reverse("predict"), data={"text": "متنفرم"})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        label = json_response[0]["label"]
        score = json_response[0]["score"]
        self.assertEqual(label, "not_recommended")
        self.assertLess(score, 1)

    def test_predict_success_case_3(self):
        response = self.client.post(reverse("predict"), data={"text": "خوشحالم"})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        label = json_response[0]["label"]
        score = json_response[0]["score"]
        self.assertEqual(label, "recommended")
        self.assertLess(score, 1)

    def test_predict_success_case_4(self):
        response = self.client.post(reverse("predict"), data={"text": "غمگینم"})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        label = json_response[0]["label"]
        score = json_response[0]["score"]
        self.assertEqual(label, "not_recommended")
        self.assertLess(score, 1)

    def test_predict_fail_method_not_allowed(self):
        response = self.client.get(reverse("predict"), data={"text": "غمگینم"})
        json_response = response.json()
        self.assertEqual(response.status_code, 405)
        self.assertEqual(json_response["detail"], 'Method "GET" not allowed.')

    def test_predict_fail_no_input(self):
        response = self.client.post(reverse("predict"), data={})
        json_response = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_response["detail"], "you should provide a text")
