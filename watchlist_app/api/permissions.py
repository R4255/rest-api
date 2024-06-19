#this .py file is to create our own custom permission and we import it in the views.py file
from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            #safe method refers to the get method
            return True
        else:
            return bool(request.user and request.user.is_staff)#this basically return true if he is an admin   


#also we want that if i am the review owner i should also have the other options other than GET
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #check permissions for read only request
            return True
        else:
            #check permissions for write only
            return obj.review_user==request.user
        
