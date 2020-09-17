CONTAINS_VALIDATORS = {
    # "domain": is_domain,
    # "ip": is_ip,
    # "hash": is_hash,
    "sha1": is_sha1,
    # "sha256": is_sha256,
    # "sha512": is_sha512,
    # "md5": is_md5,
    # "host name": is_hostname,
    # "mac address": is_mac,
    # "url": is_url,
    # "email": is_email
}


def is_sha1(maybe_sha):
    if len(maybe_sha) != 40:
        return False
    try:
        sha_int = int(maybe_sha, 16)
    except ValueError:
        return False
    return True


def get_list_from_string(list_string):
    return list_string.split(',')
