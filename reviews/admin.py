from django.contrib import admin
from .models import Review


class GradeFilter(admin.SimpleListFilter):
    title = "Filter by Grade"

    parameter_name = "Grade"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad (~⭐2)"),
            ("good", "Good (⭐3~)"),
        ]

    def queryset(self, request, reviews):
        grade = self.value()
        if grade:
            if grade == "bad":
                return reviews.filter(rating__lt=3)
            return reviews.filter(rating__gte=3)
        return reviews


class WordFilter(admin.SimpleListFilter):
    title = "Filter by Words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
            ("nice", "Nice"),
        ]

    def queryset(self, request, reviews):
        # print(reviews)
        # print(dir(request))
        # print(request.GET)
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        return reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        GradeFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
