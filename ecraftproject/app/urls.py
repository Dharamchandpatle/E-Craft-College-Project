from django.urls import path ,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import PasswordChangeView 



urlpatterns = [
    path('', views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('payment/', views.payment, name='payment'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('remove/', views.remove, name='remove'),
    path('remove1/', views.remove1, name='remove1'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('cart/', views.cart, name='cart'),
    path('show/', views.showcart, name='showcart'),
    path('login/', views.login, name='login'),
    path('shop/', views.shop, name='shop'),
    path('design/', views.design, name='design'),
    path('qr/', views.qr, name='qr'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('shopview/', views.shopview, name='shopview'),
    path('ngo/', views.ngo, name='ngo'),
    path('orderhistory/', views.orderhistory, name='orderhistory'),
    path('logout/', views.logout, name='logout'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('category/', views.category, name='category'),
    path('register/', views.register, name='register'),
    path("search/", views.search , name="search"),
    path("selling/", views.selling , name="selling"),
    path('checkout/', views.checkout, name='checkout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='app/registration/password_reset_from.html'), name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='app/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='app/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('pa/',auth_views.PasswordChangeView.as_view(template_name='app/registration/changepassword.html'), name='pa'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='app/registration/changepassworddone.html'), name='password_change_done'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
