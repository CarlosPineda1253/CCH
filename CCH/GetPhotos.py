import facebook
import wget
import os.path
import magic
import re
import secrets_tokens


class FacePhotosVideos:
    def __init__(self):
        self.list_photos_local = list()
        self.list_photos_face = list()
        self.list_videos_local = os.listdir('videos/')
        self.list_videos_face = list()
        self.graph = facebook.GraphAPI(access_token=secrets_tokens.my_token, version='3.1')

    def update_photos(self):
        self.get_photos_face()
        self.get_photos_local()
        self.get_diff_list_photos()

    def get_photos_face(self):
        albums = self.graph.get_all_connections(id='me', connection_name='albums')
        for ind1, album in enumerate(albums):
            photos = self.graph.get_all_connections(id=album['id'], connection_name='photos')
            for ind2, photo in enumerate(photos):
                self.list_photos_face.append(photo['id'])

    def get_photos_local(self):
        self.list_photos_local = os.listdir('photos/')
        for item in self.list_photos_local:
            self.list_photos_local[self.list_photos_local.index(item)] = item.split('.')[0]

    def get_diff_list_photos(self):
        set_photos_local = set(self.list_photos_local)
        set_photos_face = set(self.list_photos_face)
        print(set_photos_face.difference(set_photos_local))
        set_del = set_photos_local - set_photos_face
        set_add = set_photos_face - set_photos_local
        list_photos_add = list(set_add)
        list_photos_del = list(set_del)
        if list_photos_add:
            self.download_photos(list_photos_add)
        if list_photos_del:
            self.delete_photos(list_photos_del)

    @staticmethod
    def download_photos(list_photos_add):
        mime = magic.Magic(mime=True)
        for photo in list_photos_add:
            if not os.path.exists('photos/' + photo):
                url = 'https://graph.facebook.com/' + photo + '/picture?access_token=' + secrets_tokens.my_token + '&fields=full_picture'
                filename = 'photos/' + photo
                wget.download(url, out= filename)
                type_file = mime.from_file(filename)
                type_file, extension = type_file.split('/')
                if type_file == 'image':
                    os.rename(filename, filename + '.' + extension)

    @staticmethod
    def delete_photos(list_photos_del):
        for photo in list_photos_del:
            re_filename = re.compile(str(photo) + r'\.\w+')
            str_photos = ' '.join([str(elem) for elem in os.listdir('photos/')])
            photo_filename = re_filename.search(str_photos)
            os.remove('photos/' + photo_filename)


if __name__ == '__main__':
    app = FacePhotosVideos()
    app.update_photos()
