============
   PcfGcp
============

PcfGcp is a Python library intended to simplify consumption of Google Cloud Platform (GCP) services for apps deployed to
Cloud Foundry.  An example of usage would be::

    #!/usr/bin/env python

    from pcfgcp import PcfGcp

    pg = PcfGcp()
    client = pg.getVision()
    image = client.image(source_uri=some_uri)
    labels = []
    for label in image.detect_labels():
        labels.append(label.description.lower())
    # etc...

Here is an example entry for including this library, directly from this GitHub repo, in your app's requirements.txt::

    git+https://github.com/pivotal-partner-solution-architecture/pcf-gcp-python.git#egg=pcfgcp

Within Cloud Foundry, the GCP services are exposed by the GCP Service Broker (https://github.com/GoogleCloudPlatform/gcp-service-broker).
