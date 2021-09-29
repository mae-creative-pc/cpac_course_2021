import numpy as np
TEACHER_CODE=False
def sort_songs(audio_features):
    """"Receive audio features and sort them according to your criterion"

    Args:
        audio_features (list of dictionaries): List of songs with audio features

    Returns:
        list of dict: the sorted list
    """
    sorted_songs=[]

    # Random shuffle: replace it!
    if TEACHER_CODE:
        random_idxs=np.random.permutation(len(audio_features))
        for idx in random_idxs:
            sorted_songs.append(audio_features[idx])
    else:
        danceability=[]
        for song in audio_features:
            danceability.append(song["danceability"])
        idxs_sorted = np.argsort(danceability)
        ramp_up=idxs_sorted[0::2]
        ramp_down=idxs_sorted[1::2]
        ramp_down=ramp_down[::-1]
        for idx in ramp_up:
            sorted_songs.append(audio_features[idx])            
        for idx in ramp_down:
            sorted_songs.append(audio_features[idx])
    return sorted_songs