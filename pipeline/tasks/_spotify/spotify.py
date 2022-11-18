import luigi
from luigi.contrib.gcs import GCSTarget
from datetime import datetime
from prototypes._download_top_50_global import download_top_50_global
from prototypes._download_artists_in_global_top_50 import (
    download_artists_in_global_top_50,
)
from prototypes._get_all_audio_features_by_artist import (
    get_all_audio_features_by_artist,
)

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


class GetAudioFeaturesByArtist(luigi.Task):
    artist_id = luigi.Parameter()

    def output(self):
        return GCSTarget(
            f"gs://yo-personal-project/spotify/audio_features/{self.artist_id}.json"
        )

    def run(self):
        get_all_audio_features_by_artist(self.artist_id)


if __name__ == "__main__":
    luigi.run()
