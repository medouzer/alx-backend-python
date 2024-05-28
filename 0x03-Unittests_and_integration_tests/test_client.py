#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        test_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("test")
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])
