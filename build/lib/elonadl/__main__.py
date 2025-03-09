from Download import *
from Extract import *
from Desktop import *

if __name__ == '__main__':

    # Old Repo:
    #GH_API_CGX = "https://api.github.com/repos/Ruin0x11/ElonaPlusCustom-GX/releases/latest"

    GH_API_ELONA = "https://api.github.com/repos/vichmartins/ElonaPlusCGXDownload/releases/latest"
    GH_API_CGX = "https://api.github.com/repos/JianmengYu/ElonaPlusCustom-GX/releases/latest"
    ELONA_FILE_NAME = 'elona.zip'
    CGX_FILE_NAME = 'cgx.7z'
    SHORTCUT_NAME = 'ElonaPlusCGX'

    def main():
        print("downloading latest version of Elona+ to your %APPDATA% folder")
        elona = Download(file_name=ELONA_FILE_NAME, link=GH_API_ELONA)
        elona.create_file()
        elona.get_file()

        print("downloading latest version of CustomGX variant.")
        cgx = Download(file_name=CGX_FILE_NAME, link=GH_API_CGX)
        cgx.create_file()
        cgx.get_file()

        print("extracting Elona+")
        e = Extract(elona.get_name())
        e.extract_zip()

        print("setting up CustomGX")
        c = Extract(cgx.get_name())
        c.extract_zip()
        print("DONE!")

        print("Creating Desktop Shortcut")
        path = e.find_latest_version()
        version = e.scrape_version()
        d = Desktop(name=SHORTCUT_NAME, path=path, version=version)
        d.create_shortcut()

    main()
