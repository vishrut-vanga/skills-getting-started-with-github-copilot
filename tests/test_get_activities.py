from src.app import activities


def test_get_activities_returns_activity_data(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_participant = "michael@mergington.edu"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert expected_activity in response_data
    assert expected_participant in response_data[expected_activity]["participants"]
    assert response_data == activities
