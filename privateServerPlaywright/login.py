def telalogin(page):
    try:
        page.wait_for_selector('#login_username')
        page.wait_for_selector('#login_password')
        page.wait_for_selector('#loginsubmit')

        page.fill('#login_username', config.login_data['username'])
        page.fill('#login_password', config.login_data['password'])
        page.click('#loginsubmit')
        return True
    except:
        return False