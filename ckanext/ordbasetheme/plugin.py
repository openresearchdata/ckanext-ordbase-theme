# -*- coding: utf-8 -*-

from pylons import config

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


def get_biggest_groups(n):
    """Returns the n biggest groups, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'all_fields': True,
        'sort': 'packages'
    }
    groups = tk.get_action('group_list')(context, data_dict)
    if len(groups) > n:
        return groups[-1:-(n+1):-1]
    else:
        return groups[::-1]


def get_newest_groups(n):
    """Returns the n most recently updated groups, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'all_fields': True,
    }
    groups = tk.get_action('group_list')(context, data_dict)

    # The group_list action does not return an updated/created date for the groups.
    # This is probably super slow but let's try it.
    for group in groups:
        data_dict = {
            'id': group['id']
        }
        group['last_revision'] = tk.get_action('group_revision_list')(context, data_dict)[0]['timestamp']

    if len(groups) > n:
        return sorted(groups, key=lambda group: group['last_revision'])[-1:-(n+1):-1]
    else:
        return sorted(groups, key=lambda group: group['last_revision'])[::-1]


def get_popular_datasets(n):
    """Returns the n most viewed datasets, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'sort': 'views_total desc',
        'q': 'type:dataset'
    }
    datasets = tk.get_action('package_search')(context, data_dict)['results']
    if len(datasets) > n:
        return datasets[-1:-(n+1):-1]
    else:
        return datasets[::-1]


def get_newest_datasets(n):
    """Returns the n most recently created datasets, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'sort': 'metadata_created desc',
        'q': 'type:dataset'
    }
    datasets = tk.get_action('package_search')(context, data_dict)['results']
    if len(datasets) > n:
        return datasets[-1:-(n+1):-1]
    else:
        return datasets[::-1]


def get_ordbasetheme_config(option):
    # Get the value of the ckan.ordbasetheme.xy
    # setting from the CKAN config file as a string, or False if the setting
    # isn't in the config file.
    return config.get('ckan.ordbasetheme.' + option, False)

def remove_facets(facets_dict, facets_to_remove):
    for facet in facets_to_remove:
        try:
            del facets_dict[facet]
        except KeyError:
            pass
    return facets_dict


class OrdBaseThemePlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IFacets)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('fanstatic', 'ordbasetheme')

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def get_helpers(self):
        return {
            'get_biggest_groups': get_biggest_groups,
            'get_newest_groups': get_newest_groups,
            'get_popular_datasets': get_popular_datasets,
            'get_newest_datasets': get_newest_datasets,
            'get_ordbasetheme_config': get_ordbasetheme_config
        }

    #IFacets functions
    # Remove organization from faceted search
    def dataset_facets(self, facets_dict, package_type):
        return remove_facets(facets_dict, ['organization'])

    def group_facets(self, facets_dict, group_type, package_type):
        return remove_facets(facets_dict, ['organization'])

    def organization_facets(self, facets_dict, organization_type, package_type):
        return remove_facets(facets_dict, ['organization'])
