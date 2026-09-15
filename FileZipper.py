import zipfile as zip
import pathlib as path

def ZipFiles(files, folder):
    DestPath = path.Path(folder, "Compressed")
    with zip.ZipFile(DestPath, "w") as archive:
        for file in files:
            file = path.Path(file)
            archive.write(file, arcname = file.name)

