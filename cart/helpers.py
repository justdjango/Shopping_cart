import random
import string


def get_reference_code(model_name):
    random_chars = "".join([random.choice(string.ascii_letters + string.digits) for n in range(40)])
    if not model_name.objects.filter(ref_code=random_chars).exists():
        return random_chars
    else:
        return get_reference_code(model_name)
