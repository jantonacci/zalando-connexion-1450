#!/usr/bin/env python3

import connexion

# See https://github.com/zalando/connexion#readme
# Also see https://connexion.readthedocs.io/en/latest/index.html
CONNEXION_APP_OPTS = {
    # See https://github.com/swagger-api/swagger-ui/blob/master/docs/usage/configuration.md
    'swagger_ui_config': {
        'defaultModelsExpandDepth': -1,
        'defaultModelExpandDepth': -1,
        'defaultModelRendering': 'model',  # ["example"*, "model"]
        'docExpansion': 'list',  # ["list"*, "full", "none"]
        'operationsSorter': 'alpha',
        'syntaxHighlight.theme': 'arta',  # ["agate"*, "arta", "monokai", "nord", "obsidian", "tomorrow-night"]
        'tryItOutEnabled': True,
        # 'persistAuthorization': True,
    }
}
api = connexion.App(__name__, options=CONNEXION_APP_OPTS)

# Load the OAS defined endpoints; use test.url_map.UrlMap() to review URL rules and examples
api.add_api('openapi.yaml')


# SwaggerUI redirect
# noinspection PyUnusedLocal
@api.route('/')
def swagger_ui_redirect(*args, **kwargs):
    location = {'location': '{}/ui'.format(list(api.app.blueprints)[0])}
    return location, 302, location


# noinspection PyUnusedLocal
@api.route('/license')
def view_get_license(*args, **kwargs):
    return """
    <html><body><pre>
    This is free and unencumbered software released into the public domain.

    Anyone is free to copy, modify, publish, use, compile, sell, or
    distribute this software, either in source code form or as a compiled
    binary, for any purpose, commercial or non-commercial, and by any
    means.
    
    In jurisdictions that recognize copyright laws, the author or authors
    of this software dedicate any and all copyright interest in the
    software to the public domain. We make this dedication for the benefit
    of the public at large and to the detriment of our heirs and
    successors. We intend this dedication to be an overt act of
    relinquishment in perpetuity of all present and future rights to this
    software under copyright law.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
    </pre></body></html>
    """


# noinspection PyUnusedLocal
@api.route('/docs')
def view_get_docs(*args, **kwargs):
    return """
    <html><body><pre>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
    est laborum.
    </pre></body></html>
    """


if __name__ == '__main__':
    api.run()
