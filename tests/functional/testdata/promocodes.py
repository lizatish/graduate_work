import datetime
import uuid
from http import HTTPStatus

from api.v1.schemas.general import BaseAction
from models.common import PromocodeType, LoyaltyStatus

FIRST_USER_ID = uuid.UUID("845f1722-704f-44eb-bcc5-a329f305b4ec")
SECOND_USER_ID = uuid.UUID("245c63d5-9925-499e-8a21-68b5184b5e81")
ANOTHER_USER_UD = uuid.UUID("5735bfc4-d411-4121-995a-89f659c787be")
NOT_USED_USER_ID = uuid.UUID("fb34c784-b163-454b-acac-c1ddd58dc5d1")

COMMON_PROMOCODE_ID_DISPOSABLE = uuid.UUID("719b847d-2a4b-4e8e-81c3-e5110ad359a1")
COMMON_PROMOCODE_DISPOSABLE = "КИНО2020"
COMMON_PROMOCODE_ID_NOT_DISPOSABLE = uuid.UUID("b78130ca-a1fb-43c4-b6d2-3dca439c0b2e")
COMMON_PROMOCODE_NOT_DISPOSABLE = "НОВЫЙГОД2021"
COMMON_PROMOCODE_ID_EXPIRED = uuid.UUID("0a957746-c33e-4abe-9760-219f3b10bdfb")
COMMON_PROMOCODE_EXPIRED = "ABRACADAbRA45"

PERSONAL_ID_PROMOCODE_DISPOSABLE = uuid.UUID("37b2cb21-41ed-45bc-a5aa-a99a91bc9a28")
PERSONAL_PROMOCODE_DISPOSABLE = "ASDR456BD"
PERSONAL_ID_PROMOCODE_DISPOSABLE2 = uuid.UUID("98b547b7-766d-4e03-b821-b1be1ae65496")
PERSONAL_PROMOCODE_DISPOSABLE2 = "123ГUIAD"
PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE = uuid.UUID("dc0e9b17-9d44-43d5-b565-e337b9e0cfee")
PERSONAL_PROMOCODE_NOT_DISPOSABLE = "KJSDFND12"
PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE2 = uuid.UUID("78ed3139-0c78-4447-b196-a7731845e8c7")
PERSONAL_PROMOCODE_NOT_DISPOSABLE2 = "KIKIMORA23"
PERSONAL_ID_PROMOCODE_EXPIRED = uuid.UUID("81a745ea-8c14-43be-bf00-4745c33044ea")
PERSONAL_PROMOCODE_EXPIRED = "FGJHBDJ12312"

PERSONAL_ID_PROMOCODE_NOT_USED_DISPOSABLE = uuid.UUID("feebe886-7225-4df3-b810-c1395bee6751")
PERSONAL_PROMOCODE_NOT_USED_DISPOSABLE = 'BKJDFJKSF@'
PERSONAL_ID_PROMOCODE_NOT_USED_NOT_DISPOSABLE = uuid.UUID("1c83131c-d0ac-47de-b4be-8e86284d45f7")
PERSONAL_PROMOCODE_NOT_USED_NOT_DISPOSABLE = '89lKJDMSL'
COMMON_PROMOCODE_ID_NOT_USED_DISPOSABLE = uuid.UUID("bf17c0b2-2dd8-4770-982c-51bf86e92cd3")
COMMON_PROMOCODE_NOT_USED_DISPOSABLE = '77878HHHHHH'
COMMON_PROMOCODE_ID_NOT_USED_NOT_DISPOSABLE = uuid.UUID("8c858c35-6b7c-4fbb-bbf1-eb589d976e9d")
COMMON_PROMOCODE_NOT_USED_NOT_DISPOSABLE = '1233HGJASD'

BASE_CREATED_AT_TIME: datetime = datetime.datetime.utcnow()

