def mytag(request):
    """TODO: Docstring for mytag.

    :arg1: Ovim mytag zelim da napravim logiku za activ state u
    nav bar, kada ste na odredjenoj stranici da ta ista stranica
    bude osencena u navbar.
    Whit this I'm making logic for active state in navbar.
    :returns: mytag treba da vrati active state za navbar.
    mytag will return active state for navbar.

    """
    context = {'class': 'active'}
    return context
