from datetime import datetime
import luigi
from luigi.contrib.gcs import GCSTarget
from datetime import datetime
import pandas as pd
from _auth.get_project_id import get_project_id
from _auth.google_auth import google_auth
from _logging.logger import Logger
from _spotify.retrieve_playlist_audio_features import retrieve_playlist_audio_features


TIMESTAMP = datetime.now().strftime("%Y-%m-%d")

google_auth()


def save_playlist_audio_features_as_csv(data: dict, playlist_id: str) -> None:
    output_path = f'gs://{get_project_id()}/spotify/audio_features/{playlist_id}/{datetime.today().strftime("%Y-%m-%d")}.csv'

    pd.DataFrame(data).to_csv(
        output_path,
        index=False,
        encoding="utf-8",
    )

    logger = Logger()
    logger.info(f"{output_path} is uploaded.")


class RetrieveAudioFeaturesGlobal(luigi.Task):
    playlistId = luigi.Parameter()
    output_path = f'gs://{get_project_id()}/spotify/audio_features/{playlistId}/{datetime.today().strftime("%Y-%m-%d")}.csv'

    def run(self):
        data = retrieve_playlist_audio_features(self.playlistId)
        save_playlist_audio_features_as_csv(data, self.playlistId)

    def output(self):
        GCSTarget(self.output_path)


if __name__ == "__main__":
    luigi.run()
