from django.core.urlresolvers import reverse


class DetailURLMixin(object):

    def get_detail_url(self):
        return reverse(
            'api_{}_detail'.format(self.__class__.__name__.lower()),
            kwargs={'pk': self.id}
        )

    @classmethod
    def _get_reverse_url_helper(cls):
        return ''.join('-' + i.lower() if i.isupper()
                       else i for i in cls.__name__).strip('-')

    @classmethod
    def get_url_string(cls):
        t = 'api/{}/'
        return t.format(cls._get_reverse_url_helper())