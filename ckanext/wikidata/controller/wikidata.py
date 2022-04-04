from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import ckan.plugins.toolkit as toolkit
from flask import render_template


class WikidataController():
    def generate_wikilink(package_name):
        sparql = SPARQLWrapper("http://query.wikidata.org/sparql")

        # package_name = request.form.get('package')
        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        try:

            inchi_key = package['inchi_key']

        #inchi_key = "WIGYSAIZPJAWDF-IZZDOVSWSA-N"

            if inchi_key:
                wiki_query = """
                    SELECT ?compound ?inchikey
                    WHERE
                    {
                            ?compound wdt:P31 wd:Q11173; #Instance of Chemical Compound
                            wdt:P235 ?inchikey    #all the chemical compounds with their InChI
                            FILTER (STR(?inchikey) = "%s")
                        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
                    }
                    """ % inchi_key

                sparql.setQuery(wiki_query)  # set query using SPARQL
                sparql.setReturnFormat(JSON)  # Converting scrapped information JSON
                results = sparql.query().convert()

                results_df = pd.json_normalize(results['results']['bindings'])  # JSON information to human readable table
                link_generated = results_df.values
                return results_df['compound.value'].values
            else:
                return "0"
                #if results_df.all():
                #   return type(results_df)
                #else:
                #   return type(results_df)
        except:
            pass








































