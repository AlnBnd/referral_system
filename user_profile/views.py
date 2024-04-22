import random
import time
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
import string

class SendVerificationView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
            
        verification_code = ''.join(random.choices(string.digits, k=4))
        time.sleep(random.uniform(1, 2)) 
        request.session['stored_code'] = verification_code
        request.session['phone_number'] = phone_number
        UserProfile.objects.update_or_create(phone_number=phone_number)

        return Response({'verification_code': verification_code}, status=status.HTTP_200_OK)

            
class VerifyView(APIView):
    def post(self, request):
        stored_code = request.session.get('stored_code')
        verification_code = request.data.get('verification_code')
        
        if not verification_code:
            return Response({'status': 'error', 'message': 'Verification code is required'}, status=400)

        if stored_code == verification_code:
            phone_number = request.session.get('phone_number')
            user_profile = UserProfile.objects.get(phone_number=phone_number)
            user_profile.is_verified = True
            user_profile.invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            user_profile.is_activate = False
            user_profile.save()
                        
            return Response({'message': 'Verification successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)    

class UserProfileView(APIView):
    def get(self, request):
        phone_number = request.session.get('phone_number')
        if phone_number:
            user = UserProfile.objects.get(phone_number=phone_number)
            if user.activated_invite_code is not None:
                return Response({
                        'phone_number': user.phone_number,
                        'activated_invite_code': user.activated_invite_code
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                        'phone_number': user.phone_number
                    }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        activate_code = request.data['invite_code']
        phone_number = request.session.get('phone_number')
        user_profile = get_object_or_404(UserProfile, phone_number=phone_number)
        if user_profile.activated_invite_code:
          return Response({'error': 'Invite code already activated', 'message': f'Your activated invite code: {user_profile.invite_code}'}, status=status.HTTP_400_BAD_REQUEST)
        
        if UserProfile.objects.filter(invite_code=activate_code).exists() and activate_code != user_profile.invite_code:
            user_profile.activated_invite_code = activate_code
            user_profile.is_activate = True
            user_profile.save()
            return Response({'message': 'Invite code activated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid invite code'}, status=status.HTTP_400_BAD_REQUEST)

class InviteesListView(APIView):
    def get(self, request):
        phone_number = request.session.get('phone_number')
        user_profile = get_object_or_404(UserProfile, phone_number=phone_number)
        invited_users = UserProfile.objects.filter(activated_invite_code=user_profile.invite_code)
        data = [{'phone_number': profile.phone_number} for profile in invited_users]
        if not data:
            return Response({'message': 'List is empty'}, status=status.HTTP_200_OK)
        return Response(data, status=status.HTTP_200_OK)