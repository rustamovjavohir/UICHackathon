from api.products.views import pet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('pet', pet.PetViewSet, basename='pet')
