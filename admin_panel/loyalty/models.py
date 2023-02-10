import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_at')
    )
    expired_at = models.DateTimeField(
        verbose_name=_('expired_at')
    )

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    class Meta:
        abstract = True


class BaseDiscount(UUIDMixin, TimeStampedMixin):
    class DiscountType(models.TextChoices):
        all_users = "all_users"
        registration = "registration"
        birthday = "birthday"

    percent = models.FloatField()
    group_product_id = models.UUIDField()
    discount_type = models.CharField(
        verbose_name=_('discount_type'),
        max_length=20,
        choices=DiscountType.choices,
        blank=False, null=False
    )

    class Meta:
        managed = False
        db_table = 'base_discount'


class BasePromocode(UUIDMixin, TimeStampedMixin):
    class PromocodeType(models.TextChoices):
        all_users = "all_users"
        personal = "personal"
    label = models.CharField(unique=True, max_length=100)
    is_disposable = models.BooleanField()
    percent = models.FloatField()
    promocode_type = models.CharField(
        verbose_name=_('promocode_type'),
        max_length=20,
        choices=PromocodeType.choices,
        blank=False, null=False
    )

    class Meta:
        managed = False
        db_table = 'base_promocode'


class LoyaltyStatus(models.TextChoices):
    in_process = "in_process"
    finished = "finished"
    not_processed = "not_processed"


class PersonalDiscount(UUIDMixin):
    discount = models.ForeignKey(BaseDiscount, on_delete=models.CASCADE)
    user_id = models.UUIDField()
    discount_status = models.CharField(
        verbose_name=_('discount_status'),
        max_length=20,
        choices=LoyaltyStatus.choices,
        blank=False, null=False
    )

    class Meta:
        managed = False
        db_table = 'personal_discount'
        unique_together = (('discount_id', 'user_id'),)


class PersonalPromocode(UUIDMixin):
    promocode= models.ForeignKey(BasePromocode, on_delete=models.CASCADE)
    user_id = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'personal_promocode'


class PromocodeHistory(UUIDMixin):
    promocode = models.ForeignKey(BasePromocode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField()
    promocode_status = models.CharField(
        verbose_name=_('promocode_status'),
        max_length=20,
        choices=LoyaltyStatus.choices,
        blank=False, null=False
    )

    class Meta:
        managed = False
        db_table = 'promocode_history'
