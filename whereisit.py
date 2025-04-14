'''
Jmoody
4.2025 Wk 12 Tool Development 8 - whereisit.py
Citation: Python for Networking & Security vol 3 - JOrtega
Usage: Command to run the script (if running from directory where script is located):
run in a different terminal: python whereisit.py whereisit.jpg
'''

# import modules
import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import sys

# finding GPS info in exif data
# puts the gps data into a dictionary
def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

# converting gps coords from DMS to DD
def dms_to_dd(d, m, s, ref):
    decimal_degrees = d + float(m)/60 + float(s)/(60*60)
    if ref in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

# getting the latitude and longitude
def extract_gps_coords(exif_data):
    geotags = get_geotagging(exif_data)
    if not geotags:
        return None, None

    latitude = dms_to_dd(geotags['GPSLatitude'][0], geotags['GPSLatitude'][1], geotags['GPSLatitude'][2], geotags['GPSLatitudeRef'])
    longitude = dms_to_dd(geotags['GPSLongitude'][0], geotags['GPSLongitude'][1], geotags['GPSLongitude'][2], geotags['GPSLongitudeRef'])

    return latitude, longitude

# main function that uses argparse to accept an image file path from the command line.
def main():
    parser = argparse.ArgumentParser(description='Metadata from images')
    parser.add_argument('PICTURE_FILE', help='Path to the image file')
    args = parser.parse_args()

    # opening image and extracting the exif data
    img_file = Image.open(args.PICTURE_FILE)
    exif_data = img_file._getexif()

    # error handling
    if exif_data is None:
        print("No EXIF data found")
        sys.exit()

    # getting the coordiantes and printing a google maps link to the location.
    latitude, longitude = extract_gps_coords(exif_data)

    if latitude is not None and longitude is not None:
        print("GPS Coordinates: {}, {}".format(latitude, longitude))
        gmaps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print("Google Maps URL: {}".format(gmaps_url))

# main function block
if __name__ == "__main__":
    main()
