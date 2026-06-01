from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', products_list, name='product_list'),
    path('product/<int:prod_id>/', product_detail, name='product_detail')
]

# <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-0 bg-white border-bottom box-shadow">
#     <h5 class="my-0 mr-md-auto font-weight-normal">Skystore</h5>
#     <nav class="ms-5">
#         <a class="p-2 btn btn-outline-primary" href="/">Каталог</a>
#         <a class="p-2 btn btn-outline-primary" href="/contacts/">Контакты</a>
#     </nav>
# </div>