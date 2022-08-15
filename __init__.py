from .mdcr_lpm import Mdcr_LPM


def create_instance(c_instance):
    return Mdcr_LPM(c_instance)
