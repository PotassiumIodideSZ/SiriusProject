"""
Custom exceptions for shared functionality across all domains.
"""
from rest_framework.exceptions import APIException


class DomainException(APIException):
    """
    Base exception for domain-specific errors.
    """
    status_code = 400
    default_detail = 'A domain error occurred.'
    default_code = 'domain_error'


class ValidationException(APIException):
    """
    Exception for validation errors.
    """
    status_code = 400
    default_detail = 'Validation failed.'
    default_code = 'validation_error'


class ResourceNotFoundException(APIException):
    """
    Exception for when a resource is not found.
    """
    status_code = 404
    default_detail = 'Resource not found.'
    default_code = 'not_found'


class PermissionDeniedException(APIException):
    """
    Exception for permission-related errors.
    """
    status_code = 403
    default_detail = 'You do not have permission to perform this action.'
    default_code = 'permission_denied'


class ConflictException(APIException):
    """
    Exception for conflict errors (e.g., duplicate resources).
    """
    status_code = 409
    default_detail = 'A conflict occurred with the current state of the resource.'
    default_code = 'conflict'


class BusinessLogicException(APIException):
    """
    Exception for business logic errors.
    """
    status_code = 422
    default_detail = 'Business logic validation failed.'
    default_code = 'business_logic_error'
