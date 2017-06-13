from .models import MainMenu

def main_menu_items(request):
    context = {
        'menu_items': MainMenu.objects.all()
    }
    return context
