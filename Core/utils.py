from graphene import relay


class CustomNode(relay.Node):
    class Meta:
        name = 'Node'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        model = only_type._meta.model
        return model.objects.get(id=global_id)


def user_verification(modeldataUser, user):
    """[User Verification]
    you can use the convenient user_verification function which raises a PermissionDenied
    exception when the informed users are not equal each other.

    Args:
        modeldataUser ([object]): [It is related with the user in your specific model]
        user ([object]): [It is related with the authenticated user who made the request]

    Raises:
        Exception: [raises a PermissionDenied
    exception when the informed users are not equal each other.]

    Returns:
        [bollean]: [return True
    if the informed users are not equal each other.]
    """
    if modeldataUser != user:
        raise Exception("You do not have permission to perform this action!")
    return True
