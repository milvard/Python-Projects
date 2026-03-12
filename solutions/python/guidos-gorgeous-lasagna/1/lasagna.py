"""Λειτουργίες για την προετοιμασία της υπέροχης λαζάνιας του Guido."""

# Σταθερές για τους υπολογισμούς
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Υπολογίζει τον υπολειπόμενο χρόνο ψησίματος.
    
    :param elapsed_bake_time: int - ο χρόνος που η λαζάνια βρίσκεται ήδη στον φούρνο.
    :return: int - τα λεπτά που απομένουν βάσει της σταθεράς EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Υπολογίζει τον χρόνο προετοιμασίας βάσει των στρώσεων.
    
    :param number_of_layers: int - ο αριθμός των στρώσεων που θα προστεθούν.
    :return: int - συνολικά λεπτά προετοιμασίας (2 λεπτά ανά στρώση).
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Υπολογίζει τον συνολικό χρόνο που έχει δαπανηθεί μέχρι τώρα.
    
    :param number_of_layers: int - ο αριθμός των στρώσεων της λαζάνιας.
    :param elapsed_bake_time: int - τα λεπτά που η λαζάνια ψήνεται ήδη.
    :return: int - το άθροισμα του χρόνου προετοιμασίας και του χρόνου ψησίματος.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
