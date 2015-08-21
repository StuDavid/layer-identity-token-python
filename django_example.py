# -*- coding: utf-8 -*-
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from layer import generate_identity_token

# disables the CSRF middleware, if you have it installed
@csrf_exempt
def get_identity_token(request):
    # check to ensure that we were given the req'd params
    if set(('user_id', 'nonce')) <= set(request.POST):
        user_id = request.POST['user_id']
        nonce = request.POST['nonce']
    else:
        return HttpResponse("Invalid Request.")

    # create the token
    identityToken = generate_identity_token(user_id, nonce)

    # return our token with a JSON Content-Type
    return JsonResponse({'identity_token': identityToken})
