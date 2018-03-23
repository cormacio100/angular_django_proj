from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        #   verifies whether action is allowable
        if request.method in permissions.SAFE_METHODS:
            return True

        #   if the if does NOT return true
        #   The creator/owner can EDIT the object
        #   Other users can only VIEW it
        return obj.owner == request.user