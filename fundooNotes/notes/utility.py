import json
import logging

from django.core.exceptions import ObjectDoesNotExist

from .redis import RedisCode


class Cache:

    def add_note_to_cache(self, user_id, note):
        """
        for adding the note in catch
        :param user_id: user_id of the person
        :param note: note details
        :return: id and data
        """
        try:
            note_list = RedisCode().get(user_id)
            if note_list is None:
                RedisCode().cache.set(user_id, json.dumps([note]))
            else:
                note_list = json.loads(note_list)
                note_list.append(note)
                RedisCode().cache.set(user_id, json.dumps(note_list))
                return
        except Exception as e:
            logging.error(e)

    def get_note_from_cache(self, user_id):
        """
        for geting note from catch
        :param user_id: user_id of the person
        :return: user_id
        """
        try:
            RedisCode().cache.get(user_id)
        except Exception as e:
            raise e

    def update_note_to_cache(self, user_id, note):
        """
        for updating the note in cache
        :param user_id: id of note
        :param note: note details
        :return: updated note list
        """
        note_list = RedisCode().get(user_id)
        if note_list is None:
            RedisCode().cache.set(user_id, json.dumps([note]))
            return
        for note in note_list:
            if RedisCode().cache.get(user_id):
                note.set(note)
                note_list.append(note)
                return
        else:
            raise ObjectDoesNotExist

    def delete_note_to_cache(self, id):
        """
        for deleting the note from cache
        :param id: id of the note
        :return: note list
        """
        note_list = RedisCode().cache.get(id)
        if note_list is None:
            raise ObjectDoesNotExist
        for note in note_list:
            if RedisCode().cache.get(id) == note.pk:
                del(note)
                return
        else:
            raise ObjectDoesNotExist
