import xml.etree.ElementTree as ET
from .models import Vulnerability

def parse_nessus(file_path, scan):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for host in root.iter("ReportHost"):
        hostname = host.attrib.get("name")

        for item in host.iter("ReportItem"):
            severity_map = {
                "0": "Info",
                "1": "Low",
                "2": "Medium",
                "3": "High",
                "4": "Critical",
            }

            Vulnerability.objects.create(
                scan=scan,
                host=hostname,
                plugin_name=item.attrib.get("pluginName"),
                severity=severity_map[item.attrib.get("severity")],
            )

