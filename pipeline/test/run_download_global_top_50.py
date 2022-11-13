import sys

sys.path.append("..")
from tasks._spotify import spotify
import luigi

luigi.build([spotify.DownloadGlobalTop50()])
