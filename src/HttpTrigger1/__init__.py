import logging
import urllib.request
import json
import xmltodict
import pandas

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = "https://status.sdpf.ntt.com/rss/ja/fic/japan-east/"
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = xmltodict.parse(data)
    x = data_dict['rss']['channel']['item']
    df = pandas.DataFrame.from_dict(x)
    md_data = df.to_markdown(index=False)
    json_data = json.dumps(data_dict['rss']['channel']['item'])

    return func.HttpResponse(
            md_data,
            status_code=200
    )
