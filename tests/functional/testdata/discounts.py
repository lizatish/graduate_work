import datetime
import uuid
from http import HTTPStatus

from models.common import DiscountType, LoyaltyStatus
from api.v1.schemas.general import BaseAction

EXPIRED_AT = datetime.datetime(2024, 1, 15, 21, 55, 59, 342380)
CREATED_AT = datetime.datetime(2023, 1, 15, 21, 55, 59, 342380)


FIRST_USER_ID = uuid.UUID("845f1722-704f-44eb-bcc5-a329f305b4ec")
SECOND_USER_ID = uuid.UUID("5fe03c80-8c2a-4e88-8984-50112bc27b7d")
THIRD_USER_ID = uuid.UUID("95f9edba-a529-4902-ae33-33ae37faa788")
FOURTH_USER_ID = uuid.UUID("4b644fe7-5256-4547-be4a-e0742ee0fa9b")
FIFTH_USER_ID = uuid.UUID("95435e59-7aa3-44b8-afd0-c2909a14f519")

base_discounts_init_data: list[dict] = [
    {
        "id": "ad511a48-6d26-45ee-b6ad-98b3eec635fb",
        "group_product_id": "8af4d21c-c44a-443f-a993-81399a8f774c",
        "percent": 350,
        "discount_type": DiscountType.all_users,
        "expired_at": EXPIRED_AT,
        "created_at": CREATED_AT
    },
    {
        "id": "32d909a2-dd47-4e5c-9141-bf98770eb0d6",
        "group_product_id": "f740b79d-f4ef-4c43-8a72-07508196f68b",
        "percent": 420,
        "discount_type": DiscountType.all_users,
        "expired_at": EXPIRED_AT,
        "created_at": CREATED_AT
    },
    {
        "id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f",
        "group_product_id": "c646669a-e96b-44fc-aff3-68e95eb4f1cb",
        "percent": 100,
        "discount_type": DiscountType.registration,
        "expired_at": EXPIRED_AT,
        "created_at": CREATED_AT
    },
    {
        "id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f",
        "group_product_id": "251fb224-9873-40f3-9414-61b8c1bb28dd",
        "percent": 150,
        "discount_type": DiscountType.birthday,
        "expired_at": EXPIRED_AT,
        "created_at": CREATED_AT
    },
    {
        "id": "945da646-c872-4562-8b12-21b4ecf778e7",
        "group_product_id": "48fc918f-8cbd-4b09-8257-c3eafb8861a1",
        "percent": 137,
        "discount_type": DiscountType.all_users,
        "expired_at": datetime.datetime(2022, 1, 15, 21, 55, 59, 342380),
        "created_at": datetime.datetime(2021, 1, 15, 21, 55, 59, 342380)
    }
]

personal_discounts_init_data: list[dict] = [
    {
        "id": "c37e5e52-032e-4a15-beae-a4131f596328",
        "discount_id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f",
        "user_id": FIRST_USER_ID,
        "discount_status": LoyaltyStatus.not_processed,
    },
    {
        "id": "3395e97d-8399-4762-afcd-9c8918a9abf5",
        "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f",
        "user_id": FIRST_USER_ID,
        "discount_status": LoyaltyStatus.not_processed,
    },
    {
        "id": "1e857af3-cb48-49fc-83a9-8bba08d6981d",
        "discount_id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f",
        "user_id": SECOND_USER_ID,
        "discount_status": LoyaltyStatus.not_processed,
    },
    {
        "id": "6bfca656-2e04-46e1-bfbf-cb5603f39aea",
        "discount_id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f",
        "user_id": THIRD_USER_ID,
        "discount_status": LoyaltyStatus.in_process,
    },
    {
        "id": "58679813-1993-44c6-86ad-1822dd8eb472",
        "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f",
        "user_id": THIRD_USER_ID,
        "discount_status": LoyaltyStatus.finished,
    },
    {
        "id": "ff50669b-bac5-4ced-9d3a-221082af6039",
        "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f",
        "user_id": FIFTH_USER_ID,
        "discount_status": LoyaltyStatus.in_process,
    }
]

