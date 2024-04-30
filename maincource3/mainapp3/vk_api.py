import vk_api

def get_name_from_vk(access_token, user_id):
    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()
    response = vk.users.get(user_ids=user_id, fields='first_name,last_name')
    user = response[0]
    first_name = user['first_name']
    last_name = user['last_name']
    
    return first_name, last_name