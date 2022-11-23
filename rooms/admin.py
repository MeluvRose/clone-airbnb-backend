from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to Zero")
def reset_prices(model_admin, request, rooms):
    # print(model_admin)
    # print(dir(request))
    # print(dir(request.user))
    # print(queryset)

    for room in rooms.all():
        # print(room)
        room.price = 0
        room.save()


@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    search_fields = ("^name", "=price", "owner__username")


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
