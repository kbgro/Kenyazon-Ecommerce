from subcategory.models import SubCategory


def sub_menu_links(request):
    s_links = SubCategory.objects.all()
    return dict(s_links=s_links)
