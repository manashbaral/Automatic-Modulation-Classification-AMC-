import h5py

filename="E:\\AMC\\datasets\\RadioMl2018\\GOLD_XYZ_OSC.0001_1024.hdf5"

with h5py.File(filename, 'r') as f:
    print("=== Dataset Information ===")
    print("-" * 50)

    #printing the keys of the HDF5 file
    print("X Shape:",f['X'].shape)
    print("Y Shape:",f['Y'].shape)
    print("Z Shape:",f['Z'].shape)

    #printing the data types of the datasets
    print("-" * 50 )
    print("\n Data Types:")
    print("X Type:",f['X'].dtype)
    print("Y Type:",f['Y'].dtype)
    print("Z Type:",f['Z'].dtype)

    #printing the first  samples of each dataset
    print("-" * 50)
    print("\n First 5 Samples:")
    print(f["X"][0])  # Print first  samples of X
    print(f["Y"][0])  # Print first  samples of Y
    print(f["Z"][0])  # Print first  samples of Z

    #printing the size and shape of each dataset
    print("-" * 50)
    print("\nDataset Sizes and Shapes:")
    print("X Size:", f['X'].size, "Shape:", f['X'].shape)
    print("Y Size:", f['Y'].size, "Shape:", f['Y'].shape)
    print("Z Size:", f['Z'].size, "Shape:", f['Z'].shape)

    #maping the Y dataset to its corresponding modulation types with a help of dataset description
    print("-" * 50)
    print("\n Modulation Types Mapping:")

    