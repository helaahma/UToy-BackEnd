from django.urls import path

from .views import (ApproveFinalBidToSellView, OnGoingBidDetail,OnGoingBidsList,BidView, CreateSellRequest,RequestUpdateView,DeleteCollectable,CollectableList, CollectableDetails, UserCreateAPIView,  UserProfile, UserProfileUpdate)

from rest_framework_simplejwt.views import TokenObtainPairView

app_name = "api"

urlpatterns=[
path('login/', TokenObtainPairView.as_view() , name='login'),
path('register/', UserCreateAPIView.as_view(), name='register'),
path('collectable/list/', CollectableList.as_view(), name='collectable-list'),
path('collectable/detail/<int:collectable_id>/', CollectableDetails.as_view(), name='collectable-detail'),
path('collectable/delete/<int:collectable_id>/', DeleteCollectable.as_view(), name='collectable-delete'),
path('sellrequest/', CreateSellRequest.as_view(), name='sell-request'),
path('sellrequest/update/<int:sellrequest_id>/', RequestUpdateView.as_view(), name='update-sellrequest'),
path('bid/list/', OnGoingBidsList.as_view(), name='bid-list'),
path('bid/detail/<int:bid_id>/', OnGoingBidDetail.as_view(), name='bid-detail'),
path('bid/<int:collectable_id>/', BidView.as_view(), name='bid-create'),
path('approve/sell/<int:collectable_id>/', ApproveFinalBidToSellView.as_view(), name='approve-sell'),
path('userprofile/', UserProfile.as_view(), name='user-profile'),
path('userprofileupdate/', UserProfileUpdate.as_view(), name='user-profile-update'),
]

# <slug:user_username>/