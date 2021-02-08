from utils.my_status import *
from rest_framework.response import Response
from rest_framework import status as _status


def response(code=_status.HTTP_201_CREATED, headers=None, **data):
    data['code'] = code
    return Response(data, status=code, headers=headers)


def response_success_200(headers=None, code=STATUS_200_SUCCESS, **data):
    data['code'] = code
    return Response(data, status=_status.HTTP_200_OK, headers=headers)


def response_error_400(status=STATUS_400_BAD_REQUEST, headers=None, **data):
    data['code'] = STATUS_400_BAD_REQUEST
    data['status'] = status
    return Response(data, status=_status.HTTP_400_BAD_REQUEST, headers=headers)


def response_error_500(status=STATUS_500_INTERNAL_SERVER_ERROR, headers=None, **data):
    data['code'] = STATUS_500_INTERNAL_SERVER_ERROR
    data['status'] = status
    return Response(data, status=_status.HTTP_500_INTERNAL_SERVER_ERROR, headers=headers)


def response_not_found_404(status=STATUS_404_NOT_FOUND, headers=None, **data):
    data['code'] = STATUS_404_NOT_FOUND
    data['status'] = status
    return Response(data, status=_status.HTTP_404_NOT_FOUND, headers=headers)