test_get_all_discounts_data = [
    (
        {
            "user_id": FIRST_USER_ID,
        },
        {
            "status": HTTPStatus.OK,
            "response": [
                {
                    "id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 100.0,
                    "group_product_id": "c646669a-e96b-44fc-aff3-68e95eb4f1cb",
                    "discount_type": "registration",
                },
                {
                    "id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 150.0,
                    "group_product_id": "251fb224-9873-40f3-9414-61b8c1bb28dd",
                    "discount_type": "birthday",
                },
                {
                    "id": "ad511a48-6d26-45ee-b6ad-98b3eec635fb",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 350.0,
                    "group_product_id": "8af4d21c-c44a-443f-a993-81399a8f774c",
                    "discount_type": "all_users",
                },
                {
                    "id": "32d909a2-dd47-4e5c-9141-bf98770eb0d6",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 420.0,
                    "group_product_id": "f740b79d-f4ef-4c43-8a72-07508196f68b",
                    "discount_type": "all_users",
                }
            ]
        },
    ),
    (
        {
            "user_id": SECOND_USER_ID,
        },
        {
            "status": HTTPStatus.OK,
            "response": [
                {
                    "id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 100.0,
                    "group_product_id": "c646669a-e96b-44fc-aff3-68e95eb4f1cb",
                    "discount_type": "registration",
                },
                {
                    "id": "ad511a48-6d26-45ee-b6ad-98b3eec635fb",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 350.0,
                    "group_product_id": "8af4d21c-c44a-443f-a993-81399a8f774c",
                    "discount_type": "all_users",
                },
                {
                    "id": "32d909a2-dd47-4e5c-9141-bf98770eb0d6",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 420.0,
                    "group_product_id": "f740b79d-f4ef-4c43-8a72-07508196f68b",
                    "discount_type": "all_users",
                }
            ]
        },
    ),
    (
        {
            "user_id": THIRD_USER_ID,
        },
        {
            "status": HTTPStatus.OK,
            "response": [
                {
                    "id": "ad511a48-6d26-45ee-b6ad-98b3eec635fb",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 350.0,
                    "group_product_id": "8af4d21c-c44a-443f-a993-81399a8f774c",
                    "discount_type": "all_users",
                },
                {
                    "id": "32d909a2-dd47-4e5c-9141-bf98770eb0d6",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 420.0,
                    "group_product_id": "f740b79d-f4ef-4c43-8a72-07508196f68b",
                    "discount_type": "all_users",
                }
            ]
        },
    ),
    (
        {
            "user_id": FOURTH_USER_ID,
        },
        {
            "status": HTTPStatus.OK,
            "response": [
                {
                    "id": "ad511a48-6d26-45ee-b6ad-98b3eec635fb",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 350.0,
                    "group_product_id": "8af4d21c-c44a-443f-a993-81399a8f774c",
                    "discount_type": "all_users",
                },
                {
                    "id": "32d909a2-dd47-4e5c-9141-bf98770eb0d6",
                    "created_at": CREATED_AT.isoformat(),
                    "expired_at": EXPIRED_AT.isoformat(),
                    "percent": 420.0,
                    "group_product_id": "f740b79d-f4ef-4c43-8a72-07508196f68b",
                    "discount_type": "all_users",
                }
            ]
        },
    )
]

test_change_personal_discount_status_data = [
    (
        {
            "user_id": FIRST_USER_ID,
            "action": BaseAction.apply.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.OK,
            "response": {"detail": "Discount applied"}
        },
    ),
    (
        {
            "user_id": FOURTH_USER_ID,
            "action": BaseAction.apply.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.NOT_FOUND,
            "response": {"detail": "Discount not found"}
        },
    ),
    (
        {
            "user_id": THIRD_USER_ID,
            "action": BaseAction.apply.value,
            "discount_id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f"
        },
        {
            "status": HTTPStatus.BAD_REQUEST,
            "response": {"detail": "Wrong type of discount"}
        },
    ),
    (
        {
            "user_id": THIRD_USER_ID,
            "action": BaseAction.confirm.value,
            "discount_id": "78ab52a9-d64d-4034-bbf8-3c11cfd9ad8f"
        },
        {
            "status": HTTPStatus.OK,
            "response": {"detail": "Discount confirmed"}
        },
    ),
    (
        {
            "user_id": FOURTH_USER_ID,
            "action": BaseAction.confirm.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.NOT_FOUND,
            "response": {"detail": "Discount not found"}
        },
    ),
    (
        {
            "user_id": THIRD_USER_ID,
            "action": BaseAction.confirm.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.BAD_REQUEST,
            "response": {"detail": "Wrong type of discount"}
        },
    ),
    (
        {
            "user_id": FIFTH_USER_ID,
            "action": BaseAction.revoke.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.OK,
            "response": {"detail": "Discount revoked"}
        },
    ),
    (
        {
            "user_id": FOURTH_USER_ID,
            "action": BaseAction.revoke.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.NOT_FOUND,
            "response": {"detail": "Discount not found"}
        },
    ),
    (
        {
            "user_id": THIRD_USER_ID,
            "action": BaseAction.revoke.value,
            "discount_id": "2da1c1a4-4d79-4b31-aef4-2b6c5625075f"
        },
        {
            "status": HTTPStatus.BAD_REQUEST,
            "response": {"detail": "Wrong type of discount"}
        },
    ),
]
