# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import CSVTable
from docutils.statemachine import StringList
from eagexp.image import export_image
from eagexp.partlist import raw_partlist, structured_partlist
from unipath import Path
import docutils.parsers.rst.directives.images
import logging

__version__ = '0.0.0'
   
log = logging.getLogger(__name__)
log.debug('sphinxcontrib.eagle (version:%s)' % __version__)


#class EagleError(Exception):
#    pass

parent = docutils.parsers.rst.directives.images.Image
images_to_delete = []
image_id = 0

class EagleImageDirective(parent):
    option_spec = parent.option_spec.copy()
    option_spec.update(dict(
#                       prompt=flag,
                       palette=directives.unchanged,
                       resolution=directives.unchanged,
                       timeout=directives.unchanged,
                       ))
    def run(self):
        palette = self.options.get('palette', 'white')
        resolution = self.options.get('resolution', 150)
        timeout = self.options.get('timeout', 20)
        
        #visible = 'visible' in self.options
        
        fname_sch = str(self.arguments[0])
        fname_sch = Path(fname_sch).expand().absolute()
        
        global image_id        
        fname_img = '%s.%s.png' % (fname_sch.name, str(image_id))
        image_id += 1
        fname_img_abs = Path(self.src).parent.child(fname_img)
        images_to_delete.append(fname_img_abs)

        export_image(fname_sch, fname_img_abs, palette=palette, resolution=resolution, timeout=timeout)
        
        self.arguments[0] = fname_img
        x = parent.run(self)

        return x
    
class EaglePartlistDirective(CSVTable):
    option_spec = dict(
                       raw=directives.flag,
                       timeout=directives.nonnegative_int,
                       header=directives.unchanged,
                       widths=directives.positive_int_list,
                       )

    def run(self):
        #timeout = 20 #default
        #if 'timeout' in self.options:
        #    timeout = self.options['timeout']
        
        timeout = self.options.get('timeout', 20)

        raw = 'raw' in self.options
        
        fname_sch = str(self.arguments[0])
        fname_sch = Path(fname_sch).expand().absolute()


        if raw:
            s = raw_partlist(fname_sch, timeout=timeout)
            node_class = nodes.literal_block
            elems = [node_class(s, s)]
        else:            
            (header, data) = structured_partlist(fname_sch, timeout=timeout)
            if 'header' in self.options:
                selected = self.options['header']
                selected = selected.split(',')     
                selected = [x.strip() for x in selected]     
            else:
                selected = header

            d = [','.join(['"' + dic[x] + '"' for x in selected]) for dic in data]
            selected = ','.join(['"' + x + '"' for x in selected])
            
            #self.options['header-rows'] = 1
            self.options['header'] = selected
            self.content = StringList(d)
            self.arguments[0] = ''
            elems = CSVTable.run(self)

        return elems

def cleanup(app, exception):
    for x in images_to_delete:
        f = Path(x)
        if f.exists():
            log.debug('removing image:' + x)
            f.remove()

def setup(app):
    #app.add_config_value('programoutput_use_ansi', False, 'env')
    #app.add_config_value('eagle_prompt_template',
    #                     '$ %(command)s\n%(output)s', 'env')
    app.add_directive('eagle-image', EagleImageDirective)
    app.add_directive('eagle-partlist', EaglePartlistDirective)
    app.connect('build-finished', cleanup)

#logging.basicConfig(level=logging.DEBUG)
