def can_publish(user):
    """
        发布商品的权限
    """
    if user.get('phone'):
        return True
    else:
        return False


def can_buy(user):
    """
        发布商品的权限
    """
    if user.get('phone') and user.get('realname'):
        return True
    else:
        return False


def is_newuser(user):
    """
        判断是否有昵称和头像
    """
    if user.get('realname') and user.get('head_url'):
        return False
    else:
        return True