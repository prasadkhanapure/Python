test_settings = {
        'theme': 'dark',
        'notifications': 'enabled',
        'volume': 'high'
    }

def add_setting(test_settings, new_user):

    key, value = new_user
    key = key.lower()

    if isinstance(value,str):
        value = value.lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    
add_setting({'theme': 'light'}, ('THEME', 'dark'))

def update_setting(test_settings, update_user):
    key, value = update_user
    key = key.lower()

    if isinstance(value,str):
        value = value.lower()
    
    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings, key):

    if not isinstance(key,str): return
    key = key.lower()

    if key in test_settings:
        test_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else: return "Setting not found!"

def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    else:
        # print("Current User Settings:")
        result = "Current User Settings:\n"
        for key, value in test_settings.items():
            # print(f"{key.capitalize()}: {value}")
            result += f"{key.capitalize()}: {value}\n"
    return result

add_setting(test_settings, ('Language', 'English'))
update_setting(test_settings, ('VOLUME', 'MEDIUM'))
delete_setting(test_settings, 'LANGUAGE')
view_settings(test_settings)