import ray
from ray import serve

ray.init()

@serve.deployment
def hello_world(*args, **kwargs):
  return "hello world"

serve.start(detached=True)

hello_world.deploy()

