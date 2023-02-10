import json
from http import HTTPStatus

import pytest as pytest
from httpx import AsyncClient

from tests.functional.testdata.promocodes import test_change_promocode_status_not_successful_data, \
    test_change_promocode_status_successful_data, tests_apply_promocode_second_many_times_successful_data, \
    tests_apply_promocode_second_many_times_unsuccessful_data, tests_get_promocode_history_successful_data

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


@pytest.mark.parametrize(
    'request_body, expected_answer', test_change_promocode_status_successful_data)
async def test_change_promocode_status_successful(
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


@pytest.mark.parametrize(
    'request_body, expected_answer', tests_apply_promocode_second_many_times_successful_data)
async def tests_apply_promocode_second_many_times_successful(
        promocodes_api_client: AsyncClient,
        request_body: list[dict],
        expected_answer: list[dict],
        mocker,
):
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body[0]['user_id'])

    for i in range(3):
        for request_body_elem, expected_answer_elem in zip(request_body, expected_answer):
            response = await promocodes_api_client.post(
                f'/api/v1/promocode/status',
                content=json.dumps(request_body_elem["content"]),
            )
            response_body = response.json()

            assert response_body == expected_answer_elem['response']
            assert response.status_code == expected_answer_elem['status']


@pytest.mark.parametrize(
    'request_body, expected_answer', tests_apply_promocode_second_many_times_unsuccessful_data)
async def tests_apply_promocode_second_many_times_unsuccessful(
        promocodes_api_client: AsyncClient,
        request_body: list[dict],
        expected_answer: list[dict],
        mocker,
):
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body[0]['user_id'])

    for request_body_elem, expected_answer_elem in zip(request_body, expected_answer):
        response = await promocodes_api_client.post(
            f'/api/v1/promocode/status',
            content=json.dumps(request_body_elem["content"]),
        )
        response_body = response.json()

        assert response_body == expected_answer_elem['response']
        assert response.status_code == expected_answer_elem['status']

    for request_body_elem, _ in zip(request_body, expected_answer):
        response = await promocodes_api_client.post(
            f'/api/v1/promocode/status',
            content=json.dumps(request_body_elem["content"]),
        )
        response_body = response.json()
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response_body == {'detail': 'This promocode can\'t be used because has invalid status'}


@pytest.mark.parametrize(
    'request_body, expected_answer', tests_get_promocode_history_successful_data)
async def tests_get_promocode_history_successful(
        promocodes_api_client: AsyncClient,
        request_body: dict,
        expected_answer: dict,
        mocker,
):
    mocker.patch("core.middleware.AuthRequired.__call__", return_value=request_body['user_id'])

    response = await promocodes_api_client.get(f'/api/v1/promocode/history')
    response_body = response.json()

    assert response_body == expected_answer['response']
    assert response.status_code == expected_answer['status']
