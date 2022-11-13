import luigi
from luigi.contrib.gcs import GCSTarget
from datetime import datetime
from _download_top_50_global import download_top_50_global

TIMESTAMP = datetime.now().strftime("%Y-%m-%d")


class DownloadGlobalTop50(luigi.Task):
    def output(self):
        return GCSTarget(
            f"gs://yo-personal-project/spotify/global_top_50/{TIMESTAMP}.csv"
        )

    def run(self):
        download_top_50_global()


if __name__ == "__main__":
    luigi.run()
