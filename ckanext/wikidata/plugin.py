import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint
from ckan.common import request, config
from ckanext.wikidata.controller.wikidata import WikidataController


class WikidataPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('public/statics', 'ckanext-wikidata')


    def get_blueprint(self):

        blueprint = Blueprint(self.name, self.__module__)

        blueprint.template_folder = u'templates'
        blueprint.add_url_rule(
            u'/http://ckanchem11.test.service/fancy_type/<package_name>',
            u'generate_wikilink',
            WikidataController.generate_wikilink,
            methods=['POST']
        )
        ## To display the information
        blueprint.template_folder = u'templates'
        blueprint.add_url_rule(
            u'/http://ckanchem11.test.service/fancy_type/<package_name>',
            u'generate_wikilink',
            WikidataController.generate_wikilink,
            methods=['GET']
        )

        return blueprint

    def get_helpers(self):
       return {'wikidata_link': WikidataController.generate_wikilink}
