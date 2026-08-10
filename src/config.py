CONFIG = {
    "classes": [
        "OOK",
        "BPSK",
        "QPSK",
        "AM-DSB-WC",
        "AM-DSB-SC",
        "FM"
    ],

    "snrs": [
        -10,
        -4,
        0,
        4,
        10,
        16,
        20
    ],

    "samples_per_class_snr": 1000,

    "train_ratio": 0.70,
    "validation_ratio": 0.15,
    "test_ratio": 0.15,

    "seed": 42,

    "batch_size": 128,
    "epochs": 30,
    "learning_rate": 0.001
}