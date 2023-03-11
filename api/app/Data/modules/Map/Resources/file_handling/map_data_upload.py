from typing import Any
from flask import request
import geopandas as gpd
import zipfile
import os
from shutil import rmtree
from app import db


class MapDataUpload:
    __doc__ = 'Class to upload and extract data from zip file'
    file: str = ''
    atr: str = ''
    zip_file: Any 

    def __init__(self, file, atr):
        self.file = file
        self.atr = atr


    def upload(self):
        try:
            self.file.save(os.path.join('app/Data/repository', self.file.filename))
            return {"Message":"File uploaded"}, 201
        except:
            return {"Error":"File not uploaded"}, 404


    def extract_zip(self):
        try:
            zip_file = zipfile.ZipFile(self.file)
            self.zip_file = zip_file
            for f in zip_file.namelist():
                if 'SHP' in f:
                    zip_file.extract(f, 'app/Data/repository')

            shp = gpd.read_file('app/Data/repository/' + f)
            return shp
        except Exception as e:
            return {"Error":f"File not extracted {e}"}, 404


    def delete_file(self):
        try:
            os.remove((os.path.join('app/Data/repository', self.file.filename)))
            return {"Message":"File deleted"}, 200
        except:
            return {"Error":"File not deleted"}, 404


    def clean_folder(self):
        try:
            rmtree('app/Data/repository/' + self.file.filename.replace('.zip', ''))
        except Exception as e:
            return {"Error":f"File not {e}"}, 404

    def correct_table_name(self):
        try:
            sql = 'ALTER TABLE "' + self.file.filename.replace('.zip', '') + '" RENAME TO ' + self.file.filename.replace('.zip', '')
            db.engine.execute(sql)
        except Exception as e:
            return {"Error":f"File not {e}"}, 404


    def create_color_column(self):
        try:
            sql = 'ALTER TABLE ' + self.file.filename.replace('.zip', '') + ' ADD COLUMN colors text'
            db.engine.execute(sql)
            rename_atr = 'ALTER TABLE ' + self.file.filename.replace('.zip', '') + ' RENAME COLUMN "' + self.atr + '" TO '  + self.atr
            db.engine.execute(rename_atr)
        except Exception as e:
            return {"Error":f"File not {e}"}, 404


    def create_table(self):
        try:
            shp = self.extract_zip()
            shp.to_postgis(self.file.filename.replace('.zip', ''), db.engine, if_exists='replace', index=True, index_label='Index')
            self.correct_table_name()
            self.create_color_column()
        except Exception as e:
            return {"Error":f"{e}"}, 404

    
    def upload_proccess(self):
        try:
            self.upload()
            self.create_table()
            self.clean_folder()
            self.delete_file()
        except Exception as e:
            return {"Error":f"{e}"}, 404

            
