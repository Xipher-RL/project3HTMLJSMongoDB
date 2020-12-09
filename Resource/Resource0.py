from cryptography.fernet import Fernet

# encrypted MongoDB Info x3 times
R0L = b'gAAAAABfwxkMXlO7c34sn6lCbOIh_c51b6rZWE-b-FdVGXRbq4-swxQc1rFOo8WUSgmoeZTP_W4WITKzXthyTIQsEe-9Owoj-vgIqOd0RwSq5JkiocN2AucoJp5Prswf-5YR-D452RKZiZNz3sSAbxK05Fswjw6HXnRqkTeAreppE-XaYnRlAu3c0R9VMHbM5dyVmnBA0VqiihVoQ3zPRiew4FG4vAUz81tvnyLD2cZTkh_c96NdsWQSKGCO0o8M5YipQ5LLCDhQagw47nue6rQgQ6fFQJAgWL2_Rq23m48J_dQCrLmAOky1e8Vh_sXHAieoUClxM1WHEMfipLCNZbz0iwBEIgOTyFKxeSDhjfV3-SZX1Nl8sNFMYphcjVYHPZLY1_lzmpkv'
R0P = b'gAAAAABfwxkM1-lohrNypoosx4javKovu_OTF0SfDEI6Wq-6Oxvoe6NJUsupV0oftbxabEGGGdqOO76HBg0FI1vbRgNWim_6ZIl_bP4gcskV4yqutCl0F8cO9tsVwAMDJ9ngPQzzs6u6w3jHmcNYzfZzD8wZigF8c7vWdtYACgmEKsY3IbbnXjg6fyqx3Q4Di7LjMkYsY7V-5SVoQNqVrTpFOIyv2wx0nbWrVUBDv6klCFd0Nxu3gfJYO93QWA53YlHy_SeWrB0N614PNwKfB0eAh9AIQNY_MvRhLc_gsXn3orJvHCfK36jB97kuCRowkS0CNggEz_cEZORM_AXXrC-Rte61ZNKmynnugdZYwJM5aGRsTZAxY_7l708q8KhPhZsnqVbevVRt9q0Y4KFBpOcNQgwI19QC7A=='
R0O = b'gAAAAABfwxkMqQz-VLSi5shFDILR7U9XWukp4Y9G41x5OSfks2YPaDp9OMJS-ef7SpYCgSPL89OkRNVFUJN_Ze0B-5fa-51FlZKMb_DGZ1ynEUbYtlLATolqm2n2d3ZLTjf55dPzAD2Dn-n_lX1VpiJTamacHZsqaWRf6qM55OqnZGkYnrAolbUR0SddpL1Lams6QZWhN4OTJM6yv1dFmAV0g6Na8W17Uvr38dCDXa3SJwW2hcS-r8EbhfX0x7d8cBvfA7ZxJ-WmCtkRUd5IzS_XEceMFdzFoZUebJ7PsBTIknH2CRhLenBnSEqRLdGGTaQm5t7BD4PV0yw0WDpD2NCF5jdzEojKEyM6IbUJbxXOsHio_dxOnSnIV9pLmfx1hxyuXavvysJnjsXxjWrGRcjI2POM4FMKKA=='
R0DN = b'gAAAAABfwxkM4p5Jvhj0BjH0oyV6Pplo_djZwlXNapEpfE1cgexsCDAtUald6pAP8I7LXPnYrbMR0vaxYV8UMdZMY1CuJ7H0omQix19l_Vg0QhRvkTsWw5u9Ooh89de589CajW60_LCLSOq0nkCI__FKpL_01Xou_B9P89tvRuM5OubHh8GbaHkJ9h8CfVn_X5wQxth1pywiXU3tpaKhUJQMJnk1Ix6iYl1J8zC4Kk9MRx6ErNQ1-ofN2qTK_-122Utfc_BZ1e6a1xhzmPQwi-lrzfX_OT157Jw9SiO9xNtldf5uRHURcfR8X5sQ_Tx1WGGHo9wI--5sHCXrgcpBXPKOZu3c5BH2WLUlHb1JFYDe0S2mVBaw-C3nqkeXPTxCSpcLjiS8jFy0'

gottenList = []


def getList():
    # encryption key file
    with open('Resource/Resource1.ext', 'rb') as file:
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
    gottenList.append(encrypted0)
    gottenList.append(encrypted1)
    gottenList.append(encrypted2)
    gottenList.append(encrypted3)

    return gottenList
