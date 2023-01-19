import json
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def completion_with_backoff(openai_key, kwargs):
    openai.api_key = openai_key
    return openai.Completion.create(**kwargs)
    
class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def post(self):
        # input_data is a dictionary with a key "name"
        input_data = self.get_json_body()
        openai_key = input_data["openai_key"]
        params = input_data["params"]
        self.finish(json.dumps(completion_with_backoff(openai_key, params)))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "gpt-jupyterlab", "complete")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)
