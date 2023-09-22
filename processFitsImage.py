import numpy as np
import matplotlib.pyplot as plt

# Define the path to the FITS file
fits_file = r"/home/robsteele49/git/gmnSoftware/FF_US0027_20230914_050005_245_0223744.fits"
#fits_file = r"/home/robsteele49/git/gmnSoftware/FF_US0027_20230914_051821_765_0251136.fits"
#fits_file = r"/home/robsteele49/git/gmnSoftware/FF_US0027_20230914_052907_367_0267264.fits"

# Open and read the FITS file
with open(fits_file, "rb") as file:
    header = file.read(2880)  # Read the header (assuming 2880 bytes)
    print(header)

    # Skip the data start position for other images
    start_data = [int.from_bytes(header[80:84], byteorder="big")]

    print ("start_data: ", start_data)
    
    for i in range(1, 5):
        print ("i : ", i)
        print (start_data[i-1])
        start_data.append(start_data[i - 1] + 921600)

    # Read and display image data
    for i in range(5):
        file.seek(start_data[i])

        print ("start_data[i]: ", start_data[i])
        
        try:
            img = np.fromfile(file, dtype=np.uint8, count=1280 * 720)

            print ("Try printing the image")
            
            # rob:
            try:
                plt.imshow(img, cmap='gray')
                plt.show()
            except Exception as e:
                print ("exc of Rob's test")
                
            print ("file     : ", file)
            print ("img.size : ", img.size)
            
            img = img.reshape(720, 1280)
        except Exception as e:
            print(f"Error reading file: {e}")

        plt.imshow(img, cmap='gray')
        plt.show()

# Close the file
file.close()