base_promocodes_init_data: list[dict] = [
    {
        "id": PERSONAL_ID_PROMOCODE_NOT_USED_DISPOSABLE,
        "label": PERSONAL_PROMOCODE_NOT_USED_DISPOSABLE,
        "is_disposable": True,
        "percent": 350,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": PERSONAL_ID_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
        "label": PERSONAL_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
        "is_disposable": False,
        "percent": 100,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": COMMON_PROMOCODE_ID_NOT_USED_DISPOSABLE,
        "label": COMMON_PROMOCODE_NOT_USED_DISPOSABLE,
        "is_disposable": True,
        "percent": 1300,
        "promocode_type": PromocodeType.all_users,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": COMMON_PROMOCODE_ID_NOT_USED_NOT_DISPOSABLE,
        "label": COMMON_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
        "is_disposable": False,
        "percent": 210,
        "promocode_type": PromocodeType.all_users,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": PERSONAL_ID_PROMOCODE_DISPOSABLE,
        "label": PERSONAL_PROMOCODE_DISPOSABLE,
        "is_disposable": True,
        "percent": 350,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": PERSONAL_ID_PROMOCODE_DISPOSABLE2,
        "label": PERSONAL_PROMOCODE_DISPOSABLE2,
        "is_disposable": True,
        "percent": 350,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE,
        "label": PERSONAL_PROMOCODE_NOT_DISPOSABLE,
        "is_disposable": False,
        "percent": 100,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE2,
        "label": PERSONAL_PROMOCODE_NOT_DISPOSABLE2,
        "is_disposable": False,
        "percent": 100,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": PERSONAL_ID_PROMOCODE_EXPIRED,
        "label": PERSONAL_PROMOCODE_EXPIRED,
        "is_disposable": False,
        "percent": 230,
        "promocode_type": PromocodeType.personal,
        "expired_at": datetime.datetime.utcnow() - datetime.timedelta(days=1),
    },
    {
        "id": COMMON_PROMOCODE_ID_DISPOSABLE,
        "label": COMMON_PROMOCODE_DISPOSABLE,
        "is_disposable": True,
        "percent": 1300,
        "promocode_type": PromocodeType.all_users,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": COMMON_PROMOCODE_ID_NOT_DISPOSABLE,
        "label": COMMON_PROMOCODE_NOT_DISPOSABLE,
        "is_disposable": False,
        "percent": 210,
        "promocode_type": PromocodeType.all_users,
        "expired_at": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    },
    {
        "id": COMMON_PROMOCODE_ID_EXPIRED,
        "label": COMMON_PROMOCODE_EXPIRED,
        "is_disposable": True,
        "percent": 120,
        "promocode_type": PromocodeType.all_users,
        "expired_at": datetime.datetime.utcnow() - datetime.timedelta(days=1),
    },
]
personal_promocodes_init_data: list[dict] = [
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_NOT_USED_DISPOSABLE,
        "user_id": NOT_USED_USER_ID,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
        "user_id": NOT_USED_USER_ID,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_DISPOSABLE,
        "user_id": FIRST_USER_ID,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE,
        "user_id": FIRST_USER_ID,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE2,
        "user_id": SECOND_USER_ID,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_DISPOSABLE2,
        "user_id": SECOND_USER_ID,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_EXPIRED,
        "user_id": SECOND_USER_ID,
    }
]

promocode_history_init_data: list[dict] = [
    # уже примененный одноразовый (не персональный)
    {
        "promocode_id": COMMON_PROMOCODE_ID_DISPOSABLE,
        "user_id": ANOTHER_USER_UD,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.in_process,
    },
    {
        "promocode_id": COMMON_PROMOCODE_ID_DISPOSABLE,
        "user_id": SECOND_USER_ID,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.finished,
    },
    # многоразовый для всех
    {
        "promocode_id": COMMON_PROMOCODE_ID_NOT_DISPOSABLE,
        "user_id": ANOTHER_USER_UD,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.in_process,
    },
    {
        "promocode_id": COMMON_PROMOCODE_ID_NOT_DISPOSABLE,
        "user_id": SECOND_USER_ID,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.finished,
    },
    # одноразовый для одного
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_DISPOSABLE,
        "user_id": FIRST_USER_ID,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.in_process,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_DISPOSABLE2,
        "user_id": SECOND_USER_ID,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.finished,
    },
    # многоразовый для одного
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE,
        "user_id": FIRST_USER_ID,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.in_process,
    },
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_NOT_DISPOSABLE2,
        "user_id": SECOND_USER_ID,
        "created_at": BASE_CREATED_AT_TIME,
        "promocode_status": LoyaltyStatus.finished,
    },
    # персональный уже просроченный
    {
        "promocode_id": PERSONAL_ID_PROMOCODE_EXPIRED,
        "user_id": SECOND_USER_ID,
        "created_at": BASE_CREATED_AT_TIME - - datetime.timedelta(days=2),
        "promocode_status": LoyaltyStatus.finished,
    },
    # общий уже просроченный
    {
        "promocode_id": COMMON_PROMOCODE_ID_EXPIRED,
        "user_id": SECOND_USER_ID,
        "created_at": BASE_CREATED_AT_TIME - datetime.timedelta(days=2),
        "promocode_status": LoyaltyStatus.finished,
    },
    {
        "promocode_id": COMMON_PROMOCODE_ID_EXPIRED,
        "user_id": FIRST_USER_ID,
        "created_at": BASE_CREATED_AT_TIME - datetime.timedelta(days=2),
        "promocode_status": LoyaltyStatus.in_process,
    },
]

