import ray
import anyscale
import os

from compute_1 import run_job

runtime_env = {
    "conda": {
        "dependencies":
        ["toolz", "dill", "pip", {
            "pip": ["pendulum"]
        }]
    }
    # "pip": ["pendulum"],
    # "env_vars": {"TF_WARNINGS": "none"}
}

print("This demo connects to anyscale and computes fib sequences")

# This command will use the environment variable RAY_ADDRESS 
# to connect to a ray cluster.
# If RAY_ADDRESS begins with "anyscale://" then your program 
# uses an Anyscale cluster to run Ray.
ray.init("anyscale://cluster_15", runtime_env=runtime_env)

N = 2000
print(f"Getting the {N}th fibonnaci number for you, a few times")

objs = [run_job.remote(N) for i in range(20)]

return_vals = ray.get(objs)
