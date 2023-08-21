# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Callable
from abc import abstractmethod

# Pip
from selenium_account import SeleniumAccount

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------ class: SeleniumUploaderAccount ------------------------------------------------ #

class SeleniumUploaderAccount(SeleniumAccount):

    # --------------------------------------------------- Abstract methods --------------------------------------------------- #

    @abstractmethod
    def _upload_function(self) -> Callable:
        pass


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def upload_content(self, *args, **kwargs):
        return self._upload_function()(*args, **kwargs)


# -------------------------------------------------------------------------------------------------------------------------------- #