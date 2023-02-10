import pytest as pytest
from httpx import AsyncClient

from tests.functional.testdata.discounts import test_get_all_discounts_data, test_change_personal_discount_status_data

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    'request_body, expected_answer', test_get_all_discounts_data)
async def test_get_all_discounts(
        discounts_api_client: AsyncClient,
        request_body: dict,
        expected_answer: dict,
        mocker,
):
    """
    Тест для получения всех доступных скидок.
    Проверяет:
    - успешный статус запроса
    - соответствие полученных скидок ожидаемому значению
    """
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body['user_id'])

    response = await discounts_api_client.get('/api/v1/discount/')
    response_body = response.json()

    assert response_body == expected_answer['response']
    assert response.status_code == expected_answer['status']


@pytest.mark.parametrize(
    'request_body, expected_answer', test_change_personal_discount_status_data)
async def test_change_personal_discount_status(
        discounts_api_client: AsyncClient,
        request_body: dict,
        expected_answer: dict,
        mocker,
):
    """
    Тест для изменения статуса персональной скидки.
    Проверяет:
    - соответствие статуса запроса ожидаемому значению
    - соответствие полученного ответа ожидаемому значению
    """
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body['user_id'])

    response = await discounts_api_client.post(
        f'/api/v1/discount/{request_body["action"]}/{request_body["discount_id"]}'
    )
    response_body = response.json()

    assert response_body == expected_answer['response']
    assert response.status_code == expected_answer['status']
