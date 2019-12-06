def get_formatted_name(firstname,lastname,midname = ""):
    if midname:
        fullname = firstname + " " + midname + " " + lastname
    else:
        fullname = firstname + " " + lastname
    return fullname.title()