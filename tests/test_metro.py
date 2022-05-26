from unittest.mock import Mock

import pytest
import requests


class MockResponse:
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove attempts within tests to create http requests."""
    monkeypatch.delattr("requests.sessions.Session.request")


def test_direction_json(client, monkeypatch):
    """Test the basic busroute json respons"""
    json = [{"direction_id": 0, "direction_name": "Northbound"}, {"direction_id": 1, "direction_name": "Southbound"}]

    def mock_get(*args, **kwargs):
        return MockResponse(json)

    monkeypatch.setattr(requests, "get", mock_get)
    response = client.get("/direction/1")
    assert response.json == json


def test_stops_json(client, monkeypatch):
    """Test the basic routes response"""
    json = [{"ABCD": "Stop 1", "ANNO": "Stop 2"}]

    def mock_get(*args, **kwargs):
        return MockResponse(json)

    monkeypatch.setattr(requests, "get", mock_get)
    response = client.get("/stops/10/30")
    assert response.json == json
