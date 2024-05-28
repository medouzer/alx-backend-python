import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """class  TestGithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1, "node_id": "MDQ6VXNlcjE=", "url": "https://api.github.com/orgs/google"}),
        ("abc", {"login": "abc", "id": 2, "node_id": "MDQ6VXNlcjI=", "url": "https://api.github.com/orgs/abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_org, mock_get_json):
        mock_get_json.return_value = expected_org
        
        client = GithubOrgClient(org_name)
        result = client.org
        
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_org)