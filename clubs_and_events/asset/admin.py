from django.contrib import admin

from asset.models import AlbumImage, Announcement, Album, Comment


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'partial_text', 'community', 'created_at', 'created_by', 'updated_at', 'updated_by']

    def partial_text(self, obj):
        if len(obj.text) <= 64:
            return obj.text
        return obj.text[:64] + '...'


class AlbumImageInline(admin.StackedInline):
    model = AlbumImage
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'photos', 'community', 'community_event', 'created_at', 'created_by', 'updated_at', 'updated_by'
    ]
    inlines = [AlbumImageInline]

    def photos(self, obj):
        return len(AlbumImage.objects.filter(album=obj.id))


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'partial_text', 'written_by', 'event', 'created_at', 'created_by']

    def partial_text(self, obj):
        if len(obj.text) <= 64:
            return obj.text
        return obj.text[:64] + '...'


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Comment, CommentAdmin)