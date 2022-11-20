from _spotify.rertireve_standardised_audio_features import (
    retirieve_standardised_audio_features,
)


def test_retirieve_standardised_audio_features():
    res = retirieve_standardised_audio_features("2IqjKEBiz0CdLKdkXhxw84")

    metrics = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms",
    ]

    assert type(res) == dict
    assert res.keys() == set(metrics)
