"""Autograding script."""

# pylint: disable=broad-exception-raised

import os

import homework.word_count as wc


def test_01():
    """Test Word Count"""

    if os.path.exists("files/output/"):
        for file in os.listdir("files/output/"):
            os.remove(os.path.join("files/output/", file))
        os.rmdir("files/output/")

    wc.run_experiment(
        n=1000,
        mapper=wc.wordcount_mapper,
        reducer=wc.wordcount_reducer,
        raw_dir="files/raw",
        input_dir="files/input",
        output_dir="files/output",
    )

    if not os.path.exists("files/output/"):
        raise Exception("Output directory does not exist")

    if not os.path.exists("files/output/_SUCCESS"):
        raise Exception("Output directory is empty")

    with open("files/output/part-00000", "r", encoding="utf-8") as f:
        lines = f.readlines()
        result = {}
        for line in lines:
            key, value = line.strip().split("\t")
            result[key] = int(value)

    assert result["analytics"] == 5000
    assert result["business"] == 7000
    assert result["by"] == 3000
    assert result["algorithms"] == 2000
    assert result["analysis"] == 4000
