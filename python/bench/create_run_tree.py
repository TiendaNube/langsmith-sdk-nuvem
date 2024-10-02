import os
from unittest.mock import patch

from langsmith import RunTree

os.environ["LANGSMITH_***REMOVED***"] = "fake"


def create_run_trees(N: int):
    with patch("langsmith.client.requests.Session", autospec=True):
        for i in range(N):
            RunTree(name=str(i)).post()
