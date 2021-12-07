import ray

@ray.remote(num_cpus=1)
class Foo:
  def foo(self):
    import time
    i = 0
    while True:
      print(f"hi {i}")
      i += 1
      time.sleep(10)

ray.init() # cloud="anyscale_default_cloud")

foo = Foo.options(lifetime="detached", name="foo_actor").remote()

foo.foo.remote()
