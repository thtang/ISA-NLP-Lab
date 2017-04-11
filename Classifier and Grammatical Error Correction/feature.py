def gen_feature_set(tags, offset):
    def tags_to_word_pos(tags):
        return " ".join((tag[0] + "_" + tag[2] for tag in tags))

    features = {}
    features['TGLR'] = tags_to_word_pos([tags[offset - 1], tags[offset + 1]]) if 0 < offset < len(tags) - 1 else ''
    features['TGL'] = tags_to_word_pos([tags[offset - 2], tags[offset - 1]]) if 1 < offset else ''
    features['TGR'] = tags_to_word_pos([tags[offset + 1], tags[offset + 2]]) if offset < len(tags) - 2 else ''
    features['BGL'] = tags_to_word_pos([tags[offset - 1]]) if 0 < offset else ''
    features['BGR'] = tags_to_word_pos([tags[offset + 1]]) if offset < len(tags) - 1 else ''
    return features
