import luigi
from luigi.contrib.gcs import GCSTarget
from datetime import datetime
from _download_top_50_global import download_top_50_global
from _download_artists_in_global_top_50 import download_artists_in_global_top_50

TIMESTAMP = datetime.now().strftime("%Y-%m-%d")


class DownloadGlobalTop50(luigi.Task):
    def output(self):
        return GCSTarget(
            f"gs://yo-personal-project/spotify/global_top_50/{TIMESTAMP}.csv"
        )

    def run(self):
        download_top_50_global()


class DownloadArtistGlobalTop50(luigi.Task):
    def output(self):
        return GCSTarget(
            f"gs://yo-personal-project/spotify/artists_in_global_top_50/{TIMESTAMP}.json"
        )

    def run(self):
        download_artists_in_global_top_50()


if __name__ == "__main__":
    luigi.run()
