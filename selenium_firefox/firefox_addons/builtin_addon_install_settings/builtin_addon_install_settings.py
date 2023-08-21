# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
import os

# Pip
from selenium_browser import AddonInstallSettings

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Defines ----------------------------------------------------------- #

RESOURCES_FOLDER_NAME = 'resources'


# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- class: BuiltinAddonInstallSettings ---------------------------------------------- #

class BuiltinAddonInstallSettings(AddonInstallSettings):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(self):
        if not self._name.endswith('.xpi'):
            self._name += '.xpi'

        super().__init__(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                RESOURCES_FOLDER_NAME,
                self._name
            )
        )


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    _name: str = ''


# -------------------------------------------------------------------------------------------------------------------------------- #