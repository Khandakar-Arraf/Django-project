from django.urls import path,include
from myapp.views import views,adminviews,emailview,ML_view
from user_payment import payment_views
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #website urls
    path('insur/',views.insurances,name = 'check_fraud'),
    
    path('predict/',views.results,name='predict'),
    #path('dashboards/',adminviews.index,name='index'),
    path('dashboards/',adminviews.dashboard,name='dashboard'), 
    path('dashbaord-page/',adminviews.dashboard_page,name='dashboard_page'), #admin dashboard
 
    path('home',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('login_user',views.login_user,name='login_user'),
    path('registration.html',views.user_registration,name='registration'),
    path('insertuser', views.insertuser),
    path('update_profile',views.update_profile,name='update_profile'),

    #product urls
    path('Products/',views.Products,name='Products'),

    #profile aurls
    path('profile',views.profile,name='profile'),

    #path('checkout',views.checkout,name='checkout'),
    path('faq',views.faq,name='faq'),
    path('team',views.team,name='team'),
    path('policy',views.policy,name='policy'),
    path('testimonials',views.testimonials,name='testimonials'),
    path('conditions',views.conditions,name='conditions'),
    path('contact',views.contact,name='contact'),
    path('recover_password',views.recover_password,name='recover_password'),
    path('insurance_application',views.insurance_application,name='insurance_application'),
    path('forget_password',views.forgot_password,name='forget_password'),
    path('reset-password',views.reset_password,name="reset_password"),
    path('new_password',views.new_password,name='new_password'),
    path('user_image',views.profile_image,name='user_image'),
    path('contact_message',views.contact_message,name='contact_message'),
    
    #blog views
    path('blog_detail/<int:id>',views.blog_details,name='blog_details'),
    path('blog',views.blog,name='blog'),
    path('blog_comment',views.blog_comment,name='blog_comment'),
    path('delete_comment/<int:comment_id>/<int:blog_id>',views.delete_comment,name='delete_comment'),
    

    #admin views

    path('blog_publish',adminviews.blog_publish,name='blog publish'), # link for publisshing blog
    path('blog_list.html',adminviews.blog_list,name='blog_list'),
    path('blog_delete/<int:id>',adminviews.blog_delete,name='blog_delete'),
    path('blog_post.html',adminviews.blog_post,name='blog_post'), # link for UI of blog posting
    path('blog_edit/<int:id>',adminviews.blog_edit,name='edit_blog'),
    path('update_blog/<int:id>',adminviews.update_blog,name='update_blog'),
    path('messages.html',adminviews.email_messages,name='messages'),
    path('compose.html',adminviews.compose,name='compose'),
    path('reply.html',adminviews.reply,name='reply'),
    path('chat_drawer.html',adminviews.chat_drawer,name='chat_drawer'),
    path('group_chat.html',adminviews.group_chat,name='group_chat'),
    path('private_chat.html',adminviews.private_chat,name='private_chat'),
    path('invoice2.html',adminviews.invoice2,name='invoice2'),
    path('invoice.html',adminviews.invoice,name='invoice'),
    path('invoice3',adminviews.invoice3,name='invoice3'),
    path('create_invoice.html',adminviews.create_invoice,name='create_invoice'),

    path('customer', adminviews.customer, name = 'customer'),
    path('customer_list.html',adminviews.customer_list,name='customer_list'),
    path('customer_view.html',adminviews.customer_view,name='customer_view'),
    path('customer_edit/<int:id>',adminviews.customer_edit,name='customer_edit'),
    path('customer_update/<int:id>',adminviews.customer_update,name='customer_update'),
    path('account_deactivate/<int:id>',adminviews.account_deactivate,name='account_deactivate'),
    path('account_activate/<int:id>',adminviews.account_activate,name='account_activate'),
    path('customer_delete/<int:id>',adminviews.customer_delete,name='customer_delete'),
    path('contact',adminviews.contact,name='contact'),
    path('add_customer.html',adminviews.add_contact,name='add_contact'),
    path('edit_customer.html',adminviews.edit_contact,name='edit_contact'),
    path('view_customer.html',adminviews.view_contact,name='view_contact'),

    path('files.html',adminviews.files,name='files'),
    path('folder.html',adminviews.folders,name='folders'),
    path('settings.html',adminviews.dashboard_settings,name='settings'),
    path('file_manager.html',adminviews.root_directory,name = 'root_directory'),

    path('user_list.html',adminviews.user_list,name='user_list'),
    path('user_view.html',adminviews.user_view,name='user_view'),
    path('permission.html',adminviews.permissions,name='permission'),
    path('role-list.html',adminviews.role_list,name='role_list'),
    path('role-view.html',adminviews.role_view,name='role_view'),

    path('two-factor.html',adminviews.two_factor,name='two_factor'),
    path('signup-html',adminviews.sign_up, name ='sign_up'),
    path('sign-in.html',adminviews.sign_in, name ='sign_in'),
    path('logout',adminviews.admin_logout,name='admin_logout'),
    #path('new-password.html',adminviews.new_password,name='new_password'),
    path('reset-password.html',adminviews.reset_password,name='reset_password'),
    path('verify-email.html',adminviews.verify_email,name='verify_email'),
    path('welcome.html',adminviews.welcome_user,name='welcomes'),

    #ecommerce urls
    path('add_category.html',adminviews.add_category, name = 'add_category'),
    path('new_products',adminviews.new_products, name = 'new_product'),
    path('delete_products/<int:id>',adminviews.delete_products,name='delete_products'),
    #url for uploading products
    path('uploading',adminviews.upload),
    path('categogries.html',adminviews.categogries, name = 'categogries'),
    path('edit_categories.html',adminviews.edit_categories, name = 'edit_categories'),
    path('product_edit',adminviews.product_edit, name = 'product_edit'),
    path('product_edit/<int:id>',adminviews.product_editing,name='product_editing'),
    path('product_update/<int:id>',adminviews.product_update,name='product_update'),
    path('products.html',adminviews.products, name = 'products'),


    #Orders urls
    path('Order_lisitng.html',adminviews.customer_orders, name = 'orders'),
    path('order_items',adminviews.order_items,name='order_items'),
    #order approval
    path('approval/<int:id>',adminviews.approval,name='approval'),
    #order decline
    path('decline/<int:id>',adminviews.decline,name='decline'),
    path('transaction',adminviews.transaction,name='transaction'),

    #path('testing',adminviews.testing),
    #reports urls
    path('customer_orders.html',adminviews.customer_orders, name = 'customer_orders'),
    path('returns',adminviews.returns, name = 'returns'),
    #path('sales',adminviews.sales,name='sales'),
    path('shipping',adminviews.shipping,name='shipping'),
    path('view',adminviews.view,name='view'),
    path('settings.html',adminviews.dashboard_settings,name='settings'),

    path('account_settings.html',adminviews.account_settings,name='account_settings'),

    #invoice url
    path('invoice',views.invoice),

    # pricing urls
    path('pricing',views.pricing),
    #dashboard types
    path('ecommerce.html', views.ecommerce,name='ecommerce'),
    path('analytics.html', views.analytics_dashboard,name='analytics_dashboard'),
    path('sales.html',adminviews.sales,name='sales_dashboard'),
    path('Database.html/',adminviews.database,name='Claim database'),
     path('Database_copy.html/',adminviews.database_copy,name='Claim database copy'),
    path('email.html',emailview.mailtest),
    #activating link
    #path('activation',emailview.activation,name='activate_link'),
    path('activate/<token>', emailview.activate, name='activate_link'),
    path('verifying',emailview.verify,name="verify"),
    path('resend_code',views.resend_code,name='resend_code'),
    path('reset-password',views.reset_password,name='reset_password'),
    path('changePassword/<token>',emailview.changePassword,name='forgotPassword'),
    path('update_password',views.update_password,name='update_password'),

    #views from user payement app
    path('product_page', payment_views.product_page, name='product_page'),

    #product image uplaod
    path('upload/', views.upload_product, name='upload_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('order_process',views.order_process,name='order_process'),
    #procced to checkout urls
    path('prescription_approval',views.prescription_approval,name='prescription_approval'),
    path('checkout',views.checkout,name='checkout'),
    path('products',views.product_test),
    
    #customer message urls
    path('customer_message',adminviews.customer_message,name='customer_message'),


    path('ml_testing1',ML_view.Knn_view,name='knn_model'),
    path('ml_testing2',ML_view.logistic_view,name='logistic_accuracy'),
    path('ml_testing3',ML_view.xgboost_view,name='xgb_accuracy'),
    path('ml_testing4',ML_view.randomforest_view,name='rdmf_accuracy'),
    path('delete_accuracy',ML_view.reset_accuracy,name='reset_accuracy'),

    path('reset_knn',ML_view.reset_knn,name='reset_knn'),
    path('reset_logistic',ML_view.reset_logistic,name='reset_logistic'),
    path('reset_xgboost',ML_view.reset_xgboost,name='reset_xgboost'),
    path('reset_rdmf',ML_view.reset_rdmf,name='reset_rdmf'),


    path('ml_ui',ML_view.ml_ui,name='ml_ui'),
    path('testing',ML_view.testing,),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