test_change_promocode_status_not_successful_data = [
    ### НЕСУЩЕСТВУЮЩИЙ ПРОМОКОД
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": "123456HJHJB",
                "action": BaseAction.apply.value
            }

        },
        {
            'status': HTTPStatus.NOT_FOUND,
            'response': {'detail': 'Promocode not found'},
        },
    ),
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": "ZiMA7890",
                "action": BaseAction.confirm.value
            }

        },
        {
            'status': HTTPStatus.NOT_FOUND,
            'response': {'detail': 'Promocode not found'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": "LETO1212",
                "action": BaseAction.revoke.value
            }

        },
        {
            'status': HTTPStatus.NOT_FOUND,
            'response': {'detail': 'Promocode not found'},
        },
    ),
    ### НЕКОРРЕКТНЫЙ СТАТУС
    # уже примененный одноразовый (статус in_process) (не персональный)  [можно сменить статус на confirm, revoke]
    (
        {
            "user_id": ANOTHER_USER_UD,
            "content": {
                "label": COMMON_PROMOCODE_DISPOSABLE,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # полностью использованный одноразовый (статус finished) (не персональный) [сменить статус нельзя]
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_DISPOSABLE,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_DISPOSABLE,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_DISPOSABLE,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # уже примененный многоразовый (статус in_process) (не персональный) [можно сменить статус на confirm, revoke]
    (
        {
            "user_id": ANOTHER_USER_UD,
            "content": {
                "label": COMMON_PROMOCODE_NOT_DISPOSABLE,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # полностью использованный многоразовый (статус finished) (не персональный) [сменить статус можно на apply]
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_NOT_DISPOSABLE,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_NOT_DISPOSABLE,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # уже примененный одноразовый (статус in_process) (персональный)  [можно сменить статус на confirm, revoke]
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_DISPOSABLE,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # полностью использованный одноразовый (статус finished) (персональный) [сменить статус нельзя]
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_DISPOSABLE2,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_DISPOSABLE2,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        }
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_DISPOSABLE2,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        }
    ),
    # уже примененный многоразовый (статус in_process) (персональный) [можно сменить статус на confirm, revoke]
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_DISPOSABLE,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        }
    ),
    # полностью использованный многоразовый (статус finished) (персональный) [сменить статус можно на apply]
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_DISPOSABLE2,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        }
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_DISPOSABLE2,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        }
    ),
    # просроченный (статус finished) (персональный) [сменить статус нельзя]
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_EXPIRED,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_EXPIRED,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_EXPIRED,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    # просроченный (статус finished) (не персональный) [сменить статус нельзя]
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    # просроченный (статус in_process) (не персональный) [сменить статус нельзя]
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": FIRST_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    ### НЕИСПОЛЬЗОВАННЫЕ
    # просроченный (не персональный) [сменить статус нельзя]
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.apply.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_EXPIRED,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.GONE,
            'response': {'detail': 'This promo code has expired'},
        },
    ),
    # одноразовый (персональный) [сменить статус можно на apply]
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_USED_DISPOSABLE,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_USED_DISPOSABLE,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # многоразовый (персональный) [сменить статус можно на apply]
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": PERSONAL_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # одноразовый (не персональный) [сменить статус можно на apply]
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_NOT_USED_DISPOSABLE,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_NOT_USED_DISPOSABLE,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    # многоразовый (не персональный) [сменить статус можно на apply]
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
                "action": BaseAction.confirm.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
    (
        {
            "user_id": NOT_USED_USER_ID,
            "content": {
                "label": COMMON_PROMOCODE_NOT_USED_NOT_DISPOSABLE,
                "action": BaseAction.revoke.value
            }
        },
        {
            'status': HTTPStatus.BAD_REQUEST,
            'response': {'detail': 'This promocode can\'t be used because has invalid status'},
        },
    ),
]
