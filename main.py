import fcsparser


if __name__ == '__main__':
    path = "FlowRepository_FR-FCM-ZY87_files/151110_ASE001_758_moDC_DV2_8h.fcs"
    meta, data = fcsparser.parse(
        path,
        reformat_meta=True,
        meta_data_only=False,
    )

    channels = meta["_channel_names_"]
    isotopes_proteins = {}
    for i, e in enumerate(channels):
        key = f"$P{i+1}S"
        if key not in meta.keys():
            continue
        isotopes_proteins[e] = meta[key]
    print(isotopes_proteins)
    data = data.drop(["Time", "Event_length"], axis=1)

    data = data.drop(list(set(isotopes_proteins.keys()) ^ set(data.columns)), axis=1)
    data.columns = [f"{isotopes_proteins[c]}:{c}" for c in data.columns]
    print(data)
