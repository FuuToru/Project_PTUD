from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),    
    path('profile',views.profile,name="profile"),
    path('checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),

]
