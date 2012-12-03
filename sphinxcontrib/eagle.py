# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import CSVTable
from docutils.statemachine import StringList
from eagexp.image import export_image
from eagexp.image3d import export_image3d
from eagexp.partlist import raw_partlist, structured_partlist
from path import path
import docutils.parsers.rst.directives.images
import logging
import os

__version__ = '0.0.7'

log = logging.getLogger(__name__)
log.debug('sphinxcontrib.eagle (version:%s)' % __version__)

ENABLE_CACHE = 1

# class EagleError(Exception):
#    pass

parent = docutils.parsers.rst.directives.images.Image
images_to_delete = []
image_id = 0


def init_cache(app):
    create = False
    if hasattr(app.env, 'eagle_cache'):
        if app.env.eagle_cache_version != __version__:
            log.debug('cache version mismatch: %s!=%s' % (
                app.env.eagle_cache_version, __version__))
            create = True
    else:
        log.debug('missing cache')
        create = True
    if create:
        log.debug('creating cache')
        app.env.eagle_cache = dict()
        app.env.eagle_cache_version = __version__
    init_cache.cache = app.env.eagle_cache
#    init_cache.cache_old_keys = app.env.eagle_cache.keys()
    init_cache.cache_new_keys = set()


def do_action(fname_sch, fname_img_abs, directive, export_func):
    if not ENABLE_CACHE:
        return export_func(fname_sch, fname_img_abs)

    cache = init_cache.cache

    # dict is not hashable -> convert it
    options = str(sorted(directive.options.items()))

    cache_key = str(
        fname_sch), fname_sch.mtime, options, directive.__class__.__name__
    if cache_key in cache.keys():
        last_data = cache[cache_key]
        log.debug('found in cache:%s' % str(cache_key))
        if fname_img_abs:
            open(fname_img_abs, 'wb').write(last_data)
    else:
        log.debug('not in cache: %s' % str(cache_key))
        last_data = export_func(fname_sch, fname_img_abs)
        if fname_img_abs:
            assert last_data is None
            last_data = open(fname_img_abs, 'rb').read()
        cache[cache_key] = last_data
    init_cache.cache_new_keys.add(cache_key)
    return last_data


def get_fname(self):
    fname_sch = str(self.arguments[0])
    cwd = path.getcwd()
    os.chdir(path(self.src).parent)
    fname_sch = path(fname_sch).expand().abspath()
    os.chdir(cwd)
    return fname_sch


class EagleImage3dDirective(parent):
    option_spec = parent.option_spec.copy()
    option_spec.update(dict(
                       timeout=directives.nonnegative_int,
                       size=directives.unchanged,
                       pcbrotate=directives.unchanged,
                       ))

    def run(self):
        timeout = self.options.get('timeout', 20)

        size = self.options.get('size', '800x600')
        size = map(int, size.split('x'))

        pcbrotate = self.options.get('pcbrotate', '0,0,0')
        pcbrotate = map(int, pcbrotate.split(','))

        fname_sch = get_fname(self)

        global image_id
        fname_img = '%s_3d_%s.png' % (
            fname_sch.name.replace('.', '_'), str(image_id))
        image_id += 1
        fname_img_abs = path(self.src).parent / fname_img

        def export_func(fname_sch, fname_img_abs):
            export_image3d(fname_sch, fname_img_abs, size=size,
                           timeout=timeout, pcb_rotate=pcbrotate)
        do_action(fname_sch, fname_img_abs, self, export_func)
        images_to_delete.append(fname_img_abs)

        self.arguments[0] = fname_img
        x = parent.run(self)

        return x


class EagleImageDirective(parent):
    option_spec = parent.option_spec.copy()
    option_spec.update(dict(
                       palette=directives.unchanged,
                       resolution=directives.unchanged,
                       timeout=directives.nonnegative_int,
                       mirror=directives.flag,
                       layers=directives.unchanged,
                       command=directives.unchanged,
                       ))

    def run(self):
        palette = self.options.get('palette', 'white')
        resolution = self.options.get('resolution', 150)
        timeout = self.options.get('timeout', 20)
        command = self.options.get('command', None)

        mirror = 'mirror' in self.options

        layers = self.options.get('layers', None)
        if layers:
            layers = layers.split(',')

        fname_sch = get_fname(self)

        global image_id
        fname_img = '%s_%s.png' % (
            fname_sch.name.replace('.', '_'), str(image_id))
        image_id += 1
        fname_img_abs = path(self.src).parent / fname_img

        self.arguments[0] = fname_img
        x = parent.run(self)

        def export_func(fname_sch, fname_img_abs):
            export_image(fname_sch, fname_img_abs, palette=palette, resolution=resolution, timeout=timeout, layers=layers, mirror=mirror, command=command)
        do_action(fname_sch, fname_img_abs, self, export_func)
        images_to_delete.append(fname_img_abs)

        return x


class EaglePartlistDirective(CSVTable):
    option_spec = dict(
        raw=directives.flag,
        timeout=directives.nonnegative_int,
        header=directives.unchanged,
        widths=directives.positive_int_list,
    )

    def run(self):
        # timeout = 20 #default
        # if 'timeout' in self.options:
        #    timeout = self.options['timeout']

        timeout = self.options.get('timeout', 20)

        raw = 'raw' in self.options

        fname_sch = get_fname(self)

        elems = []
        if raw:
            def export_func(fname_sch, fname_img_abs):
                return raw_partlist(fname_sch, timeout=timeout)
            s = do_action(fname_sch, None, self, export_func)
        else:
            def export_func(fname_sch, fname_img_abs):
                return structured_partlist(fname_sch, timeout=timeout)
            (header, data) = do_action(fname_sch, None, self, export_func)

        if raw:
            node_class = nodes.literal_block
            elems = [node_class(s, s)]
        else:
            if 'header' in self.options:
                selected = self.options['header']
                selected = selected.split(',')
                selected = [x.strip() for x in selected]
            else:
                selected = header

            d = [','.join(
                ['"' + dic[x] + '"' for x in selected]) for dic in data]
            selected = ','.join(['"' + x + '"' for x in selected])

            # self.options['header-rows'] = 1
            self.options['header'] = selected
            self.content = StringList(d)
            self.arguments[0] = ''
            elems = CSVTable.run(self)

        return elems


def cleanup_cache():
    unused = [x for x in init_cache.cache.keys(
    ) if x not in init_cache.cache_new_keys]
    for x in unused:
        log.debug('removing key from cache:' + str(x))
        del init_cache.cache[x]


def cleanup(app, exception):
    for x in images_to_delete:
        f = path(x)
        if f.exists():
            log.debug('removing image:' + x)
            f.remove()
    if ENABLE_CACHE:
        cleanup_cache()


def setup(app):
    # app.add_config_value('programoutput_use_ansi', False, 'env')
    # app.add_config_value('eagle_prompt_template',
    #                     '$ %(command)s\n%(output)s', 'env')
    app.add_directive('eagle-image', EagleImageDirective)
    app.add_directive('eagle-partlist', EaglePartlistDirective)
    app.add_directive('eagle-image3d', EagleImage3dDirective)
    app.connect('build-finished', cleanup)
    app.connect('builder-inited', init_cache)

# logging.basicConfig(level=logging.DEBUG)
