import json

from django.http import JsonResponse
from rest_framework.response import Response

getResponseMessage = "Get Successfully"
createResponseMessage = "Created Successfully"
updateResponseMessage = "Updated Successfully"
deleteResponseMessage = "Deleted Successfully"
errorResponseMessage = "Something Went Wrong"
notFoundResponseMessage = "Data Not Found"
authorizedResponseMessage = "Authorized"
unAuthorizedResponseMessage = "UnAuthorized"
authenticationResponseMessage = "Authenticated"
unAuthenticationResponseMessage = "UnAuthenticated"
loginResponseMessage = "Login Successfully"


def getResponse(data):
    return JsonResponse({"message": getResponseMessage, "data": data}, status=200)


def createResponse(data):
    return JsonResponse({"message": createResponseMessage, "data": data}, status=201)


def updateResponse(data):
    return JsonResponse({"message": updateResponseMessage, "data": data}, status=201)


def deleteResponse():
    return JsonResponse({"message": deleteResponseMessage}, status=204, safe=False)


def errorResponse(data):
    return Response({"message": errorResponseMessage, "errors": data}, status=400)


def notFoundResponse():
    return Response({"message": notFoundResponseMessage}, status=404)


def unAuthorizedResponse():
    return JsonResponse({"message": unAuthorizedResponseMessage}, status=403, safe=False)


def loginResponse(data, token):
    return Response({"message": loginResponseMessage, "data": data, "token": token}, status=200)
