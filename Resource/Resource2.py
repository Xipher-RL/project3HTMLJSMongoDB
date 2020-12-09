from cryptography.fernet import Fernet

# encrypted MongoDB Info x3 times
R0L = b'gAAAAABfwxz5w48wajF91bpGQNqq_lKS93r0mZEQaKGcgc2d0cnyxEEqOAqE6_-MoN8FWlqyjXbFELNYdNaN34p1vnvagUsfLMLbE3EZ7Ic7bslTuEIGlJT-tFCHRSHplsPARanVwMyzykWZ6wL4fu9wQzUL7lbpIjDMNlT5xDngu7maMMpGQVhaPNNvnLcvC4tiPpfh5wZMYal7V8lSNkwpuKPc3YUMfkaqIW62e_F8qyQenhRZQSeQ10k_V3hE4OhBd_rm6qDABNKNooh68Feh_ptwRQac690cWbvT8GBNa6yJutMZd0HmkNUjUPpQH6Tz2V-FpTQcvYms3FrW7WvHWpv5j-ayHHuB9utUTC0CEQl25VhV0uQsLiJsD9QfHlbyoMhJjMWU'
R0P = b'gAAAAABfwxz5DAXsEkhJjmSdQ39WxVukDNwphBJz5citRqYRpzWoj5juCOKSbS_XyaoEDLg-0JLtqvQ-vjJJjFTg9R_4dMsxeomNF-aFBtEd31ypWwBhz3-oxK4Xi5fNuhV6zOKaBupj8FxbMTPPjt02SCMNi6IdFP5Bkggj2pH2MvpThJcGgYOKlCIeZ5t_Md_rn-fIBzldaOwMagele_cldVre-yTKo5xEqGtAw4cn3bc-eEBTcImnJ9kbCdISAEz9Z-WzCxK4qy5yLKw9Z4t8c5YMpWGD01kKXNtfYM1j3Nnk6eldCj8PlmLvTYwy5XEoRWY4pExBpoZJJyfncTcsCRDhnmNnJdjFPxmCkHrSW9IVDyPectUASAI4ijuecNMoABopCQYlMEvU3yKG97FqLVplcL1xVw=='
R0O = b'gAAAAABfwxz5yLxbhqj7OMgrM44wOR8yEQfFlWoD8Uq0mEGQWlT52lI3-Ya2WKQczBffLwsEUAGcrHzZTkFqXC6ajnfCNgF7laQcNkF00TME1pPl2EJmCWtXuUsukoEFPtF8l9SyjJEQgTMY6gX7sF8OOhEzBhwpI6mJJ_lYFwDDam9wur2AAfShG1y810yjeka39b6PxK1jnM_25nkNMgI-AKgZmikv6uOqXjeQoucwzi6rIMTrDAT-jd-csJPoIa8WoTWdyt6Z2Xm22Ebc49oRMH4MLHqjUYIfgpTF5yVfsftMzDdzSzn1aqMJ0BvQIRroUeBvg5dFj1jsQSzpPeJCjgEPrTOfvjIWEgedUQUwSjLSQV4aOiR4AD_2dQOO4mko8oeC6KP1zvjrJ-1sn5JD3K8_R9Xb6g=='
R0DN = b'gAAAAABfwxz5bIiYcr74E2BXLpfqz0V_9l_gTe8VdjScH7ehq9jAi0Pv3LXcrCBg9M9u89YBal53Klkg--q6jU1GU1tDwn3eJbIhUITm-M6gYq51qLNiEAUXRrAluxKxsYdmRc7ISFS2UP4oO3WkJntjMEy461PctOGJsYGLiqZMhP-C1Y8-bUGN7BkXrOMrpcSVCMNsNPVd_cvfb_55Fy7UFr0rWa9dh5NY74_OBEjVEjFt0nrspsLH4hL6OL_xuyE_YYUzSvz2OSbSQ6goHD_eTujRzV-gwVPmoMGckCyrL1SyYcVbH2_2OKyF9bGFmVibN2AYLgBWXM_VXS3yXUhYk2cqBrMzY7YkfAiUhLRIQpbDRL12o9s6QJnJmKsL0edlxQll6Vqo'

gottenList2 = []


def getList2():
    # encryption key file
    with open('Resource/Resource3.ext', 'rb') as file:
        secret = file.read()

    cipher = Fernet(secret)

    # initial decryption pulls encrypted data from variables
    encrypted0 = cipher.decrypt(R0L)
    encrypted1 = cipher.decrypt(R0P)
    encrypted2 = cipher.decrypt(R0O)
    encrypted3 = cipher.decrypt(R0DN)

    # while loop iterates an addition 2 decryption steps for a total of 3
    i = 0
    while i <= 1:
        encrypted0 = cipher.decrypt(encrypted0)
        encrypted1 = cipher.decrypt(encrypted1)
        encrypted2 = cipher.decrypt(encrypted2)
        encrypted3 = cipher.decrypt(encrypted3)
        i += 1

    # converts byte data back to string data
    encrypted0 = encrypted0.decode()
    encrypted1 = encrypted1.decode()
    encrypted2 = encrypted2.decode()
    encrypted3 = encrypted3.decode()

    # list assembler for login data.
    gottenList2.append(encrypted0)
    gottenList2.append(encrypted1)
    gottenList2.append(encrypted2)
    gottenList2.append(encrypted3)

    return gottenList2
