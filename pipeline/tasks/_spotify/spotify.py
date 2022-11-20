from datetime import datetime
import luigi
from _retrieve_playlist_audio_features import retrieve_playlist_audio_features


TIMESTAMP = datetime.now().strftime("%Y-%m-%d")


class RetrieveAudioFeaturesGlobal(luigi.Task):
    playlistId = luigi.Parameter()

    def run(self):
        retrieve_playlist_audio_features(self.playlistId)


if __name__ == "__main__":
    luigi.run()
