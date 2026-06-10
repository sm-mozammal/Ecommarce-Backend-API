from rest_framework.views import exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):
    """Custom exception handler for better error messages"""
    response = exception_handler(exc, context)

    if response is not None:
        # Authentication errors (401)
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.data = {
                'status': 'error',
                'message': 'Unauthorized access. Please provide a valid authentication token.',
            }
        
        # Permission errors (403)
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            response.data = {
                'status': 'error',
                'message': 'You do not have permission to perform this action.',
            }
        
        # Not found errors (404)
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data = {
                'status': 'error',
                'message': 'Resource not found.',
            }
        
        # Validation errors (400)
        elif response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data = {
                'status': 'error',
                'message': 'Validation failed.',
                'errors': response.data,
            }

    return response
