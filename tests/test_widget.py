import unittest
import requests


class WidgetTestCase(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    WIDGET_URL = "{}/widget/".format(API_URL)
    WIDGETS_URL = "{}/widgets".format(API_URL)

    def test_1_create_widget(self):
        widget_name = "widget_test_1"
        payload = {
            "number_of_parts": 20
        }
        expected_result = {
            "name": "widget_test_1",
            "number_of_parts": 20
        }
        expected_status_code = 201
        response = requests.post(self.WIDGET_URL + "/" + widget_name, payload)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_result)

    def test_2_create_another_widget(self):
        widget_name = "widget_test_2"
        payload = {
            "number_of_parts": 100
        }
        expected_result = {
            "name": "widget_test_2",
            "number_of_parts": 100
        }
        expected_status_code = 201
        response = requests.post(self.WIDGET_URL + "/" + widget_name, payload)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_result)

    def test_3_get_widgets(self):
        expected_widgets_count = 2
        expected_result = [
            {
                "name": "widget_test_1",
                "number_of_parts": 20
            },
            {
                "name": "widget_test_2",
                "number_of_parts": 100
            }
        ]
        expected_status_code = 200
        response = requests.get(self.WIDGETS_URL)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(
            len(response.json()), expected_widgets_count)
        self.assertEqual(response.json(), expected_result)

    def test_4_get_widget_by_name(self):
        widget_name = "widget_test_1"
        expected_result = {
            "name": "widget_test_1",
            "number_of_parts": 20
        }
        expected_number_of_parts = 20
        expected_status_code = 200
        response = requests.get(self.WIDGET_URL + "/" + widget_name)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_result)
        self.assertEqual(
            response.json()['number_of_parts'], expected_number_of_parts)

    def test_5_update_widget_by_name(self):
        widget_name = "widget_test_2"
        payload = {
            "number_of_parts": 120
        }
        expected_result = {
            "name": "widget_test_2",
            "number_of_parts": 120
        }
        expected_number_of_parts = 120
        expected_status_code = 200
        response = requests.put(self.WIDGET_URL + "/" + widget_name, payload)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_result)
        self.assertEqual(
            response.json()['number_of_parts'], expected_number_of_parts)

    def test_6_delete_widget(self):
        widget_name = "widget_test_1"
        expected_result = {"message": "Widget deleted"}
        expected_status_code = 200
        response = requests.delete(self.WIDGET_URL + "/" + widget_name)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_result)

    def test_7_get_widgets(self):
        expected_widgets_count = 1
        expected_result = [
            {
                "name": "widget_test_2",
                "number_of_parts": 120
            }
        ]
        expected_status_code = 200
        response = requests.get(self.WIDGETS_URL)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(
            len(response.json()), expected_widgets_count)
        self.assertEqual(response.json(), expected_result)


if __name__ == '__main__':
    unittest.main()
