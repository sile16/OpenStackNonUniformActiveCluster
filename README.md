# OpenStack w/ActivCluster Doing Live Migrations with NonUniform FC Connectivity

[Video](https://youtu.be/H5WL8P0OKVQ)


## Zoning
| Source Device      | Source WWN         | Target Device       | Port  | Target WWN       |
|--------------------|--------------------|---------------------|-------|------------------|
| sn1-pool-c07-05    | 21000024ff8ab4ec   | sn1-x90r2-f05-27    | CTO.FC0 | 524A93732763AF00 |
|                    |                    | sn1-x90r2-f05-27    | CT1.FC0 | 524A93732763AF10 |
|                    | 21000024ff8ab4ed   | sn1-x90r2-f05-27    | CTO.FC1 | 524A93732763AF01 |
|                    |                    | sn1-x90r2-f05-27    | CT1.FC1 | 524A93732763AF11 |
| sn1-pool-c07-06    | 21000024ff59bf56   | sn1-x90r2-f05-33    | CTO.FC3 | 524A937C5A85A503 |
|                    |                    | sn1-x90r2-f05-33    | CT1.FC3 | 524A937C5A85A513 |
|                    | 21000024ff59bf57   | sn1-x90r2-f05-33    | CTO.FC2 | 524A937C5A85A502 |
|                    |                    | sn1-x90r2-f05-33    | CT1.FC2 | 524A937C5A85A512 |

### Shell commands

[link code](shellcmds.sh)

### Python SDK Setup

[link code](sdksetup.py)

### Mulitpath script that shows host & target WWNs

[link code](multipath.sh)

