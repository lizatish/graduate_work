from django.contrib import admin

from loyalty.models import (BaseDiscount, BasePromocode, PersonalDiscount,
                            PersonalPromocode, PromocodeHistory)


@admin.register(BaseDiscount)
class BaseDiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'expired_at', 'percent', 'group_product_id',
        'discount_type'
    )
    list_filter = ('created_at', 'expired_at', 'discount_type',)


@admin.register(BasePromocode)
class BasePromocodeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'expired_at', 'label', 'is_disposable',
        'percent', 'promocode_type'
    )
    list_filter = ('created_at', 'expired_at', 'promocode_type',)


@admin.register(PersonalDiscount)
class PersonalDiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'discount_id', 'user_id', 'discount_status'
    )
    list_filter = ('discount_status',)


@admin.register(PersonalPromocode)
class PersonalPromocodeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'promocode_id', 'user_id'
    )


@admin.register(PromocodeHistory)
class PromocodeHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'promocode_id', 'created_at', 'user_id', 'promocode_status'
    )
    list_filter = ('promocode_status', 'created_at',)
