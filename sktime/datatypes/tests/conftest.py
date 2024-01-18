"""Testing configuration file for datatypes."""

import pytest


@pytest.fixture(autouse=True)
def _change_current_dir():
    """Initialize ray to test modin mtypes."""
    import os
    import ray

    os.environ["MODIN_ENGINE"] = "ray"
    ray.init(num_cpus=1, object_store_memory=1 * 1024)
