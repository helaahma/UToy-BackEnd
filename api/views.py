from django.shortcuts import render
from .models import Collectable, ProfileUser, BidOrder
from .serializers import CollectableDetailSerializer,OnGoingBidsSerializer, BidSerializer, CollectableSerializer, UserCreateSerializer, ProfileSerializer, ProfileUpdateSerializer
from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from rest_framework.views import APIView 
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import Collectable, ProfileUser, BidOrder
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser,)
from rest_framework.response import Response
from django.http import Http404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
from .permissions import IsOwner, IsNotOwner
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.mail import send_mail
from django.template.loader import render_to_string



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserProfile(RetrieveAPIView):
    serializer_class = ProfileSerializer
    def get_object(self):
        return self.request.user.profile


class UserProfileUpdate(RetrieveUpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsOwner]
    

class CreateSellRequest(CreateAPIView):
    serializer_class = CollectableSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CollectableList(ListAPIView):
    queryset= Collectable.objects.filter(available=True)
    serializer_class = CollectableSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item', 'group', 'desired_price', 'special_features', 'condition', 'owner']


class CollectableDetails(RetrieveAPIView):
    queryset = Collectable.objects.all()
    serializer_class = CollectableDetailSerializer
    permission_classes = [AllowAny]
    lookup_field ='id'
    lookup_url_kwarg ='collectable_id'


class DeleteCollectable(DestroyAPIView):
    queryset = Collectable.objects.filter(available=False)
    lookup_field = 'id'
    lookup_url_kwarg = 'collectable_id'
    permission_classes = [IsAdminUser, IsOwner]


class RequestUpdateView(RetrieveUpdateAPIView):
    queryset = Collectable.objects.all()
    serializer_class = CollectableSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sellrequest_id'


class OnGoingBidsList(ListAPIView):
    queryset = BidOrder.objects.filter(collectable__available=True)
    serializer_class = OnGoingBidsSerializer
    permission_classes = [IsAuthenticated]


class OnGoingBidDetail(RetrieveAPIView):
    queryset = BidOrder.objects.all()
    serializer_class = OnGoingBidsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'bid_id'


class BidView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sell_request.html'

    def send_email(self, owner_email,collectable):
        print(collectable)
        html_message = render_to_string('sell_request.html', {'collectable': collectable, 'request':self.request})
        email = send_mail(
            'Sell Requiste Status', 'plain',
            'demorejoycoded@gmail.com', [owner_email],fail_silently=False, html_message=html_message)
    def post(self, request, collectable_id):
            collectable = Collectable.objects.get(id=collectable_id)
            print(collectable)
            highest_bid = BidOrder.objects.filter(
                collectable=collectable, price__gte=int(request.data['price'])
            ).exists()
            if not highest_bid:
                bid, _ = BidOrder.objects.get_or_create(collectable=collectable)
                bid.price = request.data['price']
                bid.bidder = self.request.user
                bid.save()
                owner_email = collectable.owner.email
                print(owner_email)
                print(collectable.id)
                self.send_email(owner_email, collectable)
                return Response(status=HTTP_200_OK)
            else:
                highest = collectable.bid_order.all().order_by('-price').first()
                return Response({"highest_bid":highest.price}, status=HTTP_400_BAD_REQUEST)

class ApproveFinalBidToSellView(APIView):
    permission_classes = [IsOwner]
    
    def get (self, request, collectable_id, format = None):
        collectable = Collectable.objects.get(id=collectable_id)
        collectable.available = False
        collectable.save()
        bid_closing = BidOrder.objects.get(collectable=collectable)
        bid_closing.status = False
        bid_closing.save()
        return Response({"sell_request": bid_closing.price},status=HTTP_200_OK)


        











