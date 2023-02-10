import pytest as pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
async def test_promocode(promocodes_api_client: AsyncClient, mocker):
    user_id = 123
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=user_id)

    response = await promocodes_api_client.post(f'/api/v1/promocode/apply/user/{user_id}')
    response_body = response.json()

    assert response.status_code == 200
    assert response_body == {'answer': 1}

