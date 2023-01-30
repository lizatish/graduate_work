import json

import pytest as pytest
from httpx import AsyncClient

from tests.functional.testdata.promocodes import test_change_promocode_status_not_successful_data

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    'request_body, expected_answer', test_change_promocode_status_not_successful_data)
async def test_change_promocode_status_not_successful(
        promocodes_api_client: AsyncClient,
        request_body: dict,
        expected_answer: dict,
        mocker,
):
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body['user_id'])

    response = await promocodes_api_client.post(
        f'/api/v1/promocode/status',
        content=json.dumps(request_body["content"]),
    )
    response_body = response.json()

    assert response_body == expected_answer['response']
    assert response.status_code == expected_answer['status']
#
# @pytest.mark.parametrize(
#     'request_body, expected_answer', test_change_promocode_expired_data)
# async def test_change_promocode_expired(
#         promocodes_api_client: AsyncClient,
#         request_body: dict,
#         expected_answer: dict,
#         mocker,
# ):
#     mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body['user_id'])
#
#     response = await promocodes_api_client.post(
#         f'/api/v1/promocode/status',
#         content=json.dumps(request_body["content"]),
#     )
#     response_body = response.json()
#
#     assert response_body == expected_answer['response']
#     assert response.status_code == expected_answer['status']
#

# todo в случае успешного применения промокода - возвращать данные промокода - тесты на успех
# todo тесты на получение истории
#  todo тесты на существующий промокод но чужой
