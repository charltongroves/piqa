r"""PyTorch Image Quality Assessement (PIQA)

The `piqa` package is divided in several submodules, each of
which implements the functions and/or classes related to a
specific image quality assessement metric.
"""

__version__ = '1.1.6'

from .tv import TV
from .psnr import PSNR
from .ssim import SSIM, MS_SSIM
from .lpips import LPIPS
from .gmsd import GMSD, MS_GMSD
from .mdsi import MDSI
from .haarpsi import HaarPSI
from .vsi import VSI
from .ssi import SSI
from .fsim import FSIM
