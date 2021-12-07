import ray

ray.init()

@ray.remote(num_cpus=1)
class Foo:
  def foo(self):
    import time
    i = 0
    while True:
      i += 1
      print(f"hi {i}")
      time.sleep(10)

foos = [Foo.options(lifetime="detached").remote() for _ in range(16)]
[foo.foo.remote() for foo in foos]



