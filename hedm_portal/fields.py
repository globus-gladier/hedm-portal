import os
from urllib.parse import urlsplit, urlunsplit, urlencode


def title(result):
    """The title for this Globus Search subject"""
    return result[0]["dc"]["titles"][0]["title"]


def globus_app_link(result):
    """A Globus Webapp link for the transfer/sync button on the detail page"""
    url = get_file(result).get("url")
    if not url:
        return
    parsed = urlsplit(url)
    query_params = {
        "origin_id": parsed.netloc,
        "origin_path": os.path.dirname(parsed.path),
    }
    return urlunsplit(
        ("https", "app.globus.org", "file-manager", urlencode(query_params), "")
    )


def https_url(result):
    """Add a direct download link to files over HTTPS"""
    url = get_file(result).get("url")
    if not url:
        return
    path = urlsplit(url).path
    return urlunsplit(("https", "g-71c9e9.10bac.8443.data.globus.org", path, "", ""))


def get_file(result):
    """To start, 'test' files are just a single file in a directory, so we'll always just look
    for the first file in the list."""
    return result[0]["files"][0]


def search_results(result):
    file_metadata = get_file(result)
    return [
        {
            "field": "name",
            "title": "Name",
            "value": file_metadata.get('filename')
        },
        {
            "field": "size",
            "title": "Size",
            "type": "int",
            "value": file_metadata.get('length')
        },
    ]