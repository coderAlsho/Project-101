import os
import dropbox

class TransferData:

    def upload_file(self):
        for roots, dires, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

            dbx = dropbox.Dropbox(self.access_token)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox.path, mode = WriteMode('override'))
                TransferData()

                def Main():

                    access_token = "*******"

                    file_from = 'sample.txt'
                    file_to = '/Project 101/big.txt'

                    TransferData.upload_file(file_from, file_to)
                    Main()



                    
